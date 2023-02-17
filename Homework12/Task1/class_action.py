class Action:
    """
    A class representing an action that can be performed by a Human object.

    Attributes:
        name (str): The name of the action.

    Methods:
        __call__() -> str: Returns a string representing the action being performed.
    """
    def __init__(self, name: str):
        """
        Initializes a new instance of the Action class.

        Parameters:
            name (str): The name of the action.

        Returns:
            None
        """
        self.name = name

    def __call__(self) -> str:
        """
        Returns:
            str: A string representing the action being performed.
        """
        print(f"Performing action: {self.name}")
