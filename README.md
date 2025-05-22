Tổng quan dự án
1. Mô tả tổng quan
Dự án xây dựng một ứng dụng web cho phép người dùng thực hiện mã hóa và giải mã tệp tin bằng thuật toán AES (Advanced Encryption Standard). Đây là một thuật toán mã hóa đối xứng hiện đại, được sử dụng rộng rãi nhờ tính an toàn và hiệu quả cao. Ứng dụng hỗ trợ người dùng tải tệp lên, nhập khóa bí mật, lựa chọn thao tác (mã hóa hoặc giải mã), và nhận lại kết quả là tệp đã được xử lý.
2. Mục tiêu
- Tăng cường bảo mật thông tin trong quá trình lưu trữ hoặc truyền tải qua mạng.
- Hỗ trợ người dùng dễ dàng sử dụng mã hóa/giải mã mà không cần kiến thức chuyên sâu.
- Thay thế các thuật toán cũ không còn an toàn như DES bằng AES hiện đại.
3. Công nghệ sử dụng
Thành phần	Công nghệ
Backend	Python, Flask
Mã hóa	PyCryptodome (AES)
Giao diện	HTML, CSS, Bootstrap
4. Cơ chế mã hóa và giải mã
- Thuật toán sử dụng: AES – chế độ CBC (Cipher Block Chaining)
- Khóa mã hóa:
  + Người dùng nhập từ giao diện web.
  + Yêu cầu tối thiểu 8 ký tự, được chuẩn hóa thành 16 byte để phù hợp với AES-128.
- IV (Initialization Vector):
  + Tạo ngẫu nhiên mỗi lần mã hóa.
  + Gắn vào đầu dữ liệu mã hóa để phục vụ giải mã.
- Padding: Áp dụng chuẩn PKCS7 để bổ sung dữ liệu phù hợp với độ dài khối AES.
5. Các chức năng chính
- Cho phép tải tệp lên từ thiết bị cá nhân.
- Nhập khóa bí mật để mã hóa hoặc giải mã.
- Lựa chọn thao tác: mã hóa hoặc giải mã tệp.
- Trả về tệp kết quả để người dùng tải xuống.
  ![image](https://github.com/user-attachments/assets/1641b0d4-b5ac-4986-bad7-33761a5da9e6)
6. Ưu điểm của ứng dụng
- Giao diện đơn giản, thân thiện, phù hợp cả với người không chuyên về kỹ thuật.
- Đảm bảo tính bảo mật cao nhờ sử dụng chuẩn AES.
- Dữ liệu xử lý trực tiếp, không lưu trữ vĩnh viễn trên máy chủ.
- Có khả năng mở rộng hỗ trợ các thuật toán khác như RSA, Blowfish, Twofish,...
