"""
conftest.py – Cấu hình fixtures dùng chung cho toàn bộ test suite.
Website kiểm thử: https://www.saucedemo.com  (demo e-commerce)
"""

from pathlib import Path
import sys
from datetime import datetime
import re

# Ensure project root is on sys.path so `from pages...` imports work under pytest.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.saucedemo.com"
VALID_USER = "standard_user"
VALID_PASS = "secret_sauce"
SCREENSHOT_DIR = PROJECT_ROOT / "reports" / "screenshots"


@pytest.fixture(scope="function")
def driver():
    """Khởi tạo Chrome WebDriver trước mỗi test, đóng sau khi xong."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")          # chạy không cần giao diện
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,800")

    driver_path = Path(ChromeDriverManager().install())
    # webdriver-manager hiện tại có thể trả về nhầm file (ví dụ `THIRD_PARTY_NOTICES.chromedriver`)
    # trong khi `chromedriver.exe` vẫn tồn tại trong cùng thư mục.
    if driver_path.name.lower() != "chromedriver.exe":
        candidate = driver_path.parent / "chromedriver.exe"
        if candidate.exists():
            driver_path = candidate

    service = Service(str(driver_path))
    drv = webdriver.Chrome(service=service, options=options)
    drv.implicitly_wait(10)
    yield drv
    drv.quit()


@pytest.fixture(scope="function")
def logged_in_driver(driver):
    """Fixture đã đăng nhập sẵn – dùng cho các test cần pre-condition đăng nhập."""
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys(VALID_USER)
    driver.find_element(By.ID, "password").send_keys(VALID_PASS)
    driver.find_element(By.ID, "login-button").click()
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Tự động chụp ảnh khi test thất bại ở phase `call`.
    Ảnh được lưu tại: reports/screenshots/
    """
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or report.passed:
        return

    drv = item.funcargs.get("driver") or item.funcargs.get("logged_in_driver")
    if drv is None:
        return

    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    test_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", item.nodeid)
    screenshot_path = SCREENSHOT_DIR / f"{test_name}_{timestamp}.png"
    drv.save_screenshot(str(screenshot_path))
