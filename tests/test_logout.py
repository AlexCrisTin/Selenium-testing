"""
tests/test_logout.py

TC06 – Đăng xuất khỏi hệ thống
"""

import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


class TestLogout:

    # ──────────────────────────────────────────────
    # TC06: Đăng xuất thành công
    # ──────────────────────────────────────────────
    def test_TC06_logout_success(self, logged_in_driver):
        """
        Mô tả  : Kiểm tra chức năng đăng xuất khỏi hệ thống.
        Pre-condition : Người dùng đã đăng nhập thành công.
        Bước   :
            1. Bấm nút menu (hamburger icon) ở góc trên trái
            2. Bấm 'Logout' trong menu điều hướng
        Kỳ vọng :
            - Hệ thống chuyển hướng về trang đăng nhập (https://www.saucedemo.com)
            - URL không còn chứa '/inventory.html'
        """
        inventory = InventoryPage(logged_in_driver)
        inventory.logout()

        login_page = LoginPage(logged_in_driver)

        assert not login_page.is_on_inventory_page(), (
            "[TC06 FAIL] Sau khi đăng xuất, URL không nên chứa '/inventory.html'."
        )
        # Kiểm tra nút Login xuất hiện → đang ở trang login
        assert "saucedemo.com" in logged_in_driver.current_url, (
            f"[TC06 FAIL] Sau khi đăng xuất phải về trang saucedemo.com. "
            f"URL hiện tại: {logged_in_driver.current_url}"
        )
