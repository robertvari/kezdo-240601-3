class Person:
    # class attribute
    name = "Tamás"
    
    def __init__(self, name):
        # instance attribute
        self.name = name

csaba = Person("Csaba")

print(Person.name)
print(csaba.name)