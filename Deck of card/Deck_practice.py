import random

class Card():
    def __init__(self,number,suits):
        self.suits = suits
        self.number = number

    def print(self):
        print("{} of {}".format(self.number,self.suits))  

class Deck():
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suits in ['spades','hearts','diamonds','clubs']:
            for value in range(1,14):
                self.cards.append(Card(suits,value))
   
        #52 card build

    def show(self):
        for val in self.cards:
            val.print()
        #show all cards 

    def shuffle(self):
        l = len(self.cards)
        for i in range(l):
            r = random.randint(0,i)
            self.cards[i],self.cards[r] = self.cards[r],self.cards[i]
               
        #shuffle cards


    def drawCard(self):
        return self.cards.pop()
        #pop last card


class Player():
    def __init__(self,name):
        self.name = name
        self.hand = []

    def draw(self):
        for card in range(5):
            self.hand.append(deck.drawCard())


    def showHand(self):
        for i in self.hand:
            i.print()




deck = Deck()  
deck.shuffle()

pl1 = Player("pl1")

pl1.draw()   
#deck.shuffle()   
##deck.show()
pl1.showHand()