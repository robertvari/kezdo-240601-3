class Person:
    def __init__(self, name):
        # public attributes (you can print and change this)
        self.name = name

        # protected attributes (you can print this but shouldn't change it!!!)
        self._name = name

        # private attributes (you can't print and can't change this)
        self.__name = name


csaba = Person("Csaba")