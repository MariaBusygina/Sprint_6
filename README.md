# Sprint_6
Проект автоматизированного тестирования сервиса qa-scooter.education-services.ru.
Sprint_6/
├── locators/
│   ├── __init__.py
│   ├── main_page_locators.py   # Локаторы главной страницы
│   └── order_page_locators.py  # Локаторы страницы заказа
├── pages/
│   ├── base_page.py      # Базовый класс с общими методами
│   ├── main_page.py      # Page Object главной страницы
│   └── order_page.py     # Page Object страницы заказа
├── tests/
│   ├── test_faq.py       # Тесты раздела «Вопросы о важном»
│   └── test_order.py     # Тесты оформления заказа
├── config.py             # URL сервиса
├── helpers.py            # Вспомогательные функции
├── conftest.py           # Фикстура драйвера Firefox
├── pytest.ini            # Конфигурация pytest
└── requirements.txt      # Зависимости

Установка
pip3 install -r requirements.txt
Запуск тестов
python3 -m pytest tests/ -v
Открыть отчёт в браузере
allure serve allure-results
