class Person:
    def __init__(self, name, password, email):
        self.__name = name
        self.__email = email
        self.__password = password

    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email

csaba = Person("Csaba", "testpas123", "csaba@gmail.com")
print(csaba.get_name(), csaba.get_email())