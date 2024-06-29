import os, random


class MagicNumber:
    def __init__(self):
        self.__player = Player()
        self.__computer = Computer()

        self.clear_screen()
        self.intro()

        if self.__player.ask_for_start_game():
            self.game_loop()
        else:
            self.exit_game()
    
    def game_loop(self):
        self.clear_screen()

        # reset trycount
        trycount = 3

        self.__computer.think_a_number()
        self.__player.think_a_number()

        while self.__computer.my_number != self.__player.my_number:
            self.clear_screen()

            trycount -= 1
            if trycount == 0:
                break

            print(f"Wrong guess! You have {trycount} tries left. Try again.")
            self.__player.think_a_number()
        
        self.clear_screen()

        # End game conditions
        if self.__computer.my_number == self.__player.my_number:
            print(f"You win! {self.__computer.my_number} was my number! :)")
            print("I give you 10 credits :)")
            self.__player.give_credits(10)
        else:
            print(f"You lost the round. My number was {self.__computer.my_number}.")
            print(f"I take 10 credits from you.")
            self.__player.take_credits(10)

        
        if self.__player.credits > 0:
            print(f"You have {self.__player.credits} credits.")
        elif self.__player.credits == 0:
            print(f"You lost all of your credits but I give you an other chance.")
        else:
            print("You lost all of your credits. Game Over.")
            self.exit_game()

        if self.__player.ask_for_new_round():
            self.game_loop()
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
        exit()

class Player:
    def __init__(self):
        self.__name = None
        self.__credits = 0
        self.__my_number = 0

    @property
    def name(self):
        return self.__name

    @property
    def my_number(self):
        return str(self.__my_number)

    @property
    def credits(self):
        return self.__credits

    def give_credits(self, value):
        self.__credits += value

    def take_credits(self, value):
        self.__credits -= value

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

    def think_a_number(self):
        self.__my_number = input("What is your number? ")

class Computer:
    def __init__(self):
        self.__min_number = 1
        self.__max_number = 10
        self.__my_number = 0

    @property
    def my_number(self):
        return str(self.__my_number)

    @property
    def min_number(self):
        return self.__min_number
    
    @property
    def max_number(self):
        return self.__max_number

    def think_a_number(self):
        self.__my_number = random.randint(self.__min_number, self.__max_number)

MagicNumber()