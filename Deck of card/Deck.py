import random

class Card(object): # card Object Super Class 
    def __init__(self,suit,val):
        self.suit = suit
        self.value = val

    def show(self):
        print ("{} of {}".format( self.suit,self.value)) # printing card and number
   

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suits in ["Spades","Clubs","Diamonds","Hearts"]:
            for value in range(1, 14):
                self.cards.append(Card(suits,value))
                #print ("{} of {}".format(v,s))

    def show(self):
        for v in self.cards:
            v.show()


    def shuffle(self):
        for length in range(len(self.cards)-1,0,-1):
            #print(i)
            r = random.randint(0,length)
            self.cards[length],self.cards[r] = self.cards[r],self.cards[length]  

    def drawCard(self):
        return self.cards.pop()          

class Player():
    def __init__(self,name):
        self.name = name
        self.hand = []

    def draw(self,deck):
        self.hand.append(deck.drawCard()) 
        #return self  

    def showHand(self):
        for card in self.hand:
            card.show()  

    def discard(self):
        return self.hand.pop()           



deck = Deck()
deck.shuffle()
#card = deck.draw()
#card.show()

lol = Player("lol")

for num in range(5):
    lol.draw(deck)
    
#lol.draw(deck).draw(deck)
lol.showHand()
print('--------')
lol.discard()
lol.discard()
lol.discard()
# deck.show()
print('-------')
lol.showHand()