from selenium.webdriver.common.by import By
from pages.article_list import ArticleList
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        """
        Constructs a MainPage instance.

        Args:
            driver: A web driver instance.
        """
        super().__init__(driver)

    def choose_category(self, name):
        """
         Clicks on a category.

        Args:
            name: A string with the name of the category to click.

        Returns:
            None.
        """
        category_locator = (By.XPATH, f"//a[text()='{name}']")
        self.click_for_element(category_locator)

    def choose_sub_category(self, name):
        """
        Clicks on a subcategory.

        Args:
            name: A string with the name of the subcategory to click.

        Returns:
            An ArticleList object that represents the list of articles of the subcategory.
        """
        sub_category_locator = (By.XPATH, f"//a[text()='{name}']")
        self.click_for_element(sub_category_locator)
        return ArticleList(self.driver)
