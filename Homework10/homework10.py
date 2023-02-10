from abc import ABC, abstractmethod


class Gadget(ABC):
    def __init__(self, manufacturer, model, os, screen_size, memory):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__os = os
        self.__screen_size = screen_size
        self.__memory = memory

    def get_manufacturer(self):
        return self.__manufacturer

    def get_model(self):
        return self.__model

    def get_os(self):
        return self.__os

    def get_screen_size(self):
        return self.__screen_size

    def get_memory(self):
        return self.__memory

    @abstractmethod
    def unlocking(self):
        pass


class Apple(Gadget):
    def __init__(self, manufacturer, model, os, screen_size, memory):
        super().__init__(manufacturer, model, os, screen_size, memory)

    def unlocking(self):
        return "Need a fingerprint"


class Samsung(Gadget):
    def __init__(self, manufacturer, model, os, screen_size, memory):
        super().__init__(manufacturer, model, os, screen_size, memory)

    def unlocking(self):
        return "Write a password"
