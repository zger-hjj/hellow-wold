from six import add_metaclass
from abc import ABCMeta
import random
from functools import reduce


class PlayerNumberError(Exception):
    """
    用户数量错误
    """


def multi_pop(container, num=1):
    stack = []
    for i in range(num):
        stack.append(container.pop())
    return stack


def split_cards(container):

    for card in container:



def order_cards(cards):
    cards.sort(key=lambda x: x.num)


def merge_card(cards):
    return reduce(lambda x, y: x + y, cards)


class Game:
    def __init__(self, name='majhoon'):
        self.name = name
        self.current_cards = CardProxy.init_cards()

    def initialize(self, *players):
        if not len(players) == 4:
            raise PlayerNumberError('expected 4, get {0}'.format(len(players)))
        for player in players:
            if not isinstance(player, Player):
                raise TypeError('expected a instance of {0}, get {1}'.format(Player.__name__, type(player).__name__))
        for i in range(3):
            for player in players:
                player.cards.extend(multi_pop(self.current_cards, 4))


class CardProxy:
    @staticmethod
    def init_cards():
        sequence = []
        for card in CardProxy.look_up_card():
            sequence.extend(card(i) for i in range(1, card.gross + 1))
        sequence *= 4
        CardProxy.shuffle(sequence)
        return sequence

    @staticmethod
    def look_up_card():
        cards = []
        for key, value in globals().items():
            if isinstance(value, type) and issubclass(value, Card) and value is not Card:
                cards.append(value)
        return cards

    @staticmethod
    def shuffle(iterables):
        random.shuffle(iterables)

    @staticmethod
    def order_card(cards):
        sort_CARD = []
        Tong = []
        wan = []
        suo = []
        for card in cards:
            if card.name == "Tong":
                Tong.append(card)
            elif card.name == "Wan":
                wan.append(card)
            elif card.name == "Suo":
                suo.append(card)
        for i in sorted(Tong, key=lambda x: x.num):
            sort_CARD.append(i)
        for i in sorted(wan, key=lambda x: x.num):
            sort_CARD.append(i)
        for i in sorted(suo, key=lambda x: x.num):
            sort_CARD.append(i)
        # print(sort_CARD)
        return sort_CARD


@add_metaclass(ABCMeta)
class Card:
    def __init__(self, num):
        self.name = self.__class__.__name__
        self.num = num

    def __repr__(self):
        return '<%s:%s>' % (self.name, self.num)


class Tong(Card):
    gross = 9


class Wan(Card):
    gross = 9


class Suo(Card):
    gross = 9


class Player:
    def __init__(self, username='robot'):
        self.cards = []
        self.name = username
        self.status = 'Pending'

    def __repr__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

    def sortCard(self):
        self.cards = CardProxy.order_card(self.cards)


# class Tong(Card):
if __name__ == '__main__':
    # a = ['a', 'b', 'c']

    # Card.shuffle(a)
    # Card.shuffle(a)
    # print(Game.init_game())
    # print(Game.look_up_card())
    # print(Game.init_game())
    # print(Player())
    # player1 = Player('robot1')
    # player2 = Player('robot2')
    # player3 = Player('robot3')
    # player4 = Player('robot4')
    # Game().initialize(player1, player2, player3, player4)
    # print(player1.cards)
    # player1.sortCard()
    # print(player1.cards)
    # l = [1, 2, 3]
    print(reduce(lambda x, y: x + y, [[1, 2], [1, 2]]))
