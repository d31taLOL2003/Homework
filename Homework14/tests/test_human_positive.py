import pytest
from human import Human


def test_age(john: Human) -> None:
    """
    Tests whether the age attribute of the Human object is set correctly.

    Args:
        john: A Human object representing a person.

    Returns:
        None

    Raises:
        AssertionError: If the age of the john object is not 32.
    """
    assert john.age == 32


def test_grow(john: Human) -> None:
    """
    Tests whether the age of the Human object increases by 1 year when the 'grow' method is called.
    Args:
        john: A Human object representing a person.

    Returns:
        None

    Raises:
        AssertionError: If the age of the john object is not 33 after calling the 'grow' method once.
    """
    john.grow()
    assert john.age == 33


def test_old_human(old_john: Human) -> None:
    """
    Tests whether the status of the Human object becomes "dead" after the age of the object exceeds the maximum age.

    Args:

        old_john: A Human object representing an old person.

    Returns:
        None.

    Raises:
        AssertionError: If the status of the old_john object is not "dead" after calling the 'grow' method.
    """
    old_john.grow()
    assert old_john._Human__status == "dead"


@pytest.mark.parametrize("gender", ["male", "female"])
def test_change_gender(john: Human, gender) -> None:
    """
    Tests whether the 'change_gender' method of the Human object changes the gender attribute of the object correctly.

    Args:
        john: A Human object representing a person.
        gender: A string representing the gender that the john object will be changed to.

    Returns:
        None.

    Raises:
        AssertionError: If the gender of the john object is not the same as the gender passed as an argument.
    """
    john.change_gender(gender)
    assert john.gender == gender


@pytest.mark.parametrize("age", [33, 40, 55])
def test_age_type(john: Human, age) -> None:
    """
    Tests whether the age attribute of the Human object is an integer.

    Args:
        john: A Human object representing a person.
        age: An integer representing the age of the john object.

    Returns:
        None.

    Raises:
        AssertionError: If the age attribute of the john object is not an integer.
    """
    age = john.age
    assert isinstance(age, int)
###

@pytest.mark.parametrize("gender", ["male", "female", "apache attack helicopter"])
def test_gender_type(john: Human, gender) -> None:
    """
    Tests whether the gender attribute of the Human object is a string.

    Args:
        john: A Human object representing a person.
        gender: A string representing the gender of the john object.
    Returns:
        None.
    Raises:
        AssertionError: If the gender attribute of the john object is not a string.
    """
    gender = john.gender
    assert isinstance(gender, str)
