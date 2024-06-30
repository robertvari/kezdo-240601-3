import random, time

class Player_BASE:
    def __init__(self):
        # First attributes
        self.__name = None
        self.__credits = 0
        self.__hand = []
        self.__playing = True

        # Then method calls
        self._create()

    def _create(self):
        self.__credits = random.randint(50, 100)
        self.__name = self.__get_random_name()

    def _set_name(self, new_name):
        self.__name = new_name

    def __get_random_name(self):
        first_names = ["Marnie", "Johnathan", "Mahnoor", "Hassan", "Alissa", "Millie", "Qasim", "Damon", "Shreya", "Carly"]
        last_names =  ["Roy", "Aguirre", "Sandoval", "Rogers", "Cole", "Matthams", "Allen", "Stokes", "Deleon", "Hampton"]

        return f"{random.choice(first_names)} {random.choice(last_names)}"

    @property
    def hand_value(self):
        return sum([card.value for card in self.__hand])

    def draw(self, deck):
        while self.__playing:
            if self.hand_value < 16:
                print(f"{self.__name} draws a card...")
                time.sleep(2)
                self.__hand.append(deck.draw())
            else:
                print(f"{self.__name} finishes drawing.")
                self.__playing = False

    def show_hand(self):
        print(self.__hand, f"Hand value: {self.hand_value}")

class Player(Player_BASE):
    def _create(self):
        super()._create()
        # self._set_name(input("What is your name? "))
        self._set_name("Robert Vari")

class AIPlayer(Player_BASE):
    pass


if __name__ == '__main__':
    from cards import Deck
    deck = Deck()

    ai_player = AIPlayer()
    player = Player()
    
    ai_player.draw(deck)
    player.draw(deck)

    ai_player.show_hand()
    player.show_hand()