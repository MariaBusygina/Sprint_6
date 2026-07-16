import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class OrderPage(BasePage):
    """
    Page Object страницы оформления заказа.
    Покрывает Шаг 1, Шаг 2 и модальные окна.

    Реальные локаторы получены из DevTools сайта qa-scooter.education-services.ru
    """

    # -------------------------------------------------------------------------
    # Шаг 1 — «Для кого самокат»
    # -------------------------------------------------------------------------
    # <input placeholder="* Имя" class="Input_Input__1iN_Z Input_Responsible__1jDKN">
    FIELD_NAME    = (By.XPATH, '//input[@placeholder="* Имя"]')
    FIELD_SURNAME = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    FIELD_ADDRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    FIELD_PHONE   = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')

    # <input class="select-search__input" placeholder="* Станция метро">
    FIELD_METRO   = (By.CLASS_NAME, "select-search__input")

    # Вариант в выпадающем списке метро:
    # <button class="Order_SelectOption__82bhS select-search__option">
    #   <div class="Order_Text__2broi">Сокол</div>
    # </button>
    # Клик по кнопке-варианту, внутри которой текст совпадает со станцией
    METRO_OPTION  = '//button[contains(@class,"select-search__option")]' \
                    '//div[contains(@class,"Order_Text") and text()="{station}"]'

    # <button class="Button_Button__ra12g Button_Middle__1CSJM">Далее</button>
    BUTTON_NEXT   = (By.XPATH, '//button[text()="Далее"]')

    # -------------------------------------------------------------------------
    # Шаг 2 — «Про аренду»
    # -------------------------------------------------------------------------
    # <input placeholder="* Когда привезти самокат" class="...react-datepicker-ignore-onclickoutside">
    FIELD_DATE    = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')

    # Дропдаун срока аренды:
    # <div class="Dropdown-control">...</div>
    # <div class="Dropdown-option">двое суток</div>
    DROPDOWN_PERIOD        = (By.CLASS_NAME, "Dropdown-control")
    DROPDOWN_PERIOD_OPTION = '//div[@class="Dropdown-option" and text()="{period}"]'

    # Чекбоксы цвета:
    # <input id="black" class="Checkbox_Input__14A2w" type="checkbox">
    # <input id="grey"  class="Checkbox_Input__14A2w" type="checkbox">
    CHECKBOX_BLACK = (By.ID, "black")
    CHECKBOX_GREY  = (By.ID, "grey")

    # <input placeholder="Комментарий для курьера" class="Input_Input__1iN_Z Input_Responsible__1jDKN">
    FIELD_COMMENT  = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')

    # Финальная кнопка «Заказать» на шаге 2
    # <button class="Button_Button__ra12g Button_Middle__1CSJM">Заказать</button>
    # На странице есть ещё одна кнопка «Заказать» в шапке (без Button_Middle),
    # поэтому уточняем по классу Button_Middle__1CSJM
    BUTTON_ORDER   = (By.XPATH, '//button[contains(@class,"Button_Middle__1CSJM") and text()="Заказать"]')

    # -------------------------------------------------------------------------
    # Диалог подтверждения заказа («Хотите оформить заказ?»)
    # -------------------------------------------------------------------------
    # <button class="Button_Button__ra12g Button_Middle__1CSJM">Да</button>
    BUTTON_CONFIRM_YES = (By.XPATH, '//button[text()="Да"]')

    # -------------------------------------------------------------------------
    # Модальное окно успеха
    # -------------------------------------------------------------------------
    # <div class="Order_ModalHeader__3FDaJ">Заказ оформлен...</div>
    MODAL_SUCCESS = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    # Логотипы (те же что на главной, доступны со страницы заказа)
    LOGO_YANDEX  = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")

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
        # Чекбоксы стилизованы, кликаем через JS чтобы гарантировать срабатывание
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
        # Оверлей модального окна перекрывает логотип — используем js_click
        element = self.find_clickable(self.LOGO_SCOOTER)
        self.js_click(element)

    @allure.step("Нажать логотип Яндекса")
    def click_yandex_logo(self):
        # Оверлей модального окна перекрывает логотип — используем js_click
        element = self.find_clickable(self.LOGO_YANDEX)
        self.js_click(element)

    def get_current_url(self):
        return self.driver.current_url