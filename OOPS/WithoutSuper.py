# code
class Person:

    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # To check if this person is an employee
    def display(self):
        print(self.name, self.id)


class Employee(Person):

    def __init__(self, name, id):
        self.name_ = name
        # super().__init__(name, id)

    def print(self):
        print("Employee class called")


emp_obj = Employee("Huli", 401)
print(emp_obj.name_)
print(emp_obj)
