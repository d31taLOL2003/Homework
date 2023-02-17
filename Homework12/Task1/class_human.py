from class_action import Action


class Human:
    """
    A class representing a human, which can perform actions using an instance of the Action class.

    Attributes:
        __action (Action): An instance of the Action class representing the current action the human is performing.

    Methods:
        action() -> Action: Returns the current Action instance representing the human's current action.
        do_action() -> None: Executes the current action by calling the corresponding method on the Action instance.
    """
    def __init__(self, action: Action):
        self.__action = action

    @property
    def action(self) -> Action:
        """
        Returns the current Action instance representing the human's current action.

        Returns:
            Action: An instance of the Action class representing the current action the human is performing.
        """
        return self.__action

    def do_action(self) -> None:
        """
        Executes the current action by calling the corresponding method on the Action instance.
        """
        self.action()
