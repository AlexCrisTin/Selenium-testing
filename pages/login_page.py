"""
pages/login_page.py – Page Object Model cho trang đăng nhập.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://www.saucedemo.com"

    # Locators
    USERNAME_INPUT  = (By.ID, "user-name")
    PASSWORD_INPUT  = (By.ID, "password")
    LOGIN_BUTTON    = (By.ID, "login-button")
    ERROR_MESSAGE   = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
        return self

    def enter_username(self, username: str):
        self.driver.find_element(*self.USERNAME_INPUT).clear()
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        return self

    def enter_password(self, password: str):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        return self

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return self

    def login(self, username: str, password: str):
        """Shortcut: nhập thông tin và bấm đăng nhập."""
        return self.enter_username(username).enter_password(password).click_login()

    def get_error_message(self) -> str:
        el = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return el.text

    def is_on_inventory_page(self) -> bool:
        return "/inventory.html" in self.driver.current_url
