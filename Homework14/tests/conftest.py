import pytest
from human import Human


@pytest.fixture()
def john() -> Human:
    """
    Pytest fixture that returns an instance of Human with name "John",
    age 32 and gender "male"
    """
    yield Human("John", 32, "male")


@pytest.fixture
def old_john() -> Human:
    """
    Pytest fixture that returns an instance of Human with name "John",
    age 100 and gender "male"
    """
    yield Human("John", 100, "male")
