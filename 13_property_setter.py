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

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, new_email):
        assert isinstance(new_email, str), "Email is a type of string."
        assert "@" in new_email, "This is not a valid email address" 
        assert new_email.endswith(".com"), "This is not a valid email" 

        self.__email = new_email

csaba = Person("Kiss", "Csaba", "csaba@gmail.com")
csaba.email = "wolfie77@gmail.com"
print(csaba.full_name, csaba.email)