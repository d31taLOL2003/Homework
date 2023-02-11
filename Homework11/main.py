from phone import Phone


if __name__ == "__main__":
    """
    To be able to display our results, we need to import from the file 
    where our Phone class is, into the main.py file
    """
    my_phone = Phone("realme 6", "Android", "6.5", 64)
    print(my_phone.model)
    print(my_phone.screen_size)
    print(my_phone.memory)
    print(my_phone.battery_level)
    my_phone.charge(30)
    my_phone.discharge(101)
