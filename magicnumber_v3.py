import os, random, time


class MagicNumber:
    def __init__(self):
        self.__player = Player()
        self.__computer = Computer()
        self.__trycount = 3

        self.clear_screen()
        self.intro()

        if self.__player.ask_for_start_game():
            print("Start game...")
        else:
            self.exit_game()
    
    def clear_screen(self):
        os.system("cls")

    def intro(self):
        print("*"*50, "MAGIC NUMBERS", "*"*50)
        self.__player.get_name()

        print(f"Hello {self.__player.name}. This is a simple game where I think of a number between {self.__computer.min_number}-{self.__computer.max_number}")
        print("and you have to guess it. You can try 3 times.")
        print("I give you 30 credits to start. If you guess right you win 10 credits.")
        print("Be careful, you could lose all your credits ;)")

    def exit_game(self):
        self.clear_screen()
        print("Sorry to see you go :( Maybe next time ;)")

class Player:
    def __init__(self):
        self.__name = None
        self.__credits = 0
        self.__my_number = 0

    @property
    def name(self):
        return self.__name

    def get_name(self):
        self.__name = input("What is your name?")

    def ask_for_start_game(self):
        result = input("Are you ready? (y/n)")
        if result == "y":
            return True
        return False
    
    def ask_for_new_round(self):
        result = input("Do you want to play again? (y/n)")
        if result == "y":
            return True
        return False

class Computer:
    def __init__(self):
        self.__min_number = 1
        self.__max_number = 10
        self.__my_number = 0

    @property
    def min_number(self):
        return self.__min_number
    
    @property
    def max_number(self):
        return self.__max_number

MagicNumber()