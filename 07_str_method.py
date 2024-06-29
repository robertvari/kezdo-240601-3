class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"Hello, my name is {self.name}"

kriszta = Person("Kriszta")
tamas = Person("Tamás")

print(kriszta)
print(tamas)