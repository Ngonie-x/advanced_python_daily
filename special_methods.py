class Card:
    insure = False
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()
        
    def __repr__(self):
        return "{__class__.__name__}(suit={suit!r}, rank={rank!r})".format(__class__=self.__class__, **self.__dict__)
        
        
    def __str__(self):
        return "{rank} {suit}".format(**self.__dict__)
    
    
    def __format__(self, format_spec):
        if format_spec == '':
            return str(self)
        rs = format_spec.replace('%r', self.rank).replace('%s', self.suit)
        rs = rs.replace('%%', '%')
        return rs
    
class NumberCard(Card):
    def _points(self):
        return int(self.rank), int(self.rank)
    
    
class Hand:
    def __init__(self, dealer_card, *cards):
        self.dealer_card = dealer_card
        self.cards = list(cards)
    
    def __str__(self):
        return ", ".join(map(str, self.cards))
    
    def __repr__(self):
        return "{__class__.__name__}({dealer_card!r}, {_cards_str})".format(
            __class__=self.__class__,
            _cards_str=", ".join(map(repr, self.cards)), **self.__dict__
            )
        
    def __format__(self, format_spec):
        if format_spec =='':
            return str(self)
        return ", ".join("{0:{fs}}".format(c, fs=format_spec) for c in self.cards)
    
    
    
class BlackJackCard_p:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __lt__(self, other):
        print("Compare {0} < {1}".format(self, other))
        return self.rank < other.rank
    
    def __str__(self):
        return "{rank} {suit}".format(**self.__dict__)
    

class Noisy:
    def __del__(self):
        print("Removing {0}".format(id(self)))