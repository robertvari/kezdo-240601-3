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

    @property
    def name(self):
        return self.__name

    @property
    def playing(self):
        return self.__playing
    
    @playing.setter
    def playing(self, value):
        self.__playing = value

    @property
    def cards(self):
        return str(self.__hand)
    
    def _add_card(self, new_card):
        if self.hand_value > 10 and new_card.value == 11:
            new_card.change_ace()
        self.__hand.append(new_card)

    def init_hand(self, deck):
        self.__hand.clear()

        self.__hand.append(deck.draw())

        # Check if we draw two Aces
        new_card = deck.draw()
        #           True                  True
        if self.hand_value > 10 and new_card.value == 11:
            new_card.change_ace()

        self.__hand.append(new_card)

    def draw(self, deck):
        while self.__playing:
            if self.hand_value < 16:
                print(f"{self.__name} draws a card...")
                time.sleep(2)
                new_card = deck.draw()
                if self.hand_value > 10 and new_card.value == 11:
                    new_card.change_ace()
                self.__hand.append(new_card)
            else:
                print(f"{self.__name} finishes drawing.")
                self.__playing = False

    def show_hand(self):
        print(f"Name: {self.__name}", f"Cards: {self.__hand}", f"Hand value: {self.hand_value}")

class Player(Player_BASE):
    def _create(self):
        super()._create()
        # self._set_name(input("What is your name? "))
        self._set_name("Robert Vari")

    def draw(self, deck):
        print(f"This is your turn {self.name}")

        while self.playing:
            print(f"Your cards: {self.cards}")
            print(f"Your hand value: {self.hand_value}")

            response = input("Do you want to draw a card? (y/n)")

            if response == "y":
                new_card = deck.draw()
                print(f"Your new cards: {new_card}")
                self._add_card(new_card)
            else:
                self.playing = False

class AIPlayer(Player_BASE):
    pass


if __name__ == '__main__':
    from cards import Deck
    deck = Deck()

    ai_player1 = AIPlayer()
    player = Player()

    player.cards.append("Hello!!!")

    ai_player1.init_hand(deck)
    player.init_hand(deck)

    ai_player1.draw(deck)
    player.draw(deck)

    ai_player1.show_hand()
    player.show_hand()