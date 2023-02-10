def kopiyka(number: int) -> str:
    """
    Convert a given integer to the corresponding Ukrainian word form for kopiyka,
    based on the last digit or digits of the number.

    Args:
        number: int number

    Returns:
        str: Ukrainian word form for kopiyka
    """
    numbers_ukrainian = {
        "0": "копійок",
        "1": "копійка",
        "2": "копійки",
        "3": "копійки",
        "4": "копійки",
        "5": "копійок",
        "6": "копійок",
        "7": "копійок",
        "8": "копійок",
        "9": "копійок",
        "11": "копійок",
        "12": "копійок",
        "13": "копійок",
        "14": "копійок",
    }
    int_number = int(number)
    str_number = str(number)
    if int_number >= 0 and int_number <= 9:
        if str_number[0] in numbers_ukrainian:
            return f"{int_number} {numbers_ukrainian[str_number[0]]}"
    elif int_number >= 10 and int_number <= 99:
        if str_number in numbers_ukrainian:
            return f"{int_number} {numbers_ukrainian[str_number]}"
        if str_number[1] in numbers_ukrainian:
            return f"{int_number} {numbers_ukrainian[str_number[1]]}"
    elif int_number >= 100:
        if str_number[2] in numbers_ukrainian:
            return f"{int_number} {numbers_ukrainian[str_number[2]]}"


def hryvnia(number: int) -> str:
    """
    Converts a number to a string representation of the Ukrainian hryvnia equivalent.

    Args:
        number: int number

    Returns:
        str: string representation of the Ukrainian hryvnia equivalent
    """
    numbers_ukrainian = {
        "0": "гривень",
        "1": "гривня",
        "2": "гривні",
        "3": "гривні",
        "4": "гривні",
        "5": "гривень",
        "6": "гривень",
        "7": "гривень",
        "8": "гривень",
        "9": "гривень",
        "11": "гривень",
        "12": "гривень",
        "13": "гривень",
        "14": "гривень",
    }
    int_number = int(number)
    str_number = str(number)
    if int_number >= 0 and int_number <= 9:
        if str_number in numbers_ukrainian:
            return f"{int_number} {numbers_ukrainian[str_number]}"
    elif int_number >= 10 and int_number <= 99:
        if str_number in numbers_ukrainian:
            return f"{int_number} {numbers_ukrainian[str_number]}"
        if str_number[1] in numbers_ukrainian:
            return f"{int_number} {numbers_ukrainian[str_number[1]]}"
    elif int_number >= 100 and int_number <= 999:
        if str_number[2] in numbers_ukrainian:
            return f"{int_number} {numbers_ukrainian[str_number[2]]}"
    elif int_number >= 1000 and int_number <= 9999:
        if str_number[3] in numbers_ukrainian:
            return f"{int_number} {numbers_ukrainian[str_number[3]]}"
    elif int_number >= 10000 and int_number <= 50000:
        if str_number[4] in numbers_ukrainian:
            return f"{int_number} {numbers_ukrainian[str_number[4]]}"


def hryvnia_kopiyka(number: float or int) -> list:
    """
    Accepts a number that divides into two parts. In a variable int_part we store an integer number with
    function int.
    In the float_part variable, we take the number that we got and subtract
    by the integer that is in the int_part variable.
    Then we multiply it by 100 and round it to the nearest integer with the round() function.

    Args:
        number: float or int number

    Returns:
        return [hryvnia(int_part), kopiyka(float_part)]: [hryvnia, kopiyka]

    """
    int_part = int(number)
    float_part = int(round(100 * (number - int_part)))
    return [hryvnia(int_part), kopiyka(float_part)]


def get_number(message: float or int) -> float:
    """
    Аccepts a floating point number from an incoming message.

    Args:
        number: float or int number

    Returns:
        float number

    """
    while True:
        try:
            user_input = float(input(message))
            return user_input
        except:
            print("Будь ласка, введіть правильну сумму!")


def is_hot_today(temperature=30) -> str:
    """
    Check if the temperature is hot or not.

    Args:
        temperature: The temperature to be checked. Default is 30.
    Returns:
        A string indicating whether the temperature is hot or not.
    """
    if temperature > 25:
        return "Сьогодні спекотно"
    else:
        return "Сьогодні холодно"
