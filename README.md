# YummyApp CI/CD - Bài thực hành 7

Dự án minh họa kiểm thử `unittest`, Mocking GPS, đo coverage và CI bằng GitHub Actions.

## Chạy trên Windows

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
coverage run -m unittest discover -s . -p "test_*.py"
coverage report -m
coverage html -d coverage_html
coverage report --fail-under=80
```

## Kiểm tra linter

```powershell
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```

## Những việc phải làm thủ công

- Cấu hình Git với đúng MSSV, họ tên và email sinh viên.
- Thực hiện các commit theo từng mốc và tự push lên repository GitHub.
- Chụp minh chứng CI FAILED/PASSED và Break the Build.
- Tải raw log của lần GitHub Actions thành công cuối cùng.
- Viết tay, ký tên và scan bốn trang minh chứng.
- Điền link repository và ảnh minh chứng vào báo cáo.

Xem `HUONG_DAN_VIET_TAY.md`, `BAO_CAO_KY_THUAT.md` và `CHECKLIST_NOP_BAI.md`.
