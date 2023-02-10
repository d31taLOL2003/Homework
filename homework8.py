# Task 1
def names_upper_func(name):
    return name.upper()


names_lower = ['alfred', 'ben', 'william']
names_upper = list(map(names_upper_func, names_lower))
print(names_upper)


# Task 2
def numbers_float_func(numbers):
    a = numbers ** 2
    return round(a, 3)


numbers_float_old = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
numbers_float_new = list(map(numbers_float_func, numbers_float_old))
print(numbers_float_new)


# Task 3
def zip_func(a_list, b_list):
    lst = list(zip(a_list, b_list))
    print(lst)


zip_func(['a', 'b', 'c', 'd', 'e'], [1, 2, 3, 4, 5])


# Task 4
def filter_func(name):
    if len(name) < 5:
        return True
    else:
        return False


names = "Jeff", "Alex", "Jonathan", "Richelle", "Anna"
res = list(filter(filter_func, names))
print(res)
