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
        for suits in ['Spades','Clubs','Diamonds', "Hearts"]:
            for value in range(1,14):
                self.cards.append(Card(suits,value))


    def show(self):
        for val in self.cards:
            val.print()

    def shuffle(self):
        for i in range (len(self.cards)-1,0,-1):
           
            r = random.randint(0,i)
            self.cards[i],self.cards[r] = self.cards[r],self.cards[i]

    def drawCard(self):
        return self.cards.pop()
                         
   
deck = Deck()
deck.show()
print('\n--------\n')
deck.shuffle()
deck.show()


# class Player():
#      def __init__(self):
          