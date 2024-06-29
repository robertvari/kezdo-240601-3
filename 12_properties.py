class Person:
    def __init__(self, first_name, last_name, email):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email

    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"
    
    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def last_name(self):
        return self.__last_name
    
    @property
    def name_length(self):
        return len(self.full_name)

csaba = Person("Kiss", "Csaba", "csaba@gmail.com")
print(csaba.full_name, csaba.name_length)