import os
from game_assets.cards import Deck

class Blackjack:
    def __init__(self):
        # First attributes
        self.__deck = Deck()

        # Then method calls
        self.__clear_screen()
        self.__intro()

    def __clear_screen(self):
        os.system("cls")

    def __intro(self):
        print("*"*50, "BLACKJACK", "*"*50)
        print("This is a simple card game. Your only goal is to collect cards till your hand's value reaches 21.")

    def __exit_game(self):
        self.__clear_screen()
        print("See you later! :)")
        exit()

Blackjack()