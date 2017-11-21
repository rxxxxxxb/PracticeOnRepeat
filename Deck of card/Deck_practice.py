
import random

class Card():
    def __init__(self,card,value):
        self.card = card
        self.value = value

    def show(self):
        print("{} of {}".format(self.value,self.card))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suits in ["Clubs","Hearts","Diamonds","Spades"]:
            for val in range(1,14):
                self.cards.append(Card(suits,val))


  


    def shuffle(self):
        l = len((self.cards))
        for le in range(l):
            r = random.randint(0,le)
            self.cards[le],self.cards[r] = self.cards[r],self.cards[le]



    def show(self):
        for v in self.cards:
            v.show()            


    def drawCard(self):
        return self.cards.pop()    


class Player:
    def __init__(self,name):
        self.name= name
        self.hand = []
        
    
    def draw(self):
        self.hand.append(deck.drawCard())

    def showHand(self):
        for v in self.hand:
            v.show()    



# clubs = Card("clubs","8")

# clubs.show()

deck = Deck()
deck.shuffle()
# #deck.show()
# deck.drawCard()
# deck.show()

cartman = Player("Cartman")


cartman.draw()
cartman.draw()
cartman.showHand()
#cartman.discard()
print("-----")
cartman.showHand()
