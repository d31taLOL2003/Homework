class Company:
    def __init__(self, name, location):
        """
        :param name: The name of the company
        :param location: The location of the company
        """
        self.name = name
        self.location = location

    def message(self):
        """
        :return: A string representation of the company
        """
        return f"{self.name} is located at {self.location}"


open_ai = Company("OpenAi", "San Francisco")
print(f"Name of the company: {open_ai.name}")
print(f"Location: {open_ai.location}")
print(open_ai.message())

print("\n")

apple = Company("Apple", "San Francisco")
print(f"Name of the company: {apple.name}")
print(f"Location: {apple.location}")
print(apple.message())


class Employee:
    def __init__(self, name, salary, position):
        """
        :param name: name of employee
        :param salary: salary of employee
        :param position: position of employee
        """
        self.name = name
        self.salary = salary
        self.position = position

    def message(self):
        """
        :return: A string representation of the employee
        """
        return f"The employee's name is {self.name}, he works {self.position}. And his salary is ${self.salary}."


print("\n")

john = Employee("John", 4000, "QA Automation")
print(f"Name of employee: {john.name}")
print(f"Salary: {john.salary}")
print(f"Position: {john.position}")
print(john.message())

print("\n")

dave = Employee("Dave", 6000, "Python Developer")
print(f"Name of employee: {dave.name}")
print(f"Salary: {dave.salary}")
print(f"Position: {dave.position}")
print(dave.message())
