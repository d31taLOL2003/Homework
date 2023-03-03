import pytest
from human import Human


def test_change_gender_same_as_current(john: Human) -> None:
    """
    Tests whether 'change_gender' raises an exception when the same gender as the current gender is passed as an argument.

    Args:
        john: A Human object representing a person.

    Returns:
        None.

    Raises:
        Exception: If the john object already has the gender that is passed as an argument.
    """
    with pytest.raises(Exception, match="already has gender"):
        john.change_gender("male")

###
@pytest.mark.parametrize("invalid_gender", ["tank abrams", "apache attack helicopter"])
def test_change_gender_invalid_input(john: Human, invalid_gender) -> None:
    """
    Tests whether change_gender raises an exception when an invalid gender is passed as an argument.
    Args:
        john: A Human object representing a person.
        invalid_gender: A string representing an invalid gender.

    Returns:
        None.

    Raises:
        Exception: If the john object has an invalid gender.
    """
    with pytest.raises(Exception, match="Not correct name of gender"):
        john.change_gender(invalid_gender)


def test_is_dead(john: Human) -> None:
    """
    Tests whether the is_alive method of the Human class raises an exception when the status of
     the human object is "dead".
    Args:
        john: A Human object representing a person.

    Returns:
        None

    Raises:
        Exception: If the status of the john object is "dead".
    """
    john._Human__status = "dead"
    with pytest.raises(Exception, match="is already dead"):
        john._Human__is_alive()
