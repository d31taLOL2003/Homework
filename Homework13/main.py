from shop import Shop



if __name__ == "__main__":
    """
    A simple script that demonstrates the use of the Shop class.

    Creates instances of different items from the shop, gets their name and price, 
    and prints them to the console.
    """
    buckwheat = Shop().get_item("buckwheat")
    cookies = Shop().get_item("cookies")
    apples = Shop().get_item("apples")
    print(f"Item: {buckwheat.get_name()}\nPrice: {buckwheat.get_price()}")
    print(f"\nItem: {cookies.get_name()}\nPrice: {cookies.get_price()}\n")
    print(f"Item: {apples.get_name()}\nPrice: {apples.get_price()}")
