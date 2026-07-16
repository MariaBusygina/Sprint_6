import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    """
    Page Object главной страницы.

    Реальные локаторы получены из DevTools сайта qa-scooter.education-services.ru
    """

    # --- Логотипы ---
    # <a class="Header_LogoYandex__3TSOI" href="//ya.ru"><img alt="Yandex"></a>
    # <a class="Header_LogoScooter__3lsAR" href="/"><img alt="Scooter"></a>
    LOGO_YANDEX  = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")

    # --- Кнопки «Заказать» ---
    # Верхняя: единственная кнопка с классом Button_Button__ra12g (без Button_Middle)
    # <button class="Button_Button__ra12g">Заказать</button>  — в Header_Nav
    ORDER_BUTTON_TOP = (By.XPATH, '//button[@class="Button_Button__ra12g"]')

    # Нижняя: обёрнута в div class="Home_FinishButton__1cWm"
    # <div class="Home_FinishButton__1cWm"><button class="Button_Button__ra12g Button_Middle__1CSJM">Заказать</button>
    ORDER_BUTTON_BOTTOM = (By.XPATH, '//div[contains(@class,"Home_FinishButton")]//button')

    # --- FAQ ---
    # Заголовок: <div id="accordion__heading-N" role="button" class="accordion__button">
    # Панель:    <div id="accordion__panel-N"   class="accordion__panel">

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

    @allure.step("Нажать логотип Самоката")
    def click_scooter_logo(self):
        self.find_clickable(self.LOGO_SCOOTER).click()

    @allure.step("Нажать логотип Яндекса")
    def click_yandex_logo(self):
        self.find_clickable(self.LOGO_YANDEX).click()

    def get_current_url(self):
        return self.driver.current_url