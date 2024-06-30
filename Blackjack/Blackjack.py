import os, time, random
from game_assets.cards import Deck
from game_assets.players import Player, AIPlayer


class Blackjack:
    def __init__(self):
        # First attributes
        self.__deck = Deck()
        self.__player = Player()
        self.__bet = 0

        self.__player_list = [
            self.__player,
            AIPlayer(),
            AIPlayer(),
            AIPlayer()
        ]

        # Then method calls
        self.__clear_screen()
        self.__intro()

        time.sleep(5)

        self.__game_loop()

    def __game_loop(self):
        self.__clear_screen()
        self.__deck.reset()

        random.shuffle(self.__player_list)

        for player in self.__player_list:
            player.init_hand(self.__deck)
            if player.playing:
                self.__bet += 10

        playing_players = [i for i in self.__player_list if i.playing]

        for player in playing_players:
            player.draw(self.__deck)

        for player in playing_players:
            player.show_hand()

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