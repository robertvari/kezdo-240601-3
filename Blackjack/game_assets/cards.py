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

if __name__ == '__main__':
    my_card1 = Card("Spade King", 10)
    my_card2 = Card("Spade Ace", 11)
    deck = [my_card1, my_card2]
    print(deck)
    print(my_card1)