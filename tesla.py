class Car():
    def __init__(self,brand,year,type):
        self.brand = brand
        self.type = type
        self.year = year


    def printBrand(self):
        print("Car brand : " + self.brand.title())

    def printYear(self):
        print("Year : " + str(self.year) )

    def printType(self):
        print("type of the car : " + self.type.title())   


tesla = Car("Tesla", 2015,"electric") 

tesla.printBrand()       
tesla.printType()
tesla.printYear()