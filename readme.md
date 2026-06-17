# Báo Cáo Kiểm Thử Selenium - SauceDemo

## 1) Mục tiêu

Dự án này dùng Selenium + Pytest để kiểm thử các chức năng cơ bản của website demo [SauceDemo](https://www.saucedemo.com):

- Đăng nhập thành công/thất bại
- Thêm sản phẩm vào giỏ hàng
- Xóa sản phẩm khỏi giỏ hàng
- Đăng xuất khỏi hệ thống

## 2) Công nghệ và thư viện

- Python 3.13
- Selenium 4.x
- Pytest 8.x
- webdriver-manager
- pytest-html

## 3) Cấu trúc dự án

- `pages/`: Page Object Model (`login_page.py`, `inventory_page.py`)
- `tests/`: Test cases và fixtures (`conftest.py`, `test_login.py`, `test_cart.py`, `test_logout.py`)
- `reports/screenshots/`: Ảnh chụp màn hình tự động khi chạy test
- `requirements.txt`: Danh sách thư viện cần cài

## 4) Danh sách test case

- **TC01**: Đăng nhập thành công với tài khoản hợp lệ
- **TC02**: Đăng nhập thất bại khi sai mật khẩu
- **TC03**: Đăng nhập thất bại khi bỏ trống username
- **TC04**: Thêm sản phẩm vào giỏ hàng
- **TC05**: Xóa sản phẩm khỏi giỏ hàng
- **TC06**: Đăng xuất thành công

## 5) Kết quả chạy test hiện tại

Kết quả gần nhất:

- `6 passed in ~71s`

Tất cả test case đều đã pass.

## 6) Cơ chế chụp ảnh khi test

Đã cấu hình trong `tests/conftest.py`:

- Tự động chụp ảnh ở phase `call`
- Đang chụp cả test **pass** và **fail**
- Ảnh được lưu tại: `reports/screenshots/`
- Tên file gồm: tên testcase + trạng thái (`PASSED`/`FAILED`) + timestamp

> Nếu muốn chỉ chụp khi fail, đổi `CAPTURE_SCREENSHOT_ON_PASS = False` trong `tests/conftest.py`.

## 7) Cách chạy dự án

### Cài đặt thư viện

```bash
pip install -r requirements.txt
```

### Chạy toàn bộ test

```bash
pytest -q
```

### Chạy 1 test cụ thể

```bash
pytest -vv tests/test_logout.py::TestLogout::test_TC06_logout_success
```

## 8) Ghi chú kỹ thuật

- Đã xử lý lỗi import `ModuleNotFoundError: No module named 'pages'` bằng cách bổ sung package marker và đảm bảo project root có trong `sys.path`.
- Đã xử lý tình huống `webdriver-manager` trả sai đường dẫn binary bằng fallback sang `chromedriver.exe`.
- Đã ổn định hóa luồng test logout để đảm bảo testcase pass nhất quán.
