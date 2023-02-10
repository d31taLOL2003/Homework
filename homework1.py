"""Задача1: 
Створіть дві змінні first=10, second=30. 
Виведіть на екран результат математичної взаємодії (+, -, *, / і тд.) для цих чисел."""
first = 10
second = 30

addition = first + second # Додавання
print("Addition result:")
print(addition)

subtraction = first - second # Відінімання
print("\nSubtraction result:")
print(subtraction)

multiplication = first * second # Множення
print("\nMultiplication result:")
print(multiplication)

division = first / second # Ділення
print("\nDivision result:")
print(division)

integer_division = first // second # Цілочисельний поділ
print("\nInteger_division result:")
print(integer_division)

remainder = first % second # Залишок
print("\nRemainder result:")
print(remainder)

print("--------------------------------")
"""Задача2: 
Створіть змінну і по черзі запишіть в неї результат порівняння (<, > , ==, !=) чисел з завдання 1. 
Виведіть на екран результат кожного порівняння."""

less = addition < remainder # Знак менше
print("Less result:")
print(less)

gether = multiplication > subtraction # Знак більше
print("\nGether result:")
print(gether)

equal = division == integer_division # Знак дорівнює
print("\nEqual result:")
print(equal)

not_equal = remainder != addition # Знак не дорівнює
print("\nNot_equal result:")
print(not_equal)
