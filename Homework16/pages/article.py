from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Article(BasePage):
    def __init__(self, driver):
        """
        Initializes an instance of the Article class.

        Args:
            driver: an instance of the Selenium WebDriver class.

        Returns:
            None
        """
        super().__init__(driver)

    def scroll_to_title(self, title):
        """
        Scrolls to the specified title.

        Args:
            title: the title to scroll to.
            
        Returns:
            str: the title of the page after scrolling.
        """
        locator = (By.XPATH, f"//h2[text()='{title}']")
        self.scroll_to_element(locator)
        return self.driver.find_element(*locator)

    def click_button(self, button):
        """
        Clicks the specified button on the salary chart.

        Args:
            button: The label of the button to be clicked.

        Returns:
            WebElement: The clicked button element.
        """
        locator = (By.XPATH, f"//div[@class='chart-salary']//span[text()='{button}']")
        self.check_clickable_element(locator)
        self.click_for_element(locator)
        return self.driver.find_element(*locator)
