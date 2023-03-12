import pytest
from time import sleep
from selenium.webdriver import Chrome
from pages.main_page import MainPage


@pytest.fixture()
def driver() -> Chrome:
    """
    Fixture to initialize and close a Chrome webdriver.

    Returns:
        Chrome: A Chrome webdriver instance.
    """
    driver = Chrome("drivers/chromedriver.exe")
    driver.maximize_window()
    driver.get("https://dou.ua/")
    yield driver
    sleep(5) # sleep використав, тільки для того, щоб побачити результат виконання тесту на сторінці
    driver.quit()


@pytest.fixture()
def main_page(driver) -> MainPage:
    """
    Fixture to initialize a MainPage instance.
    
    Args:
        driver: The Chrome webdriver instance.

    Returns:
        MainPage: An instance of the MainPage class.
    """
    yield MainPage(driver)
