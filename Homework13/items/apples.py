from items.item import Item


class Apples(Item):
    """
    A class representing Apples in a shop, inheriting from the Item class.

    Attributes:
        __name (str): The name of the apples.
        __price (float): The price of the apples per kilogram.

    Methods:
        get_name: Returns the name of the apples.
        get_price: Returns the price of the apples per kilogram.
    """
    def __init__(self, name: str = 'Apples', price: float = 14.0) -> None:
        """
        Initializes a new instance of the Apples class.

        Args:
            name (str): The name of the apples. Default is 'Apples'.
            price (float): The price of the apples per kilogram. Default is 14.0.

        Returns:
            None
        """
        self.__name = name
        self.__price = price

    
    def get_name(self):
        """
        Returns the name of the apples.

        Args:
            None

        Returns:
            str: The name of the apples.
        """
        return self.__name

    def get_price(self):
        """
        Returns the price of the apples per kilogram.

        Args:
            None

        Returns:
            str: The price of the apples per kilogram, in the format "{price} hryvnias per kilo".
        """
        return f"{self.__price} hryvnias per kilo"
