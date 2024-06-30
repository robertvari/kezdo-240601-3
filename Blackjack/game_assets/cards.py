class Card:
    def __init__(self, name, value):
        self.__name = name
        self.__value = value

    @property
    def value(self):
        return self.__value
    
    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"Name: {self.__name} Value: {self.__value}"
    
    def __repr__(self):
        return self.__name

class Deck:
    def __init__(self):
        # first attributes
        self.__cards = []

        # then method calls
        self.reset()

    def reset(self):
        self.__cards.clear()

        # your classic python variable
        cards = [
            ["2", 2],
            ["3", 3],
            ["4", 4],
            ["5", 5],
            ["6", 6],
            ["7", 7],
            ["8", 8],
            ["9", 9],
            ["10", 10],
            ["King", 10],
            ["Queen", 10],
            ["Jack", 10],
            ["Ace", 11]
        ]

        suits = ["Heart", "Club", "Diamond", "Spade"]

        for suit in suits:
            for card_data in cards:
                name = f"{suit} {card_data[0]}"
                value = card_data[1]
                new_card = Card(name, value)
                self.__cards.append(new_card)
    
    def draw(self):
        pass

    def show(self):
        print(self.__cards)

    @property
    def size(self):
        return len(self.__cards)

if __name__ == '__main__':
    deck = Deck()
    deck.show()
    if deck.size == 0:
        print("End round")