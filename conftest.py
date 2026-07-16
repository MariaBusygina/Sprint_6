import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="function")
def driver():
    """Запускает браузер Firefox перед каждым тестом и закрывает после."""
    options = Options()
    # Раскомментируй строку ниже для запуска без GUI (на сервере/CI):
    # options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()