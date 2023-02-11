from phones import Apple
from phones import Samsung

if __name__ == "__main__":
    """
    To be able to output our results, we need to import from the file 
    where our Apple and Samsung classes are located to the file main.py
    """
    iphone_14 = Apple("Apple", "iPhone 14", "IOS", 6.7, 128, 12)
    print(f"Manufacturer: {iphone_14.get_manufacturer()}")
    print(f"Model: {iphone_14.get_model()}")
    print(f"Operating System: {iphone_14.get_os()}")
    print(f"Screen Size: {iphone_14.get_screen_size()} inches")
    print(f"Memory: {iphone_14.get_memory()} GB")
    print(f"Camera: {iphone_14.get_camera()} megapixels")
    print(f"Unlocking method: {iphone_14.unlocking()}")
    print(iphone_14.play_music())

    print("\n")

    samsung_s23 = Samsung("Samsung", "Samsung S23", "Android", 6.1, 128, 12)
    print(f"Manufacturer: {samsung_s23.get_manufacturer()}")
    print(f"Model: {samsung_s23.get_model()}")
    print(f"Operating System: {samsung_s23.get_os()}")
    print(f"Screen Size: {samsung_s23.get_screen_size()} inches")
    print(f"Memory: {samsung_s23.get_memory()} GB")
    print(f"Camera: {samsung_s23.get_camera()} megapixels")
    print(f"Unlocking method: {samsung_s23.unlocking()}")
    print(samsung_s23.take_photo())
