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
| ID | Tên kịch bản kiểm thử | Mô tả các bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :---: |
| **TC01** | Đăng nhập thành công | 1. Truy cập `saucedemo.com`<br>2. Nhập username `standard_user`<br>3. Nhập password `secret_sauce`<br>4. Nhấp nút Login | Chuyển hướng sang trang sản phẩm `inventory.html`. | **Passed** |
| **TC02** | Đăng nhập thất bại (sai mật khẩu) | 1. Truy cập `saucedemo.com`<br>2. Nhập username `standard_user`<br>3. Nhập password sai<br>4. Nhấp nút Login | Hiển thị thông báo lỗi chứa nội dung "Username and password do not match". | **Passed** |
| **TC03** | Đăng nhập thất bại (trống username) | 1. Truy cập `saucedemo.com`<br>2. Để trống username<br>3. Nhập password `secret_sauce`<br>4. Nhấp nút Login | Hiển thị thông báo lỗi chứa nội dung "Username is required". | **Passed** |
| **TC04** | Thêm sản phẩm vào giỏ hàng | 1. Đăng nhập thành công<br>2. Thêm sản phẩm đầu tiên vào giỏ hàng | Badge giỏ hàng hiển thị số lượng bằng `1`. | **Passed** |
| **TC05** | Xóa sản phẩm khỏi giỏ hàng | 1. Đăng nhập thành công<br>2. Thêm sản phẩm đầu tiên vào giỏ hàng<br>3. Nhấp `Remove` để xóa | Badge giỏ hàng biến mất và số lượng trở về `0`. | **Passed** |
| **TC06** | Đăng xuất khỏi hệ thống | 1. Đăng nhập thành công<br>2. Mở menu bên trái<br>3. Nhấp `Logout` | Trở về trang đăng nhập và hiển thị lại các trường nhập liệu. | **Passed** |

## 5) Kết quả chạy test hiện tại

Kết quả gần nhất:

<img width="1068" height="204" alt="image" src="https://github.com/user-attachments/assets/f3296339-aefb-4652-b5bf-baf2dcb27a0e" />


Tất cả test case đều đã pass.
### Chi tiết các bước thực hiện và ảnh minh họa

#### Test đăng nhập

<img width="1262" height="648" alt="tests_test_login py_TestLogin_test_TC01_login_success_PASSED_20260617_164833" src="https://github.com/user-attachments/assets/e405e408-a475-4441-86e5-d6a40454c5bf" />


#### Test đăng nhập thất bại sai tên đăng nhập

<img width="1262" height="648" alt="tests_test_login py_TestLogin_test_TC02_login_fail_wrong_password_PASSED_20260617_164841" src="https://github.com/user-attachments/assets/2669d82e-ada0-4184-9e95-7155a20a5b0e" />


#### Test đăng nhập thất bại sai mật khẩu

<img width="1262" height="648" alt="tests_test_login py_TestLogin_test_TC03_login_fail_empty_username_PASSED_20260617_164850" src="https://github.com/user-attachments/assets/7c88cb25-7e8e-4aee-b1e2-e28980379e47" />




#### Test cho vào giỏ hàng 


<img width="1262" height="648" alt="tests_test_cart py_TestCart_test_TC04_add_product_to_cart_PASSED_20260617_164756" src="https://github.com/user-attachments/assets/5ad6d726-3c6d-471b-8d21-d447a9cb7b7c" />



#### Test loại bỏ khỏi giỏ hàng

<img width="1262" height="648" alt="tests_test_cart py_TestCart_test_TC05_remove_product_from_cart_PASSED_20260617_164824" src="https://github.com/user-attachments/assets/c6805f12-867e-4c3e-b7a4-08cd20669e72" />


#### Test đăng xuất

<img width="1262" height="648" alt="tests_test_logout py_TestLogout_test_TC06_logout_success_PASSED_20260617_164859" src="https://github.com/user-attachments/assets/23a4c3d0-ebba-4c9c-ad4b-f278c5c9542d" />

## 6) Cách chạy dự án

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
