import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from locators import order_page_locators as L


class OrderPage(BasePage):
    """Page Object страницы оформления заказа. Покрывает Шаг 1, Шаг 2 и модальные окна."""

    FIELD_NAME    = L.FIELD_NAME
    FIELD_SURNAME = L.FIELD_SURNAME
    FIELD_ADDRESS = L.FIELD_ADDRESS
    FIELD_PHONE   = L.FIELD_PHONE
    FIELD_METRO   = L.FIELD_METRO
    METRO_OPTION  = L.METRO_OPTION

    BUTTON_NEXT   = L.BUTTON_NEXT

    FIELD_DATE             = L.FIELD_DATE
    DROPDOWN_PERIOD        = L.DROPDOWN_PERIOD
    DROPDOWN_PERIOD_OPTION = L.DROPDOWN_PERIOD_OPTION
    CHECKBOX_BLACK         = L.CHECKBOX_BLACK
    CHECKBOX_GREY          = L.CHECKBOX_GREY
    FIELD_COMMENT          = L.FIELD_COMMENT

    BUTTON_ORDER       = L.BUTTON_ORDER
    BUTTON_CONFIRM_YES = L.BUTTON_CONFIRM_YES

    MODAL_SUCCESS = L.MODAL_SUCCESS

    LOGO_YANDEX  = L.LOGO_YANDEX
    LOGO_SCOOTER = L.LOGO_SCOOTER

    # =========================================================================
    # Методы Шага 1
    # =========================================================================

    @allure.step("Ввести имя: {name}")
    def fill_name(self, name: str):
        self.find_clickable(self.FIELD_NAME).send_keys(name)

    @allure.step("Ввести фамилию: {surname}")
    def fill_surname(self, surname: str):
        self.find_clickable(self.FIELD_SURNAME).send_keys(surname)

    @allure.step("Ввести адрес: {address}")
    def fill_address(self, address: str):
        self.find_clickable(self.FIELD_ADDRESS).send_keys(address)

    @allure.step("Выбрать станцию метро: {station}")
    def fill_metro(self, station: str):
        self.find_clickable(self.FIELD_METRO).send_keys(station)
        option_locator = (By.XPATH, self.METRO_OPTION.format(station=station))
        self.find_visible(option_locator).click()

    @allure.step("Ввести телефон: {phone}")
    def fill_phone(self, phone: str):
        self.find_clickable(self.FIELD_PHONE).send_keys(phone)

    @allure.step("Нажать «Далее»")
    def click_next(self):
        self.find_clickable(self.BUTTON_NEXT).click()

    @allure.step("Заполнить шаг 1")
    def fill_step1(self, name, surname, address, metro, phone):
        self.fill_name(name)
        self.fill_surname(surname)
        self.fill_address(address)
        self.fill_metro(metro)
        self.fill_phone(phone)
        self.click_next()

    # =========================================================================
    # Методы Шага 2
    # =========================================================================

    @allure.step("Указать дату доставки: {date}")
    def fill_date(self, date: str):
        field = self.find_clickable(self.FIELD_DATE)
        field.click()
        field.send_keys(date)
        field.send_keys(Keys.ESCAPE)

    @allure.step("Выбрать срок аренды: {period}")
    def select_rental_period(self, period: str):
        self.find_clickable(self.DROPDOWN_PERIOD).click()
        option_locator = (By.XPATH, self.DROPDOWN_PERIOD_OPTION.format(period=period))
        self.find_clickable(option_locator).click()

    @allure.step("Выбрать цвет: {color}")
    def select_color(self, color: str):
        """color принимает 'black' или 'grey'"""
        locator = self.CHECKBOX_BLACK if color == "black" else self.CHECKBOX_GREY
        checkbox = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", checkbox)

    @allure.step("Ввести комментарий: {comment}")
    def fill_comment(self, comment: str):
        self.find_clickable(self.FIELD_COMMENT).send_keys(comment)

    @allure.step("Нажать финальную кнопку «Заказать»")
    def click_order(self):
        element = self.find_clickable(self.BUTTON_ORDER)
        self.js_click(element)

    @allure.step("Подтвердить заказ («Да»)")
    def confirm_order(self):
        if self.is_element_visible(self.BUTTON_CONFIRM_YES, timeout=8):
            element = self.find_clickable(self.BUTTON_CONFIRM_YES)
            self.js_click(element)

    @allure.step("Заполнить шаг 2")
    def fill_step2(self, date, rental_period, color, comment):
        self.fill_date(date)
        self.select_rental_period(rental_period)
        self.select_color(color)
        self.fill_comment(comment)
        self.click_order()
        self.confirm_order()

    @allure.step("Оформить заказ")
    def complete_order(self, data: dict):
        """Заполняет оба шага формы заказа целиком."""
        self.fill_step1(
            name=data["name"], surname=data["surname"],
            address=data["address"], metro=data["metro"],
            phone=data["phone"],
        )
        self.fill_step2(
            date=data["date"], rental_period=data["rental_period"],
            color=data["color"], comment=data["comment"],
        )

    # =========================================================================
    # Модальное окно успеха
    # =========================================================================

    @allure.step("Проверить появление окна «Заказ оформлен»")
    def wait_for_success_modal(self, timeout=15) -> bool:
        return self.is_element_visible(self.MODAL_SUCCESS, timeout=timeout)

    # =========================================================================
    # Логотипы
    # =========================================================================

    @allure.step("Нажать логотип Самоката")
    def click_scooter_logo(self):
        element = self.find_clickable(self.LOGO_SCOOTER)
        self.js_click(element)

    @allure.step("Нажать логотип Яндекса")
    def click_yandex_logo(self):
        element = self.find_clickable(self.LOGO_YANDEX)
        self.js_click(element)