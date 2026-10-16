# Quy trình GitHub cần thực hiện thủ công

Không chạy `git push` hoặc tạo commit trước khi đã điền đúng danh tính sinh viên.

## 1. Cấu hình Git

```powershell
git init
git branch -M main
git config user.name "MSSV - Ho Va Ten"
git config user.email "mssv@dlu.edu.vn"
```

Kiểm tra lại bằng `git config user.name` và `git config user.email`.

## 2. Ghi nhận Quality Gate FAILED thật

Để lịch sử đúng tiến trình bài thực hành, trước commit này chỉ giữ bốn test trong `TestEasyLevel`; tạm lưu hai lớp `TestMediumLevel` và `TestHardLevel` ở ngoài repository. Không sửa `yummy_app.py`.

1. Chạy test và xác nhận bốn test cơ bản vẫn PASS.
2. Commit phiên bản workflow đã có `coverage report --fail-under=80`:

   ```powershell
   git add .
   git commit -m "MSSV: add 80 percent coverage quality gate"
   git push -u origin main
   ```

3. Mở GitHub Actions, xác nhận bước 5 FAILED do coverage dưới 80% và chụp màn hình có commit/run ID.
4. Khôi phục hai lớp test từ file hiện tại, chạy lại 11 test và coverage.
5. Commit, push và chụp lần chạy PASSED:

   ```powershell
   git add test_yummy_app.py logs/local_test.log
   git commit -m "MSSV: add promo and GPS mocking tests"
   git push
   ```

Không chỉnh số liệu coverage hoặc log bằng tay.

## 3. Break the Build

Sau khi đã có lần PASS:

1. Thêm tạm một dòng sai cú pháp rõ ràng vào cuối `yummy_app.py`, ví dụ `def broken_syntax(`.
2. Commit và push lỗi có chủ đích.
3. Trong Actions, xác nhận bước **Static Code Analysis (Linter)** FAILED và chụp màn hình.
4. Xóa đúng dòng lỗi vừa thêm, chạy linter/test cục bộ lại.
5. Commit, push bản sửa và chụp lần chạy PASSED.

Không để lỗi có chủ đích trong bài nộp cuối cùng.

## 4. Tải raw log và xuất lịch sử

Mở lần chạy Actions thành công cuối, chọn menu ba chấm rồi **View raw logs** hoặc **Download log archive**. Lưu log thật thành `logs/github_actions_run.log`.

```powershell
git log --graph --pretty=format:"%h - %an (%ad): %s" | Out-File -Encoding utf8 logs/git_history.log
```

Chạy lại lệnh trên sau commit cuối để log chứa đầy đủ lịch sử.
