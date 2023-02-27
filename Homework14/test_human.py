import pytest
from human import Human


@pytest.fixture()
def human():
    """
    A Pytest fixture that yields a Human object with the name "John", age 32, and gender "male".

    Yields:
        Human: A Human object with the specified name, age, and gender.
    """
    yield Human("John", 32, "male")


def test_init_human(human: Human) -> None:
    """
    Test the initialization of a Human object with specific attributes.

    Args:
        human (Human): A Human object to be tested.

    Returns:
        None

    Raises:
        AssertionError: If any of the attributes of the Human object do not match the expected values.
    """
    assert human._Human__name == "John"
    assert human._Human__age == 32
    assert human._Human__gender == f"male"
    assert human._Human__status == "alive"
    assert human._Human__age_limit == 100


def test_grow(human: Human) -> None:
    """
    Test the 'grow' method of a Human object.

    Args:
        human (Human): A Human object to be tested.

    Returns:
        None

    Raises:
        AssertionError: If the 'age' attribute of the Human object does not increase by 1 after the 'grow' method is called.
    """
    human.grow()
    assert human.age == 33


def test_grow_past_age_limit(human: Human) -> None:
    """
    Test the 'grow' method of a Human object when the age limit has been reached.
    Args:
        human(Human): A Human object to be tested.

    Returns:
        None

    Raises:
        AssertionError: If the 'status' attribute of the Human object is not set to "dead" after the 'grow' method is called and the age limit has been reached.
    """
    human._Human__age = 100
    human.grow()
    assert human._Human__status == "dead"


def test_change_gender(human: Human) -> None:
    """
    Test the 'change_gender' method of a Human object.
    Args:
        human(Human): A Human object to be tested.

    Returns:
        None

    Raises:
         AssertionError: If the 'gender' attribute of the Human object is not changed to the expected value after the `change_gender` method is called.
    """
    human.change_gender("female")
    assert human.gender != "male"
    assert human.gender == "female"


def test_change_gender_same_as_current(human: Human) -> None:
    """
    Test the 'change_gender' method of a Human object when attempting to set the gender to the same value.
    Args:
        human(Human): A Human object to be tested.

    Returns:
        None

    Raises:
        AssertionError: If the 'change_gender' method of the Human object does not raise an exception when attempting to set the gender to the same value.
    """
    with pytest.raises(Exception, match="already has gender"):
        human.change_gender("male")


def test_change_gender_invalid_gender(human: Human) -> None:
    """
    Test the 'change_gender' method of a Human object when attempting to set an invalid gender.

    Args:
        human (Human): A Human object to be tested.

    Returns:
        None

    Raises:
        AssertionError: If the 'change_gender' method of the Human object does not raise an exception when attempting to set an invalid gender.
    """
    with pytest.raises(Exception, match="Not correct name of gender"):
        human.change_gender("combat helicopter")


def test_is_alive(human: Human) -> None:
    """
    Test the '__is_alive' method of a Human object to ensure that it returns True when the Human is alive.

    Args:
        human (Human): A Human object to be tested.

    Returns:
        None

    Raises:
        AssertionError: If the '__is_alive' method of the Human object does not return True when the Human is alive.
    """
    assert human._Human__is_alive()


def test_is_dead(human: Human) -> None:
    """
    Test the '__is_alive' method of a Human object to ensure that it raises an exception when the Human is dead.

    Args:
        human (Human): A Human object to be tested.

    Returns:
        None

    Raises:
        AssertionError: If the '__is_alive' method of the Human object does not raise an exception when the Human is dead, or if the exception message does not contain the expected string.
    """
    human._Human__status = "dead"
    with pytest.raises(Exception, match="is already dead"):
        human._Human__is_alive()


def test_age(human: Human) -> None:
    """
    Test the 'age' property of a Human object to ensure that it returns the correct value.

    Args:
        human (Human): A Human object to be tested.

    Returns:
        None

    Raises:
        AssertionError: If the 'age' property of the Human object does not return the expected value.
    """
    assert human.age == 32


def test_gender(human: Human) -> None:
    """
    Test the 'gender' property of a Human object to ensure that it returns the correct value.

    Args:
        human(Human): A Human object to be tested.

    Returns:
        None

    Raises:
        AssertionError: If the 'gender' property of the Human object does not return the expected value.
    """
    assert human.gender == "male"


def test_name_type(human):
    """
    Test check the type of data attribute 'name'

    Args:
        human(Human): A Human object to be tested.

    Returns:
        None

    Raises:
        AssertionError: If the data type does not match
    """
    name = human._Human__name
    assert isinstance(name, str)


def test_age_type(human):
    """
    Test check the type of data attribute 'age'

    Args:
        human(Human): A Human object to be tested.

    Returns:
        None

    Raises:
        AssertionError: If the data type does not match
    """
    age = human.age
    assert isinstance(age, int)


def test_gender_type(human):
    """
    Test check the type of data attribute 'gender'

    Args:
        human(Human): A Human object to be tested.

    Returns:
        None

    Raises:
        AssertionError: If the data type does not match
    """
    gender = human.gender
    assert isinstance(gender, str)
