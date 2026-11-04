# CAMERA LIGHT SENSOR

## 1. Giới thiệu

Project sử dụng camera để phân tích độ sáng
của môi trường thông qua hình ảnh.

## 2. Công nghệ

- HTML
- CSS
- JavaScript
- Web Camera API
- Canvas API

## 3. Chức năng

- Bật và tắt camera.
- Phân tích độ sáng hình ảnh.
- Hiển thị giá trị ánh sáng.
- Phân loại môi trường sáng/tối.
- Cảnh báo khi thiếu ánh sáng.

## 4. Nguyên lý hoạt động

Camera thu hình ảnh.
JavaScript đọc dữ liệu pixel.
Canvas phân tích giá trị RGB.
Tính độ sáng trung bình.
So sánh với ngưỡng phân loại.

## 5. Ngưỡng ánh sáng

| Giá trị | Trạng thái |
|---|---|
| 0 - 79 | Tối |
| 80 - 169 | Bình thường |
| 170 - 255 | Sáng |

## 6. Cách chạy

Mở index.html bằng Live Server trong VS Code.
Cho phép trình duyệt truy cập camera.
Nhấn Bật Camera để bắt đầu.
