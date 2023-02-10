import library
import pytest


examples_kopiyka = [
    (0, "0 копійок"),
    (1, "1 копійка"),
    (2, "2 копійки"),
    (5, "5 копійок"),
    (11, "11 копійок")
]

examples_hryvnia = [
    (0, "0 гривень"),
    (1, "1 гривня"),
    (2, "2 гривні"),
    (5, "5 гривень"),
    (11, "11 гривень")
]

examples_hryvnia_kopiyka = [
    (100, ['100 гривень', '0 копійок']),
    (10.11, ['10 гривень', '11 копійок']),
    (2.01, ['2 гривні', '1 копійка']),
    (125.339, ['125 гривень', '34 копійки'])
]

examples_is_hot_today = [
    (24, 'Сьогодні холодно'),
    (30, 'Сьогодні спекотно')
]


@pytest.mark.parametrize('value, expected', examples_kopiyka)
def test_kopiyka(value, expected):
    result = library.kopiyka(value)
    assert result == expected, f"For value {value}, expected {expected} but got {result}"


def test_kopiyka_return_type():
    result = library.kopiyka(10)
    assert isinstance(result, str), f"Expected string, but got {type(result)}"


@pytest.mark.parametrize('value, expected', examples_hryvnia)
def test_hryvnia(value, expected):
    result = library.hryvnia(value)
    assert result == expected, f"For value {value}, expected {expected} but got {result}"


def test_hryvnia_return_type():
    result = library.hryvnia(10)
    assert isinstance(result, str), f"Expected string, but got {type(result)}"


@pytest.mark.parametrize('value, expected', examples_hryvnia_kopiyka)
def test_hryvnia_kopiyka(value, expected):
    result = library.hryvnia_kopiyka(value)
    assert result == expected, f"For value {value}, expected {expected} but got {result}"


def test_hryvnia_kopiyka_type():
    result = library.hryvnia_kopiyka(10.11)
    assert isinstance(result, list), f"Expected list, but got {type(result)}"


@pytest.mark.parametrize('value, expected', examples_is_hot_today)
def test_is_hot_today(value, expected):
    result = library.is_hot_today(value)
    assert result == expected, f"For value {value}, expected {expected} but got {result}"


def test_is_hot_today_type():
    result = library.is_hot_today(25)
    assert isinstance(result, str), f"Expected string, but got {type(result)}"
    