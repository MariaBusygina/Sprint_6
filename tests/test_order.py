import allure
import pytest
from datetime import datetime, timedelta
from selenium.webdriver.support.wait import WebDriverWait

from pages.main_page import MainPage
from pages.order_page import OrderPage


def _date(days):
    return (datetime.now() + timedelta(days=days)).strftime("%d.%m.%Y")


DATASET_1 = {
    "name": "Иван", "surname": "Иванов",
    "address": "Москва, ул. Ленина, д. 1",
    "metro": "Сокол",
    "phone": "+79991234567",
    "date": _date(1), "rental_period": "двое суток",
    "color": "black", "comment": "Позвоните за час до доставки",
}

DATASET_2 = {
    "name": "Мария", "surname": "Петрова",
    "address": "Москва, пр. Мира, д. 100",
    "metro": "Комсомольская",
    "phone": "+79998765432",
    "date": _date(2), "rental_period": "трое суток",
    "color": "grey", "comment": "Домофон не работает",
}

ORDER_PARAMS = [
    pytest.param("top",    DATASET_1, id="top-button-dataset-1"),
    pytest.param("bottom", DATASET_2, id="bottom-button-dataset-2"),
]


def place_order(driver, entry_point, data):
    main = MainPage(driver)
    main.open_main_page()
    if entry_point == "top":
        main.click_order_top()
    else:
        main.click_order_bottom()
    order = OrderPage(driver)
    order.fill_step1(
        name=data["name"], surname=data["surname"],
        address=data["address"], metro=data["metro"],
        phone=data["phone"],
    )
    order.fill_step2(
        date=data["date"], rental_period=data["rental_period"],
        color=data["color"], comment=data["comment"],
    )
    return order


@allure.feature("Заказ самоката")
class TestOrder:

    @allure.title("Успешный заказ — точка входа «{entry_point}»")
    @pytest.mark.parametrize("entry_point, data", ORDER_PARAMS)
    def test_order_success_modal_appears(self, driver, entry_point, data):
        with allure.step(f"Оформить заказ через кнопку '{entry_point}'"):
            order = place_order(driver, entry_point, data)

        with allure.step("Проверить появление модального окна «Заказ оформлен»"):
            assert order.wait_for_success_modal(), \
                "Модальное окно успеха не появилось."

    @allure.title("Логотип Самоката ведёт на главную страницу")
    def test_scooter_logo_goes_to_main(self, driver):
        with allure.step("Оформить заказ"):
            order = place_order(driver, "top", DATASET_1)

        with allure.step("Дождаться модального окна"):
            assert order.wait_for_success_modal()

        with allure.step("Нажать логотип Самоката"):
            order.click_scooter_logo()

        with allure.step("Проверить URL"):
            expected = "https://qa-scooter.education-services.ru/"
            assert order.get_current_url() == expected, \
                f"Ожидался '{expected}', получен '{order.get_current_url()}'"

    @allure.title("Логотип Яндекса открывает Дзен в новом окне")
    def test_yandex_logo_opens_dzen(self, driver):
        with allure.step("Оформить заказ"):
            order = place_order(driver, "bottom", DATASET_2)

        with allure.step("Дождаться модального окна"):
            assert order.wait_for_success_modal()

        with allure.step("Нажать логотип Яндекса"):
            original_handles = set(driver.window_handles)
            order.click_yandex_logo()

        with allure.step("Переключиться на новое окно"):
            new_handle = order.wait_for_new_window(original_handles)
            assert new_handle, "Новое окно не открылось."
            driver.switch_to.window(new_handle)

        with allure.step("Проверить URL нового окна"):
            WebDriverWait(driver, 15).until(
                lambda d: any(x in d.current_url for x in ("dzen.ru", "ya.ru", "yandex.ru"))
            )
            url = driver.current_url
            assert any(x in url for x in ("dzen.ru", "ya.ru", "yandex.ru")), \
                f"Ожидался URL Яндекса/Дзена, получен: '{url}'"