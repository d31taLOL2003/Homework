from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        """
        Initializes an instance of BasePage class.
        
        Args:
            driver: A web driver instance to control the browser.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def wait_for_element(self, locator):
        """
        Waiting for the element to appear on the page.
        
        Args:
            locator: A tuple containing the locator type and element locator.

        Returns:
            Returns the found element.
        """
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element

    def click_for_element(self, locator):
        """
        Clicks on an item on the page.
        
        Args:
            locator: A tuple containing the locator type and element locator.

        Returns:
            It doesn't return anything.
        """
        element = self.wait_for_element(locator)
        element.click()

    def check_clickable_element(self, locator):
        """
        Checks if the specified element is clickable within a certain time frame.
        
        Args:
            locator: A tuple containing the locator type and element locator.

        Returns:
            The clickable WebElement if it is found.
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        return element

    def scroll_to_element(self, locator):
        """
        Scrolls the page to the item.
        
        Args:
            locator: A tuple containing the locator type and element locator.

        Returns:
            Returns the coordinates of the element.
        """
        element = self.wait_for_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop - 200)")
        location = element.location_once_scrolled_into_view
        return location
