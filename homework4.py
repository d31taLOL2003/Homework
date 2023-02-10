# Task 1.
# There is a list of arbitrary numbers, for example [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44]. 
# Write a code that will delete (not create a new one, but delete!) all numbers that are less than 21 and greater than 74 from it.

lst = [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44]
lst_copy = lst.copy() # Copy of the original list.
for number in lst_copy: # Iterates over a copy of the original list.
    if number < 21:
        lst.remove(number) # Removes the number from the original list.
    if number > 74:
        lst.remove(number)
print(lst) # Dispalies the list of numbers that are less than 21 and greater than 74 from the original list.

# Task 2.
#There are two arbitrary numbers responsible for the minimum and maximum price. 
# There is a Dict with store names and prices: 
# { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}. 
# Write the code that will find and display the names of stores, the prices of which fall into the range between the minimum and maximum price.

shops = {
    'cito': 47.999,
    'BB_studio': 42.999,
    'momo': 49.999,
    'main-service': 37.245,
    'buy.now': 38.324,
    'x_store': 37.166,
    'the_patner': 38.988,
    'store': 37.720,
    'rozetka': 38.003
}

print("Hi. Please enter the minimum and maximum price.")
min_price = float(input("Min. price: ")) # Enter the minimum price here.
max_price = float(input("Max. price: ")) # Enter the maximum price here.
print("\nResult:")
for shop, price in shops.items(): # A loop that takes keys(shop) and values(price) ​​from a dictionary.
    if price >= min_price and price <= max_price: # A condition that compares the value from the dictionary(price) and the value entered by the user(min_price and max_price).
        print(shop) # Displaies stores that fall with in the range entered by the user.
