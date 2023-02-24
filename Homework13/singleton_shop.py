def singleton_shop(cls: type) -> type:
    """
    The function is a Shop class decorator, it implements the sigleton pattern, 
    checks if an instance of the Shop class was created, 
    if it was, it just returns it for further work, if not, it creates it.

    Args:
        cls (type): The Shop class.

    Returns:
        type: Shop class instance.
    """
    __instances = {}

    def wrapper(*args, **kwargs):
        if cls not in __instances:
            __instances[cls] = cls(*args, **kwargs)
        return __instances[cls]
    return wrapper
