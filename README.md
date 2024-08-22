## ⚠️ Requirements
    Python >= 3.8.x
    pip >= 24.0

# 🚀 Setup and Deployment
### Lưu ý: 
Để dùng được chatbot sinh câu hỏi, bạn phải tạo file .env với nội dung là các API key (của bạn) tương ứng như hình dưới đây (với mỗi cách triển khai, bạn hãy xem hướng dẫn từng cách đó để biết file .env được tạo ở đâu):  
![env](https://github.com/user-attachments/assets/2ca66518-8d6e-40bb-8289-c6d68a5af2ab)  

## Cách 1: Cài Đặt và Khởi Chạy Ứng Dụng Python
### 1. Clone repository
### 2. Tải các thư viện cần thiết  
```bash
pip install -r requirements.txt
```
Sau đó bạn cần phải tạo file **.env** trong thư mục gốc là **generate-quizzes-chatbot** (Xem lưu ý của **🚀 Setup and Deployment** để biết nội dung của file .env)  
### 3. Chạy python server
  - Nếu muốn dùng chatbot với dữ liệu được lưu trên pinecone (có raw-data và structured-data) thì xem file **pinecone-with-raw-data.md** và **pinecone-with-structured-data.md** hướng dẫn tương ứng trong các thư mục pinecone/raw-data và pinecone/structured-data.

## Cách 2: Triển Khai Ứng Dụng Với Docker 🐳
Hoàn toàn dùng Terminal để chạy lệnh  
### 1. Tải Docker  
### 2. Đăng nhập vào Docker  
Chạy Docker và mở Terminal để chạy cách dòng lệnh dưới đây:
```bash
docker login -u username_của_bạn
```
Nhập password và login thành công:  
![Screenshot 2024-08-19 132648](https://github.com/user-attachments/assets/e3359704-8962-472c-b908-a999a2f4e59d)  
### 3. Pull image về máy  
Lưu ý image này chỉ sử dụng chatbot với dữ liệu thô được lưu trên pinecone:
```bash
docker pull lananh15/generate-quizzes-chatbot:v1
```
Sau khi pull về kiểm tra bằng lệnh `docker images` sẽ thấy image như hình:  
![Screenshot 2024-08-19 133005](https://github.com/user-attachments/assets/c219d618-2e22-4a93-8a3f-5db0245fb575)  
### 4. Chạy container  
Bạn phải tạo file **.env** tại vị trí thư mục đang đứng trong terminal (Xem lưu ý của **🚀 Setup and Deployment** để biết nội dung của file .env), sau đó khởi động container:  
```bash
docker run --name generate-quizzes-chatbot-v1 -dp 5000:5000 --env-file .env lananh15/generate-quizzes-chatbot:v1
```
Kiểm tra container chạy hay chưa bằng `docker ps -a` thấy như hình dưới là được:  
![Screenshot 2024-08-19 133507](https://github.com/user-attachments/assets/2c3c6748-e57d-47a3-9a12-c869d3a9c6ff)  
Lúc này bạn có thể dùng Chatbot bằng cách truy cập vào http://127.0.0.1:5000/  
![Screenshot 2024-08-19 134243](https://github.com/user-attachments/assets/f11f2571-6abf-4659-902c-1fbacd3db42a)  

# 📝 About Chatbot
Chatbot hỗ trợ sinh câu hỏi trắc nghiệm cho môn học "Quản lý dự án CNTT" với nội dung môn học gồm 8 chương:  
### Chương 1. Tổng quan
- Khái niệm về quản lý
- Sự cần thiết của quản lý dự án
  - Các thống kê về quản lý dự án
  - Dự án thất bại
  - Ưu điểm của quản lý dự án
- Khái niệm dự án
  - Khái niệm
  - 4 yếu tố quan trọng
  - Các thuộc tính của dự án
  - Dự án công nghệ thông tin
- Phân loại dự án
  - Theo tầm cỡ dự án
  - Theo nội dung dự án
  - Các cách phân loại khác
- Quản lý dự án là gì
- Các giai đoạn của dự án Công nghệ Thông Tin
  - Giai đoạn xác định
  - Giai đoạn phân tích
  - Giai đoạn thiết kế
  - Giai đoạn thực hiện
  - Giai đoạn kiểm thử hệ thống
  - Giai đoạn kiểm thử chấp nhận
  - Giai đoạn vận hành  

### Chương 2. Cơ cấu quản lý dự án
- Bộ ba ràng buộc của quản lý dự án
- Các lĩnh vực kiến thức trong quản lý dự án
  - Chín lĩnh vực kiến thức cần phát triển
  - Bốn lĩnh vực quản lý cơ bản
  - Bốn lĩnh vực hỗ trợ
  - Lĩnh vực tích hợp (project integration management)
- Các công cụ và kỹ thuật
- Các kỹ năng cần thiết  

### Chương 3. Quy trình quản lý dự án
- Quy trình khởi động
- Quy trình lập kế hoạch
- Quy trình thực thi
- Quy trình điều khiển
- Quy trình kết thúc  

### Chương 4. Quản lý phạm vi
- Quản lý phạm vi là gì
- Khởi động (Initiation)
  - Quy trình chọn dự án
  - Phương pháp chọn lựa dự án
  - Project Charter (tuyên bố dự án)
- Lập kế hoạch phạm vi (Scope Planning)
- Xác định phạm vi (Scope Definition)
- Cấu trúc phân rã công việc (WBS – Work Break-down Structure)
- Kiểm tra và điều khiển thay đổi phạm vi (Verification & Controling)  

### Chương 5. Quản lý thời gian
- Giới thiệu
- Các quy trình quản lý thời gian dự án
  - Xác định các hoạt động
  - Sắp xếp thứ tự các hoạt động
  - Ước lượng thời gian cho mỗi hoạt động
  - Phát triển lịch biểu
  - Kiểm soát lịch biểu
- Các công cụ và kỹ thuật ước lượng thời gian
  - Sử dụng ý kiến chuyên gia
  - Ước lượng dựa vào lịch sử
  - Kỹ thuật PERT
  - Phương pháp đường găng CPM
  - Sơ đồ Gantt
- Các kỹ thuật rút ngắn lịch biểu
- Kết luận  

### Chương 6. Quản lý chi phí
- Giới thiệu
- Khái niệm về quản lý chi phí
- Quy trình quản lý chi phí
  - Lập kế hoạch quản lý chi phí
  - Ước lượng chi phí
  - Dự toán ngân sách
  - Kiểm soát – điều chỉnh
- Lập kế hoạch quản lý chi phí
- Ước lượng chi phí
  - Các loại ước lượng chi phí
  - Các phương pháp để ước lượng chi phí dự án
- Dự toán chi phí
- Kiểm soát và điều chỉnh chi phí
- EVM (Earned Value Management)  

### Chương 7. Quản lý rủi ro
- Khái niệm rủi ro
- Quy trình quản lý rủi ro
  - Xác định rủi ro
  - Phân tích rủi ro
  - Lập kế hoạch đối phó
  - Kiểm soát rủi ro  

### Chương 8. Quản lý chất lượng
- Khái niệm
- Quy trình quản lý chất lượng
  - Lập kế hoạch quản lý chất lượng
  - Thực hiện đảm bảo chất lượng
  - Kiểm soát chất lượng
- Các công cụ và kỹ thuật quản lý chất lượng
  - Seven Basic Tools
    - Biểu đồ nguyên nhân kết quả (xương cá)
    - Biểu đồ kiểm soát
    - Phiếu kiểm soát (checksheet)
    - Biểu đồ phân tán (scatter diagram)
    - Biểu đồ tần suất (histogram)
    - Biểu đồ Pareto
    - Biểu đồ flowchart
  - Six sigma

# 📚 Reference slides for data of Chatbot
- Chương 1: Tổng quan [Xem ngay](https://drive.google.com/file/d/1x39z2P05V_opGRKuhmcYlv2zew-2gUtS/view?usp=sharing)
- Chương 2: Cơ cấu quản lý dự án [Xem ngay](https://drive.google.com/file/d/1o7wxjtSfLGtvvh-bRjNnUZ1JT-MlosY6/view?usp=sharing)
- Chương 3: Quy trình quản lý dự án [Xem ngay](https://drive.google.com/file/d/1drsYxju-NwqXVlf4XyXVHedbBuzqzP60/view?usp=sharing)
- Chương 4: Quản lý phạm vi [Xem ngay](https://drive.google.com/file/d/1Ypes5nAxphjN5pBAkQeR2avmTQV7gJ7E/view?usp=sharing)
- Chương 5: Quản lý thời gian [Xem ngay](https://drive.google.com/file/d/1Tf-mpLD4ip2DFYSa2LRH9FbWnSlqz1En/view?usp=sharing)
- Chương 6: Quản lý chi phí [Xem ngay](https://drive.google.com/file/d/1VopOg0HCD7AdKZmDbx8zBfavMQS2wiz5/view?usp=sharing)
- Chương 7: Quản lý rủi ro [Xem ngay](https://drive.google.com/file/d/1W5Twm2s6YMXDFOmwsmGRuNfN2WiMgmEx/view?usp=sharing)
- Chương 8: Quản lý chất lượng [Xem ngay](https://drive.google.com/file/d/1ikRiCLtJw6jyP2yAuLoUO1Jo58Iq6TA5/view?usp=sharing)
