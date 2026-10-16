# Hướng dẫn chuẩn bị 4 trang minh chứng viết tay

Tự viết bằng bút mực xanh. Trên mỗi trang ghi **Họ tên, MSSV, ngày thực hành và chữ ký tươi**. Không dùng chữ ký hoặc ảnh tạo tự động.

## Trang 1 - Sơ đồ CI Pipeline

Vẽ sáu khối nối bằng mũi tên:

`Git Push Event -> Checkout Code -> Setup Python 3.11 -> Install Dependencies -> Execute Unit Tests -> Quality Gate`

Ghi chú ngắn: Quality Gate chỉ cho pipeline thành công khi linter sạch, test đạt và coverage từ 80% trở lên.

## Trang 2 - Ma trận 7 test case

Kẻ bốn cột: **Tên Test Case | Hàm được gọi | Đối tượng và giá trị Mocking | Kết quả kỳ vọng**.

| Tên test case | Hàm được gọi | Mocking | Kết quả kỳ vọng |
|---|---|---|---|
| Online, GIAM10 | `apply_promo_code(100000, "GIAM10")` | Không cần mock; online, OS 15 | `90000` |
| Offline | `apply_promo_code(...)` | Không cần mock; offline | Ném `ConnectionError` |
| NEW_OS_ONLY, OS 15 | `apply_promo_code(100000, "NEW_OS_ONLY")` | Không cần mock; OS 15 | `80000` |
| NEW_OS_ONLY, OS 14 | `apply_promo_code(...)` | Không cần mock; OS 14 | Ném `ValueError` |
| GPS trong vùng | `get_nearby_restaurants()` | GPS trả `(10.0, 105.0)` | Danh sách 2 nhà hàng |
| GPS ngoài vùng | `get_nearby_restaurants()` | GPS trả `(20.0, 110.0)` | Danh sách rỗng |
| Mất GPS | `get_nearby_restaurants()` | GPS ném `GPSSignalLostError` | Chuỗi `Khong the xac dinh vi tri.` |

## Trang 3 - Câu 2.1, 2.2, 2.3

- **2.1:** Linter đặt trước test để phát hiện nhanh lỗi cú pháp, import hoặc tên chưa định nghĩa. Pipeline dừng sớm, không tốn thời gian chạy test trên mã chắc chắn không hợp lệ.
- **2.2:** `coverage report --fail-under=80` trả mã thoát khác 0 khi tổng coverage dưới 80%. Shell chuyển mã này cho GitHub Actions; mã khác 0 làm bước và job thất bại, còn mã 0 là thành công.
- **2.3:** `-m` hiển thị số dòng chưa được chạy. Kỹ sư dựa vào các dòng này để tìm nhánh xử lý còn thiếu test và bổ sung ca kiểm thử có mục đích.

## Trang 4 - Câu 3.1, 3.2, 3.3

- **3.1:** Flaky test lúc đạt lúc trượt dù mã không đổi, thường do thời gian, thứ tự chạy, dữ liệu dùng chung hoặc dịch vụ không ổn định. Sai lệch môi trường phụ thuộc xảy ra có hệ thống khi máy local và CI dùng phiên bản thư viện, hệ điều hành hoặc cấu hình khác nhau.
- **3.2:** Ghim phiên bản giúp mọi máy cài cùng dependency, tạo build tái lập, tránh bản cập nhật ngoài ý muốn làm test hỏng hoặc thay đổi hành vi.
- **3.3:** Sáu bước: tạo nhánh nâng cấp; cập nhật phiên bản; cài và chạy linter/test/coverage; đọc release notes và kiểm tra tương thích; mở Pull Request để CI và reviewer kiểm tra; merge khi mọi kiểm tra đạt rồi giám sát sau triển khai.
