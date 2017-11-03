class Card(object):
    def __init__(self,suit,val):
        self.suit = suit
        self.value = val

    def show(self):
        print ("{} of {}".format( self.suit,self.value)
   


class Deck(object):
    def __init__(self):
        self.card = []
        self.build()
    
    def build(self):
        for s in ["Spades","Clubs","Diamonds","Hearts"]:
            for v in range(1, 14):
                #self.cards.append(Card(s,v))
                print ("{} of {}".format(v,s))

    # def show(self):
    #     for c in self.cards:
    #         c.show()       

# class Player():
#     def __init__()

# card = Card("Clubs",6) 

# card.show()    
deck = Deck()
