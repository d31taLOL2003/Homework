"""
App "Cashier at the cinema". What we need to do?
1. Create the function "age_verification". +
2. Create the function "get_age". +
3. Create the function "cinema". +
"""

def age_verification(age):
    """
    Checks into which range the number entered by the user will fall. 
    (all outputs take place in the function "cinema").
    -----------------------------------
    Args:
        age(int): Number entered by the user(in the function "get_age")
    Returns:
        (str): Message output in the function "cinema"
    """
    str_age = str(age)
    numbers_ukrainian = {
        "0": "років",
        "1": "рік",
        "2": "роки",
        "3": "роки",
        "4": "роки",
        "5": "років",
        "6": "років",
        "7": "років",
        "8": "років",
        "9": "років",
        "11": "років",
        "12": "років",
        "13": "років",
        "14": "років",
    }
    the_same_numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    for numbers in the_same_numbers:
        if numbers == age:
            if str_age in numbers_ukrainian:
                return f"О, вам {age} {numbers_ukrainian[str_age]}! Який цікавий вік!"
            if str_age[1] in numbers_ukrainian:
                return f"О, вам {age} {numbers_ukrainian[str_age[1]]}! Який цікавий вік!"
    if age >= 1 and age < 7:
        if str_age in numbers_ukrainian:
            return f"Тобі ж {age} {numbers_ukrainian[str_age]}! Де твої батьки?"
    elif age >= 8 and age < 16:
        if str_age in numbers_ukrainian:
            return f"Тобі лише {age} {numbers_ukrainian[str_age]}, а це фільм для дорослих!"
        if str_age[1] in numbers_ukrainian:
            return f"Тобі лише {age} {numbers_ukrainian[str_age[1]]}, а це фільм для дорослих!"
    elif age > 65 and age <= 99:
        if str_age[1] in numbers_ukrainian:
            return f"Вам {age} {numbers_ukrainian[str_age[1]]}? Покажіть ваше посвідчення!"
    elif age > 99 and age <= 110:
        if str_age[2] in numbers_ukrainian:
            return f"Вам {age} {numbers_ukrainian[str_age[2]]}? Покажіть ваше посвідчення!"
    elif age == 0 or age > 110:
        if str_age in numbers_ukrainian:
            return f"{age} {numbers_ukrainian[str_age]}? А ви впевненні, що вам стільки?"
    else:
        if str_age[1] in numbers_ukrainian:
            return f"Незважаючи на те, що вам {age} {numbers_ukrainian[str_age[1]]}, квитків всеодно нема!"


def get_age():
    """
    Asks the user for their age.
    -----------------------------------
    Args:
        None
    Returns:
        (int): Number entered by the user
    """
    while True:
        age = input("Вітаємо вас до нашого кінотеатру. Будь ласка, ведіть свій вік: ")
        if age.isdigit():
            return int(age)
        else:
            print("Помилка! Будь ласка, введіть цифри у текстове поле. \nНаприклад: 1, 2, 3, 4, 5, т.д.\n")
        

def cinema():
    """
    In the two previous functions, there was processing. 
    And here will be the output of verified data and if necessary, 
    the user can start again or stop the program.
    -----------------------------------
    Args:
        None
    Returns:
        Outputs a message and the age that the user entered
    """
    while True:
        user_age = get_age()

        print(age_verification(age=user_age))
        repeat = input("\nЧи бажаєте ви продовжити? (так/ні): ")
        if repeat.lower() == "так" or repeat.lower() == "т":
            continue
        elif repeat.lower() == "ні" or repeat.lower() == "н":
            break
        else:
            print("Введіть так або ні.")
            repeat = input("\nЧи бажаєте ви продовжити? (так/ні): ")
            if repeat.lower() == "так" or repeat.lower() == "т":
                continue
            elif repeat.lower() == "ні" or repeat.lower() == "н":
                break

cinema()
