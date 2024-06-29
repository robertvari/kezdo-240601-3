class Person:
    # Constructor of my class
    def __init__(self, name):
        self.name = name

    # You need this if you want to print your class
    def __str__(self) -> str:
        return f"Hello, my name is {self.name}"
    
    # You need this if you print your class in a list
    def __repr__(self):
        return self.name

kriszta = Person("Kriszta")
tamas = Person("Tamás")
csaba = Person("Csaba")
adam = Person("Ádám")

my_driends = [kriszta, tamas, csaba, adam]

print(kriszta)
print(my_driends)