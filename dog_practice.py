class Car():
    def __init__(self,brand,year,engine):
        self.brand = brand
        self.year = year
        self.engine = engine

    def printBrand(self):
        print('brand of the car ' + self.brand.title() )

    def printYear(self):
        print ('Car made in ' + str(self.year))

    def printEngine(self):
        print('engine of the car ' + self.engine.title() )    
        
ford = Car("Ford",2010,"V8")

ford.printBrand()
ford.printYear()
ford.printEngine()