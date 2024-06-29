class Person:
    def __init__(self, name, password, email):
        self.__name = name
        self.__email = email
        self.__password = password

    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    
    def set_email(self, new_email):
        assert isinstance(new_email, str), "Email is a type of string."
        assert "@" in new_email, "This is not a valid email address" 
        assert new_email.endswith(".com"), "This is not a valid email"               

        self.__email = new_email

    def set_password(self, new_password):
        assert len(new_password) > 6, "Password needs to be longer than 6 characters"
        self.__password = new_password

csaba = Person("Csaba", "testpas123", "csaba@gmail.com")
csaba.set_email("wolfie45@gmail.com")
csaba.set_password("helloworld")
print(csaba.get_name(), csaba.get_email())