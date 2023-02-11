from abc import ABC, abstractmethod


class Gadget(ABC):
    """
    Class Gadget this is an abstraction of the gadget itself, 
    it contains parameters to describe the gadget. This class is also abstract.
    """
    def __init__(self, manufacturer: str, model: str, os: str, screen_size: str, memory: int):
        """
        In this method we store the parameters of our gadget
        """
        self.__manufacturer = manufacturer
        self.__model = model
        self.__os = os
        self.__screen_size = screen_size
        self.__memory = memory

    def get_manufacturer(self) -> str:
        """
        This method return Manufactures
        """
        return self.__manufacturer

    def get_model(self) -> str:
        """
        This method return Model
        """
        return self.__model

    def get_os(self) -> str:
        """
        This method return Operating System
        """
        return self.__os

    def get_screen_size(self) -> str:
        """
        This method return size of the screen
        """
        return self.__screen_size

    def get_memory(self) -> str:
        """
        This method returns the amount of memory in the phone
        """
        return self.__memory

    @abstractmethod
    def unlocking(self):
        """
        The unlocking method is an abstract method in the Gadget class.
        Gadget is an abstract base class, any class that inherits from it must implement the unlocking method. 
        This ensures that every subclass of Gadget provides a specific implementation of the unlocking method.
        """
        pass
