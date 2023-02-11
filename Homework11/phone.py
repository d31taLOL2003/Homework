from igadget import IGadget


class Phone(IGadget):
    def __init__(self, model: str, os: str, screen_size: str, memory: int):
        """
        The Phone class inherits the IGadget class. Here in 'def __init__' we write parameters 
        for the Phone class. 
        We also make sure to write our methods 'charge' and 'discharge', which are abstract methods of 
        the IGadget class, and the Phone class inherits them.
        """
        self.__model = model
        self.__os = os
        self.__screen_size = screen_size
        self.__memory = memory
        self.__battery_level = 79

    @property
    def model(self) -> str:
        """
        This method return Model. And we use "property" 
        so that we can output this method as a parameter
        """
        model = f"\nModel: {self.__model}"
        return model

    @property
    def os(self) -> str:
        """
        This method return Operating System. And we use "property" 
        so that we can output this method as a parameter
        """
        os = f"\nOperating System: {self.__os}"
        return os

    @property
    def screen_size(self) -> str:
        """
        This method return Screen Size. And we use "property" 
        so that we can output this method as a parameter
        """
        screen_size = f"\nScreen Size: {self.__screen_size} inches"
        return screen_size
    
    @property
    def memory(self) -> int:
        """
        This method return Memory. And we use "property" 
        so that we can output this method as a parameter
        """
        memory = f"\nMemory: {self.__memory} GB"
        return memory

    @property
    def battery_level(self) -> str:
        """
        This method return Battery level which defaults to 79. And we use "property" 
        so that we can output this method as a parameter
        """
        battery = f"\nBattery level: {self.__battery_level}"
        return battery

    def charge(self, percentage: int) -> str:
        """
        Method charge takes int value from the parameter "precentage", which the user entered.
        Next we add this value to our parameter "self.__battery_level". And we have a condition here, 
        if the value in the parameter is greater than 100, we will assign 100 to our parameter.
        For example: self.__battery_level = 79, percentage = 30, self.__battery_level + percentagel = 109.
        Our result: Battery charged by 30%. Current battery level: 100%
        """
        self.__battery_level += percentage
        if self.__battery_level > 100:
            self.__battery_level = 100
        print(f"\nBattery charged by {percentage}%.\nCurrent battery level: {self.__battery_level}%")
    
    def discharge(self, percentage: int) -> str:
        """
        Method discharge takes int value from the parameter "precentage", which the user entered.
        Next we subtract this value to our parameter "self.__battery_level". And we have a condition here, 
        if the value in the parameter is less than 0, we will assign 0 to our parameter.
        For example: self.__battery_level = 100, percentage = 101, self.__battery_level - percentage = -1.
        Our result: Battery charged by 101%. Current battery level: 0%
        """
        self.__battery_level -= percentage
        if self.__battery_level < 0:
            self.__battery_level = 0
        print(f"\nBattery discharged by {percentage}%.\nCurrent battery level: {self.__battery_level}%")
