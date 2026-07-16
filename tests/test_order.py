"""
Тесты позитивного сценария заказа самоката.

Проверяемые точки:
  1. Кнопка «Заказать» вверху страницы.
  2. Кнопка «Заказать» внизу страницы.
  3. Успешное появление модального окна «Заказ оформлен».
  4. Логотип Самоката → главная страница Самоката.
  5. Логотип Яндекса → новое окно с редиректом на Дзен.
"""

import allure
import pytest

from config import BASE_URL
from helpers import get_date
from pages.main_page import MainPage
from pages.order_page import OrderPage


# ---------------------------------------------------------------------------
# Тестовые данные
# ---------------------------------------------------------------------------

DATASET_1 = {
    "name": "Иван", "surname": "Иванов",
    "address": "Москва, ул. Ленина, д. 1",
    "metro": "Сокол",
    "phone": "+79991234567",
    "date": get_date(1), "rental_period": "двое суток",
    "color": "black", "comment": "Позвоните за час до доставки",
}

DATASET_2 = {
    "name": "Мария", "surname": "Петрова",
    "address": "Москва, пр. Мира, д. 100",
    "metro": "Комсомольская",
    "phone": "+79998765432",
    "date": get_date(2), "rental_period": "трое суток",
    "color": "grey", "comment": "Домофон не работает",
}

ORDER_PARAMS = [
    pytest.param("top",    DATASET_1, id="top-button-dataset-1"),
    pytest.param("bottom", DATASET_2, id="bottom-button-dataset-2"),
]


# ---------------------------------------------------------------------------
# Тесты
# ---------------------------------------------------------------------------

@allure.feature("Заказ самоката")
class TestOrder:

    @allure.title("Успешный заказ — точка входа «{entry_point}»")
    @pytest.mark.parametrize("entry_point, data", ORDER_PARAMS)
    def test_order_success_modal_appears(self, driver, entry_point, data):
        """
        Проверяет, что после заполнения формы появляется
        модальное окно «Заказ оформлен».
        """
        main = MainPage(driver)
        main.open_main_page()
        main.go_to_order(entry_point)

        order = OrderPage(driver)
        order.complete_order(data)

        assert order.wait_for_success_modal(), \
            "Модальное окно успеха не появилось после оформления заказа."

    @allure.title("Логотип Самоката ведёт на главную страницу")
    def test_scooter_logo_goes_to_main(self, driver):
        """
        После успешного заказа клик по логотипу Самоката
        переводит на главную страницу сервиса.
        """
        main = MainPage(driver)
        main.open_main_page()
        main.go_to_order("top")

        order = OrderPage(driver)
        order.complete_order(DATASET_1)

        assert order.wait_for_success_modal(), \
            "Модальное окно успеха не появилось."

        order.click_scooter_logo()

        expected = BASE_URL + "/"
        assert order.get_current_url() == expected, \
            f"Ожидался '{expected}', получен '{order.get_current_url()}'"

    @allure.title("Логотип Яндекса открывает Дзен в новом окне")
    def test_yandex_logo_opens_dzen(self, driver):
        """
        После успешного заказа клик по логотипу Яндекса
        открывает в новом окне главную страницу Дзена (ya.ru → dzen.ru).
        """
        main = MainPage(driver)
        main.open_main_page()
        main.go_to_order("bottom")

        order = OrderPage(driver)
        order.complete_order(DATASET_2)

        assert order.wait_for_success_modal(), \
            "Модальное окно успеха не появилось."

        original_handles = order.get_window_handles()
        order.click_yandex_logo()

        new_handle = order.wait_for_new_window(original_handles)
        assert new_handle, "Новое окно не открылось после клика по логотипу Яндекса."

        order.switch_to_window(new_handle)
        order.wait_for_url_contains(["dzen.ru", "ya.ru", "yandex.ru"])

        url = order.get_current_url()
        assert any(d in url for d in ("dzen.ru", "ya.ru", "yandex.ru")), \
            f"Ожидался URL Яндекса/Дзена, получен: '{url}'"