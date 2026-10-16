# Checklist hoàn thiện và đóng gói

## Minh chứng còn phải tự thực hiện

- [ ] Bốn trang viết tay đã scan thành `MinhChung_VietTay_MSSV.pdf`.
- [ ] Mỗi trang có họ tên, MSSV, ngày, chữ ký tươi bằng bút mực xanh.
- [ ] Đã chụp CI FAILED vì Quality Gate và CI PASSED sau khi thêm test.
- [ ] Đã chụp Break the Build FAILED và lần sửa lỗi PASSED.
- [ ] `logs/git_history.log` được xuất từ lịch sử commit thật.
- [ ] `logs/github_actions_run.log` là raw log thật từ lần Actions thành công cuối.
- [ ] Báo cáo đã điền thông tin, link GitHub và ảnh; đã xuất `BaoCao_KetQua_Lab7.pdf`.

## Xuất log thật

```powershell
git log --graph --pretty=format:"%h - %an (%ad): %s" | Out-File -Encoding utf8 logs/git_history.log
```

Trong GitHub: **Actions -> lần chạy thành công cuối -> menu ba chấm -> View raw logs/Download log archive**; lưu nội dung thành `logs/github_actions_run.log`.

## Đóng gói

Chỉ tạo `MSSV_HoTen_Lab7.zip` sau khi toàn bộ checklist đã hoàn tất. Không đưa `.venv`, `__pycache__`, `.git`, `.coverage`, `coverage_html` hoặc file tạm vào ZIP.
