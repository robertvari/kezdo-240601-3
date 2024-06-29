# class definition
class Person:
    # class attributes
    name = None
    email = None
    address = None
    credits = 0

# create instances
csaba = Person()
tamas = Person()

# Fill out the forms
csaba.name = "Kiss Csaba"
csaba.email = "csaba@gmail.com"
csaba.address = "Budapest"

tamas.name = "Kovács Tamás"
tamas.email = "tamas@gmail.com"
tamas.address = "Pécs"

print(csaba.name, csaba.email, csaba.address, csaba.credits)
print(tamas.name, tamas.email, tamas.address, tamas.credits)