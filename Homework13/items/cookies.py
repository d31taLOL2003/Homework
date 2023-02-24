from items.item import Item


class Cookies(Item):
    """
    A class representing Cookies in a shop, inheriting from the Item class.

    Attributes:
        __name (str): The name of the cookies.
        __price (float): The price of the cookies per kilogram.

    Methods:
        get_name: Returns the name of the cookies.
        get_price: Returns the price of the cookies per kilogram.
    """
    def __init__(self, name='Cookies', price=100.0):
        """
        Initializes a new instance of the Cookies class.

        Args:
            name (str): The name of the cookies. Default is 'Cookies'.
            price (float): The price of the cookies per kilogram. Default is 100.0.

        Returns:
            None
        """
        self.__name = name
        self.__price = price

    
    def get_name(self):
        """
        Returns the name of the cookies.

        Args:
            None

        Returns:
            str: The name of the cookies.
        """
        return self.__name

    def get_price(self):
        """
        Returns the price of the cookies per kilogram.

        Args:
            None

        Returns:
            str: The price of the cookies per kilogram, in the format "{price} hryvnias per kilo".
        """
        return f"{self.__price} hryvnias per kilo"
