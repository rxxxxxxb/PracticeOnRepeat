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
        for suits in ['Spades','Hearts','CLubs','Diamonds']:
            for value in range(1,14):
                self.cards.append(card(suits,value))
        #52 card build

    def show(self):
        for val in self.cards:
            val.print()
        #show all cards 

    def shuffle(self):
        for i in len(self.cards):
            
        #shuffle cards


    def drawCard(self):
        #pop las card



# class Player():
#      def __init__(self):
          