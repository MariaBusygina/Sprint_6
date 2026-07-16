from selenium.webdriver.common.by import By

LOGO_YANDEX         = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
LOGO_SCOOTER        = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
ORDER_BUTTON_TOP    = (By.XPATH, '//button[@class="Button_Button__ra12g"]')
ORDER_BUTTON_BOTTOM = (By.XPATH, '//div[contains(@class,"Home_FinishButton")]//button')