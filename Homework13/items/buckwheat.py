from items.item import Item


class Buckwheat(Item):
    """
    A class representing Buckwheat in a shop, inheriting from the Item class.

    Attributes:
        __name (str): The name of the buckwheat.
        __price (float): The price of the buckwheat per kilogram.

    Methods:
        get_name: Returns the name of the buckwheat.
        get_price: Returns the price of the buckwheat per kilogram.
    """
    def __init__(self, name='Buckwheat', price=80.7):
        """
        Initializes a new instance of the Buckwheat class.

        Args:
            name (str): The name of the buckwheat. Default is 'Buckwheat'.
            price (float): The price of the buckwheat per kilogram. Default is 80.7.

        Returns:
            None
        """
        self.__name = name
        self.__price = price

    
    def get_name(self):
        """
        Returns the name of the buckwheat.

        Args:
            None

        Returns:
            str: The name of the buckwheat.
        """
        return self.__name

    def get_price(self):
        """
        Returns the price of the buckwheat per kilogram.

        Args:
            None

        Returns:
            str: The price of the buckwheat per kilogram, in the format "{price} hryvnias per kilo".
        """
        return f"{self.__price} hryvnias per kilo"
