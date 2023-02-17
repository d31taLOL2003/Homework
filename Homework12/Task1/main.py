from class_action import Action
from class_human import Human


if __name__ == "__main__":
    humans = [Human(Action("walking")), Human(Action("running")), Human(Action("sleeping"))]

    for human in humans:
        human.do_action()
