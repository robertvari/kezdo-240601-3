class Person:
    def __init__(self, name):
        self.name = name

    # this is a method of the Person class
    def say_hello(self):
        print(f"Hello, my name is {self.name}")

    def how_are_you(self):
        print("I'm fine, thank you :))")

csaba = Person("Csaba")
balazs = Person("Balazs")
kriszta = Person("Kriszta")

csaba.say_hello()
balazs.say_hello()
kriszta.how_are_you()