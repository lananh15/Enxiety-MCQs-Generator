from openai import OpenAI
from pinecone import Pinecone, ServerlessSpec
import hashlib
import json
import logging
import os
from dotenv import load_dotenv

# Đọc tệp cấu hình
load_dotenv()

# Khởi tạo OpenAI
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# Tạo đối tượng Pinecone
pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))

# Kết nối đến index đã tồn tại
index_name = "generate-quizz"
# Kiểm tra xem index có tồn tại không và xóa nếu có
if index_name in pc.list_indexes().names():
    pc.delete_index(index_name)
# Tạo mới nếu chưa tồn tại
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=1536,  # Đảm bảo dimension khớp với model embedding bạn sử dụng
        metric='cosine',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )

index = pc.Index(index_name)

# Định nghĩa đường dẫn thư mục chứa script
script_dir = os.path.dirname(__file__)

# Lên 2 cấp thư mục và kết hợp với tên file 'qtda.json'
json_path = os.path.join(script_dir, '../..', 'data', 'qtda.json')

# Chuẩn hóa đường dẫn để loại bỏ các thành phần dư thừa (nếu có)
json_path = os.path.abspath(json_path)
# Load file JSON
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

def get_embeddings(text):
    response = openai_client.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding

# Function to upsert data to Pinecone
def upsert_data(vector_id, embedding, metadata):
    logging.info(f"Upserting vector ID: {vector_id}")
    index.upsert([(vector_id, embedding, metadata)])

# Duyệt qua dữ liệu và thêm vào Pinecone
for chapter in data['chapters']:
    for heading in chapter['headings']:
        vector_id = hashlib.sha256(f"{chapter['title']}_{heading['title']}_{heading['content']}".encode()).hexdigest()
        embedding = get_embeddings(heading['content'])
        metadata = {
            'chapter_title': chapter['title'],
            'heading_title': heading['title'],
            'heading_content': heading['content'],
            'keywords': heading['keywords']
        }
        upsert_data(vector_id, embedding, metadata)
        
        for subheading in heading.get('subheadings', []):
            vector_id = hashlib.sha256(f"{chapter['title']}_{heading['title']}_{subheading['title']}_{subheading['content']}".encode()).hexdigest()
            embedding = get_embeddings(subheading['content'])
            metadata = {
                'chapter_title': chapter['title'],
                'heading_title': heading['title'],
                'subheading_title': subheading['title'],
                'subheading_content': subheading['content'],
                'keywords': subheading['keywords']
            }
            upsert_data(vector_id, embedding, metadata)

            # Xử lý subheadings con bên trong subheadings cha
            for subsubheading in subheading.get('subsubheadings', []):
                vector_id = hashlib.sha256(f"{chapter['title']}_{heading['title']}_{subheading['title']}_{subsubheading['title']}_{subsubheading['content']}".encode()).hexdigest()
                embedding = get_embeddings(subsubheading['content'])
                metadata = {
                    'chapter_title': chapter['title'],
                    'heading_title': heading['title'],
                    'subheading_title': subheading['title'],
                    'subsubheading_title': subsubheading['title'],
                    'subsubheading_content': subsubheading['content'],
                    'keywords': subsubheading['keywords']
                }
                upsert_data(vector_id, embedding, metadata)

def search(query):
    query_embedding = get_embeddings(query)
    result = index.query(vector=query_embedding, top_k=5, include_metadata=True)
    return result

# Ví dụ truy vấn
query = "Seven basic tools"
results = search(query)

for match in results['matches']:
    print(f"Chapter: {match['metadata']['chapter_title']}")
    if 'subsubheading_title' in match['metadata']:
        print(f"Subsubheading title: {match['metadata']['subsubheading_title']}")
        print(f"Content: {match['metadata']['subsubheading_content']}")
    elif 'subheading_title' in match['metadata']:
        print(f"Subheading title: {match['metadata']['subheading_title']}")
        print(f"Content: {match['metadata']['subheading_content']}")
    else:
        print(f"Heading title: {match['metadata']['heading_title']}")
        print(f"Content: {match['metadata']['heading_content']}")
    print(f"Keywords: {match['metadata'].get('keywords', [])}")
    print("-" * 50)
