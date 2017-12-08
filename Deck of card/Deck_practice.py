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
        TotalCard = len(self.cards)
        for length in range(TotalCard):
            rand = random.randint(0,length)
            self.cards[length],self.cards[rand] = self.cards[rand],self.cards[length]

    def show(self):
        for v in self.cards:
            v.show()            

    def drawCard(self):
        return self.cards.pop()    

class Player:
    def __init__(self,name):
        self.name= name
        self.hand = []
        self.size = 0
    
    def draw(self):
        callBridge = range(5)
        for ra in callBridge:
                
            self.hand.append(deck.drawCard())
            self.size += 1

    def showHand(self):
        for v in self.hand:
            v.show()    

    def discard(self):
        return self.hand.pop()        

    def showEmptyHand(self):
        # check = len(self.hand)
        # if check == 0:
        #     print("empty")
        if not self.hand:
            print("empty")    

    def lengthOfHand(self):
        print("Number of card In hand :", self.size)         

# clubs = Card("clubs","8")

# clubs.show()

deck = Deck()
deck.shuffle()
# #deck.show()
# deck.drawCard()
# deck.show()

cartman = Player("Cartman")

# for l in range(10):
cartman.draw()

cartman.showHand()
#cartman.discard()
print("-----")
#cartman.showEmptyHand()
# cartman.showHand()
cartman.lengthOfHand()
