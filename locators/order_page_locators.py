from selenium.webdriver.common.by import By

FIELD_NAME    = (By.XPATH, '//input[@placeholder="* Имя"]')
FIELD_SURNAME = (By.XPATH, '//input[@placeholder="* Фамилия"]')
FIELD_ADDRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
FIELD_PHONE   = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
FIELD_METRO   = (By.CLASS_NAME, "select-search__input")
METRO_OPTION  = ('//button[contains(@class,"select-search__option")]'
                 '//div[contains(@class,"Order_Text") and text()="{station}"]')

BUTTON_NEXT   = (By.XPATH, '//button[text()="Далее"]')

FIELD_DATE             = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
DROPDOWN_PERIOD        = (By.CLASS_NAME, "Dropdown-control")
DROPDOWN_PERIOD_OPTION = '//div[@class="Dropdown-option" and text()="{period}"]'
CHECKBOX_BLACK         = (By.ID, "black")
CHECKBOX_GREY          = (By.ID, "grey")
FIELD_COMMENT          = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')

BUTTON_ORDER       = (By.XPATH, '//button[contains(@class,"Button_Middle__1CSJM") and text()="Заказать"]')
BUTTON_CONFIRM_YES = (By.XPATH, '//button[text()="Да"]')

MODAL_SUCCESS = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

LOGO_YANDEX  = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")