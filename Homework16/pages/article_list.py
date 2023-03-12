from selenium.webdriver.common.by import By
from pages.article import Article
from pages.base_page import BasePage


class ArticleList(BasePage):
    def __init__(self, drive):
        """
        The class constructor.

        Args:
            drive: WebDriver object which controls the browser.
        """
        super().__init__(drive)
        self.__article_locator = (By.XPATH, "//a[@href='https://dou.ua/lenta/articles/salary-report-qa-winter-2023/']")

    def choose_article(self):
        """
        Clicks on the link to the chosen article.

        Returns:
            An instance of the Article class, which is used to interact with the article page.
        """
        self.click_for_element(self.__article_locator)
        return Article(self.driver)
