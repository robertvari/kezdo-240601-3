class Person:
    # class attribute
    name = "Tamás"
    
    def __init__(self, name):
        # instance attribute
        self.name = name

csaba = Person("Csaba")
geza = Person("Géza")
balazs = Person("Balázs")

print(Person.name)
print(csaba.name)
print(geza.name)
print(balazs.name)