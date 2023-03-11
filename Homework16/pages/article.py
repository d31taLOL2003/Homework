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
        self.scroll_to_element((By.XPATH, f"//h2[text()='{title}']"))
        return self.driver.title
