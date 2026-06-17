"""
tests/test_cart.py

TC04 – Thêm sản phẩm vào giỏ hàng
TC05 – Xóa sản phẩm khỏi giỏ hàng
"""

import pytest
from pages.inventory_page import InventoryPage


class TestCart:

    # ──────────────────────────────────────────────
    # TC04: Thêm sản phẩm vào giỏ hàng
    # ──────────────────────────────────────────────
    def test_TC04_add_product_to_cart(self, logged_in_driver):
        """
        Mô tả  : Kiểm tra chức năng thêm sản phẩm vào giỏ hàng.
        Pre-condition : Người dùng đã đăng nhập thành công.
        Bước   :
            1. Trên trang danh sách sản phẩm, bấm nút 'Add to cart'
               của sản phẩm đầu tiên
        Kỳ vọng : Badge số lượng trên icon giỏ hàng hiển thị giá trị = 1
        """
        page = InventoryPage(logged_in_driver)
        page.add_first_item_to_cart()

        cart_count = page.get_cart_count()
        assert cart_count == 1, (
            f"[TC04 FAIL] Số lượng trong giỏ hàng phải là 1, nhưng thực tế là: {cart_count}"
        )
        assert page.is_cart_badge_visible(), (
            "[TC04 FAIL] Badge giỏ hàng phải hiển thị sau khi thêm sản phẩm."
        )

    # ──────────────────────────────────────────────
    # TC05: Xóa sản phẩm khỏi giỏ hàng
    # ──────────────────────────────────────────────
    def test_TC05_remove_product_from_cart(self, logged_in_driver):
        """
        Mô tả  : Kiểm tra chức năng xóa sản phẩm khỏi giỏ hàng.
        Pre-condition : Người dùng đã đăng nhập và đã thêm 1 sản phẩm vào giỏ.
        Bước   :
            1. Thêm sản phẩm đầu tiên vào giỏ hàng
            2. Bấm nút 'Remove' để xóa sản phẩm
        Kỳ vọng : Badge số lượng trên icon giỏ hàng biến mất (không hiển thị)
        """
        page = InventoryPage(logged_in_driver)

        # Thêm vào giỏ trước
        page.add_first_item_to_cart()
        assert page.get_cart_count() == 1, "Pre-condition: chưa thêm được sản phẩm vào giỏ"

        # Xóa khỏi giỏ
        page.remove_first_item_from_cart()

        assert not page.is_cart_badge_visible(), (
            "[TC05 FAIL] Badge giỏ hàng phải biến mất sau khi xóa toàn bộ sản phẩm."
        )
        assert page.get_cart_count() == 0, (
            f"[TC05 FAIL] Số lượng trong giỏ hàng phải là 0, nhưng là: {page.get_cart_count()}"
        )
