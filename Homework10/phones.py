from gadget import Gadget


class Apple(Gadget):
    """
    Class Apple inherits class Gadget. Here in 'def __init__' we write the same parameters 
    of the Gadget class and apply the super function.
    We also make sure to write our 'unlocking' method, which is an abstract method of the Gadget class, 
    and the Apple class inherits it.
    """
    def __init__(self, manufacturer: str, model: str, os: str, screen_size: str, memory: str, camera: int):
        super().__init__(manufacturer, model, os, screen_size, memory)
        self.__camera = camera

    def get_camera(self) -> int:
        """
        Method get_camera returns number of megapixels
        """
        return self.__camera

    def unlocking(self) -> str:
        """
        Method unlocking returns string how to unlock the phone. Here we get "Need a fingerprint"
        """
        return "Need a fingerprint"

    def play_music(self) -> str:
        """
        Method play_music returns a string about the ability to play music.
        """
        return "Can play music"


class Samsung(Gadget):
    """
    In class Samsung everything happens in the same way as in the Apple class
    """
    def __init__(self, manufacturer: str, model: str, os: str, screen_size: str, memory: str, camera: int):
        super().__init__(manufacturer, model, os, screen_size, memory)
        self.__camera = camera

    def get_camera(self) -> int:
        """
        Method get_camera returns number of megapixels
        """
        return self.__camera

    def unlocking(self) -> str:
        """
         Method unlocking returns string how to unlock the phone. Here we get "Write a password"
        """
        return "Write a password"
    
    def take_photo(self) -> str:
        """
        Method take_photo returns a string about the ability to take a photo.
        """
        return "Can take a photo"
