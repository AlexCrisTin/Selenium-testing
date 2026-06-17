"""
tests/test_login.py

TC01 – Đăng nhập thành công với tài khoản hợp lệ
TC02 – Đăng nhập thất bại khi nhập sai mật khẩu
"""

import pytest
from pages.login_page import LoginPage


class TestLogin:

    # ──────────────────────────────────────────────
    # TC01: Đăng nhập thành công
    # ──────────────────────────────────────────────
    def test_TC01_login_success(self, driver):
        """
        Mô tả : Kiểm tra người dùng đăng nhập thành công với thông tin hợp lệ.
        Bước  :
            1. Mở trang https://www.saucedemo.com
            2. Nhập username = 'standard_user'
            3. Nhập password = 'secret_sauce'
            4. Bấm nút Login
        Kỳ vọng : Hệ thống chuyển hướng sang trang /inventory.html
        """
        page = LoginPage(driver)
        page.open().login("standard_user", "secret_sauce")

        assert page.is_on_inventory_page(), (
            f"[TC01 FAIL] Sau khi đăng nhập URL phải chứa '/inventory.html', "
            f"nhưng thực tế là: {driver.current_url}"
        )

    # ──────────────────────────────────────────────
    # TC02: Đăng nhập thất bại – sai mật khẩu
    # ──────────────────────────────────────────────
    def test_TC02_login_fail_wrong_password(self, driver):
        """
        Mô tả : Kiểm tra hệ thống hiển thị thông báo lỗi khi mật khẩu sai.
        Bước  :
            1. Mở trang https://www.saucedemo.com
            2. Nhập username = 'standard_user'
            3. Nhập password = 'wrong_password'
            4. Bấm nút Login
        Kỳ vọng : Hiển thị thông báo lỗi có nội dung 'Username and password do not match'
        """
        page = LoginPage(driver)
        page.open().login("standard_user", "wrong_password")

        error_msg = page.get_error_message()
        assert "Username and password do not match" in error_msg, (
            f"[TC02 FAIL] Thông báo lỗi không đúng. Nhận được: '{error_msg}'"
        )
        assert not page.is_on_inventory_page(), (
            "[TC02 FAIL] Không nên chuyển sang trang inventory khi đăng nhập thất bại."
        )

    # ──────────────────────────────────────────────
    # TC03 (bonus): Đăng nhập thất bại – để trống username
    # ──────────────────────────────────────────────
    def test_TC03_login_fail_empty_username(self, driver):
        """
        Mô tả : Kiểm tra hệ thống hiển thị lỗi khi username bị để trống.
        Bước  :
            1. Mở trang https://www.saucedemo.com
            2. Không nhập username
            3. Nhập password = 'secret_sauce'
            4. Bấm nút Login
        Kỳ vọng : Hiển thị thông báo 'Username is required'
        """
        page = LoginPage(driver)
        page.open().login("", "secret_sauce")

        error_msg = page.get_error_message()
        assert "Username is required" in error_msg, (
            f"[TC03 FAIL] Thông báo lỗi không đúng. Nhận được: '{error_msg}'"
        )
