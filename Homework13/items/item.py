from abc import ABC, abstractmethod


class Item(ABC):
    """
    Abstract base class for representing an item in a shop.

    Attributes:
        None

    Methods:
        get_name: Returns the name of the item.
        get_price: Returns the price of the item.
    """
    @abstractmethod
    def get_name(self) -> str:
        """
        Returns the name of the item.

        Args:
            None

        Returns:
            str: The name of the item.
        """
        pass


    @abstractmethod
    def get_price(self) -> float:
        """
        Returns the price of the item.

        Args:
            None

        Returns:
            float: The price of the item.
        """
        pass
