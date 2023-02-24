from items.buckwheat import Buckwheat
from items.cookies import Cookies
from items.apples import Apples
from singleton_shop import singleton_shop
from typing import Union


@singleton_shop
class Shop:
    """
    Represents a shop that sells various items.

    Attributes:
        None

    Methods:
        get_item: Returns an item by name.
    """

    @staticmethod
    def get_item(name: str) -> Union[Buckwheat, Cookies, Apples]:
        """
        Returns an item by name.

        Args:
            name (str): The name of the item to get.

        Returns:
            Union[Buckwheat, Cookies, Apples]: The item object.

        Raises:
            Exception: If the item with the given name is not found.
        """
        if name == "buckwheat":
            return Buckwheat()
        elif name == "cookies":
            return Cookies()
        elif name == "apples":
            return Apples()
        else:
            raise Exception("Sorry, we don't have this product")
