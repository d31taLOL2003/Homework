from abc import ABC, abstractmethod


class IGadget(ABC):
    """
    The IGadget class is an abstraction and interface for the gadget, that is, there are two methods, 
    "charge" and "discharge", which are also abstract
    """
    @abstractmethod
    def charge(self):
        pass

    @abstractmethod
    def discharge(self):
        pass

