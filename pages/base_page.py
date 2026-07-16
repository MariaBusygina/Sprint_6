import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    BASE_URL = "https://qa-scooter.education-services.ru"

    # Кнопка «да все привыкли» в баннере куки
    # <button id="rcc-confirm-button" class="App_CookieButton__3cvqF ...">да все привыкли</button>
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    def __init__(self, driver):
        self.driver = driver

    def open(self, path=""):
        self.driver.get(f"{self.BASE_URL}{path}")

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

    def wait_for_new_window(self, original_handles, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.number_of_windows_to_be(len(original_handles) + 1)
        )
        for handle in self.driver.window_handles:
            if handle not in original_handles:
                return handle