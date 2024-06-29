# class definition
class Person:
    def __init__(self, name, email, address):
        # instance attribute
        self.name = name
        self.email = email
        self.address = address


# create instances
csaba = Person("Csaba", "csaba@gmail.com", "Budapest")
tamas = Person("Tamas", "tamas@gmail.com", "Pécs")

print(csaba.name, csaba.email, csaba.address)
print(tamas.name, tamas.email, tamas.address)