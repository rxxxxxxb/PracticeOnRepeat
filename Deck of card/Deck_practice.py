class Card():
    def __init__(self,value,suits):
        self.value = value
        self.suits = suits

    def show(self):
        print("{} of {}".format(self.value,self.suits) )    

hearts = Card("King","Hearts")

hearts.show()

# class Deck():
#      def __init__(self):
   



# class Player():
#      def __init__(self):
          