"""
pages/inventory_page.py – Page Object Model cho trang danh sách sản phẩm.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    # Locators
    CART_BADGE           = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK            = (By.CLASS_NAME, "shopping_cart_link")
    MENU_BUTTON          = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK          = (By.ID, "logout_sidebar_link")
    FIRST_ADD_BTN        = (By.XPATH, "(//button[contains(@class,'btn_inventory')])[1]")
    FIRST_REMOVE_BTN     = (By.XPATH, "(//button[contains(text(),'Remove')])[1]")
    ITEM_NAMES           = (By.CLASS_NAME, "inventory_item_name")
    SORT_DROPDOWN        = (By.CLASS_NAME, "product_sort_container")
    LOGIN_USERNAME_INPUT = (By.ID, "user-name")
    LOGIN_URL = "https://www.saucedemo.com"

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, 10)

    def add_first_item_to_cart(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.FIRST_ADD_BTN))
        btn.click()
        return self

    def remove_first_item_from_cart(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.FIRST_REMOVE_BTN))
        btn.click()
        return self

    def get_cart_count(self) -> int:
        try:
            badge = self.driver.find_element(*self.CART_BADGE)
            return int(badge.text)
        except Exception:
            return 0

    def is_cart_badge_visible(self) -> bool:
        try:
            self.driver.find_element(*self.CART_BADGE)
            return True
        except Exception:
            return False

    def logout(self):
        # Đợi menu mở rồi bấm logout.
        self.wait.until(EC.element_to_be_clickable(self.MENU_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK)).click()
        # Sau khi logout, Saucedemo có thể không redirect ngay lập tức.
        # Ép điều hướng về trang login để kiểm tra trạng thái đăng xuất ổn định hơn.
        self.driver.get(self.LOGIN_URL)
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_USERNAME_INPUT))
        return self

    def get_item_names(self) -> list:
        return [el.text for el in self.driver.find_elements(*self.ITEM_NAMES)]
