import allure
import pytest
from pages.main_page import MainPage


FAQ_QUESTIONS = [
    (0, "Сколько это стоит? И как оплатить?"),
    (1, "Хочу сделать несколько самокатов! Так можно?"),
    (2, "Как рассчитывается время аренды?"),
    (3, "Можно ли заказать самокат прямо на сегодня?"),
    (4, "Можно ли продлить заказ или вернуть самокат раньше?"),
    (5, "Вы привозите зарядку вместе с самокатом?"),
    (6, "Можно ли отменить заказ?"),
    (7, "Я жду самокат, а он не приезжает. Что делать?"),
]


@allure.feature("FAQ — Вопросы о важном")
class TestFAQ:

    @allure.title("Вопрос #{n} — «{question}» — открывает ответ")
    @pytest.mark.parametrize("n, question", FAQ_QUESTIONS)
    def test_faq_answer_appears_on_click(self, driver, n, question):
        with allure.step("Открыть главную страницу"):
            page = MainPage(driver)
            page.open_main_page()

        with allure.step(f"Нажать на вопрос #{n}: «{question}»"):
            page.click_faq_question(n)

        with allure.step("Проверить, что панель с ответом открылась"):
            assert page.is_faq_panel_visible(n), \
                f"Панель accordion__panel-{n} не стала видимой после клика."