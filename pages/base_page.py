import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from config import BASE_URL


class BasePage:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    def __init__(self, driver):
        self.driver = driver

    def open(self, path=""):
        self.driver.get(f"{BASE_URL}{path}")

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def find_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def accept_cookies(self):
        """Закрывает баннер куки, если он есть."""
        try:
            btn = WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable(self.COOKIE_BUTTON)
            )
            btn.click()
        except TimeoutException:
            pass

    def is_element_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def get_current_url(self) -> str:
        return self.driver.current_url

    def get_window_handles(self) -> set:
        return set(self.driver.window_handles)

    def switch_to_window(self, handle: str):
        self.driver.switch_to.window(handle)

    def wait_for_new_window(self, original_handles, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.number_of_windows_to_be(len(original_handles) + 1)
        )
        for handle in self.driver.window_handles:
            if handle not in original_handles:
                return handle

    def wait_for_url_contains(self, domains: list, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda d: any(domain in d.current_url for domain in domains)
        )