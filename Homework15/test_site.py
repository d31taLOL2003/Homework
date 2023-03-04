from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def test_input() -> None:
    """
    The function of testing the search text box on "dou.ua" website using Chrome browser.
    """
    driver = Chrome("drivers/chromedriver.exe")
    driver.maximize_window()
    web_driver_wait = WebDriverWait(driver, 10)
    driver.get("https://dou.ua/")
    search_locator = "//input[@placeholder='пошук']"
    search_input = web_driver_wait.until(EC.presence_of_element_located((By.XPATH, search_locator)))
    search_input.send_keys("Python")
    web_driver_wait.until(EC.text_to_be_present_in_element_value((By.XPATH, search_locator), "Python"))
    driver.quit()


def test_click() -> None:
    """
    The function of testing the "Work" button on the "dou.ua" website using the Chrome browser.
    """
    driver = Chrome("drivers/chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://dou.ua/")
    search_locator = "//a[@href='https://jobs.dou.ua/']"
    search_click: WebElement = driver.find_element(By.XPATH, search_locator)
    search_click.click()
    driver.quit()


def test_scroll() -> None:
    """
    The function of testing the scroll functionality on "dou.ua" website using Chrome browser.
    """
    driver = Chrome("drivers/chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://dou.ua/")
    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.END)
    driver.quit()
