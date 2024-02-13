class Employee():
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address


# Class freelancer inherits EMP
class Freelance(Employee):
    def __init__(self, id, name, address, email):
        super().__init__(id, name, address)
        self.email = email


emp1 = Freelance(401, "Hulugesh", "Bengaluru", "hulug...esh@gmail.com")
print('The ID is:', emp1.id)
print('The Name is:', emp1.name)
print('The Address is:', emp1.address)
print('The Email is:', emp1.email)
