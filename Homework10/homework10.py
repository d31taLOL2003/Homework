from abc import ABC, abstractmethod


class Gadget(ABC):
    """
    Class Gadget this is an abstraction of the gadget itself, 
    it contains parameters to describe the gadget. This class is also abstract.
    """
    def __init__(self, manufacturer, model, os, screen_size, memory):
        """
        In this method we store the parameters of our gadget
        """
        self.__manufacturer = manufacturer
        self.__model = model
        self.__os = os
        self.__screen_size = screen_size
        self.__memory = memory

    def get_manufacturer(self):
        """
        This method return Manufactures
        """
        return self.__manufacturer

    def get_model(self):
        """
        This method return Model
        """
        return self.__model

    def get_os(self):
        """
        This method return Operating System
        """
        return self.__os

    def get_screen_size(self):
        """
        This method return size of the screen
        """
        return self.__screen_size

    def get_memory(self):
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


class Apple(Gadget):
    """
    Class Apple inherits class Gadget. Here in 'def __init__' we write the same parameters 
    of the Gadget class and apply the super function.
    We also make sure to write our 'unlocking' method, which is an abstract method of the Gadget class, 
    and the Apple class inherits it.
    """
    def __init__(self, manufacturer, model, os, screen_size, memory):
        super().__init__(manufacturer, model, os, screen_size, memory)

    def unlocking(self):
        """
        Method unlocking returns string how to unlock the phone. Here we get "Need a fingerprint"
        """
        return "Need a fingerprint"


class Samsung(Gadget):
    """
    In class Samsung everything happens in the same way as in the Apple class
    """
    def __init__(self, manufacturer, model, os, screen_size, memory):
        super().__init__(manufacturer, model, os, screen_size, memory)

    def unlocking(self):
        """
         Method unlocking returns string how to unlock the phone. Here we get "Write a password"
        """
        return "Write a password"
