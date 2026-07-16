import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators import main_page_locators as L


class MainPage(BasePage):
    """Page Object главной страницы."""

    LOGO_YANDEX         = L.LOGO_YANDEX
    LOGO_SCOOTER        = L.LOGO_SCOOTER
    ORDER_BUTTON_TOP    = L.ORDER_BUTTON_TOP
    ORDER_BUTTON_BOTTOM = L.ORDER_BUTTON_BOTTOM

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open()
        self.accept_cookies()

    @allure.step("Нажать на вопрос FAQ #{n}")
    def click_faq_question(self, n: int):
        locator = (By.ID, f"accordion__heading-{n}")
        element = self.find_element(locator)
        self.scroll_to(element)
        self.js_click(element)

    def is_faq_panel_visible(self, n: int) -> bool:
        locator = (By.ID, f"accordion__panel-{n}")
        return self.is_element_visible(locator)

    @allure.step("Нажать кнопку «Заказать» вверху страницы")
    def click_order_top(self):
        self.find_clickable(self.ORDER_BUTTON_TOP).click()

    @allure.step("Нажать кнопку «Заказать» внизу страницы")
    def click_order_bottom(self):
        element = self.find_element(self.ORDER_BUTTON_BOTTOM)
        self.scroll_to(element)
        self.js_click(element)

    @allure.step("Перейти к форме заказа через кнопку «{entry_point}»")
    def go_to_order(self, entry_point: str):
        """Нажимает нужную кнопку «Заказать» в зависимости от точки входа."""
        if entry_point == "top":
            self.click_order_top()
        else:
            self.click_order_bottom()

    @allure.step("Нажать логотип Самоката")
    def click_scooter_logo(self):
        self.find_clickable(self.LOGO_SCOOTER).click()

    @allure.step("Нажать логотип Яндекса")
    def click_yandex_logo(self):
        self.find_clickable(self.LOGO_YANDEX).click()