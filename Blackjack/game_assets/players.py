import random

class Player_BASE:
    def __init__(self):
        # First attributes
        self.__name = None
        self.__credits = 0
        self.__hand = []
        self.__playing = True

        # Then method calls
        self.__create()

    def __create(self):
        self.__credits = random.randint(50, 100)

    def __get_random_name(self):
        first_names = ["Marnie", "Johnathan", "Mahnoor", "Hassan", "Alissa", "Millie", "Qasim", "Damon", "Shreya", "Carly"]
        last_names =  ["Roy", "Aguirre", "Sandoval", "Rogers", "Cole", "Matthams", "Allen", "Stokes", "Deleon", "Hampton"]

class Player(Player_BASE):
    pass

class AIPlayer(Player_BASE):
    pass


if __name__ == '__main__':
    ai_player = AIPlayer()
    player = Player()
    pass