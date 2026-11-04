# Camera Light Sensor – Basic

Website dùng webcam và JavaScript để ước lượng độ sáng trung bình của hình ảnh theo thời gian thực.

## Chức năng
- Bật/tắt webcam.
- Đọc hình ảnh bằng Web Camera API.
- Phân tích pixel bằng Canvas API.
- Tính độ sáng trung bình từ 0 đến 255.
- Phân loại Tối, Bình thường hoặc Sáng.
- Hiển thị thanh đo và cảnh báo thiếu sáng.

## Công nghệ
HTML5, CSS3, JavaScript, MediaDevices API và Canvas API. Không cần cài thư viện ngoài.

## Cấu trúc
```text
Camera_Light_Sensor/
├── index.html
├── README.md
├── css/
│   └── style.css
└── js/
    └── app.js
```

## Cách chạy trên Windows
1. Cài VS Code và Chrome hoặc Edge.
2. Mở repository bằng VS Code.
3. Cài extension **Live Server**.
4. Mở `Camera_Light_Sensor/index.html`.
5. Chuột phải → **Open with Live Server**.
6. Cho phép camera khi trình duyệt hỏi quyền.
7. Nhấn **Bật camera** để bắt đầu.

Camera thường chỉ hoạt động trên HTTPS hoặc localhost, không nên mở trực tiếp bằng `file://`.

## Nguyên lý
1. `getUserMedia()` xin quyền và lấy luồng camera.
2. Thẻ `video` hiển thị hình ảnh.
3. `drawImage()` vẽ khung hình thu nhỏ lên Canvas.
4. `getImageData()` đọc dữ liệu RGB.
5. Chuyển pixel sang độ sáng: `Y = 0.299R + 0.587G + 0.114B`.
6. Tính trung bình và phân loại theo ngưỡng.

## Ngưỡng mặc định
| Giá trị | Trạng thái |
|---:|---|
| 0–79 | Tối |
| 80–169 | Bình thường |
| 170–255 | Sáng |

Có thể thay đổi ngưỡng trong hàm `updateDisplay()` ở `js/app.js`.

## Lưu ý
- Chỉ số 0–255 là độ sáng tương đối của pixel, **không phải lux**.
- Kết quả phụ thuộc camera, phơi sáng tự động, góc quay và nội dung trong khung hình.
- Hình ảnh được xử lý trong trình duyệt, không tải lên máy chủ.
