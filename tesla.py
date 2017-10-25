class Car():
    def __init__(self,brand,modelName,year,carType,milage):
        self.brand=brand
        self.modelName=modelName
        self.year=year
        self.carType=carType
        self.milage=milage


    def printCarinfo(self):
        print("Car Brand : " + self.brand.title() + "\n"
              "Car Model : " +  self.modelName.title() + "\n"
              "Car Released in :" + str(self.year) + "\n"
         ) 

    def printTechnicalinfo(self):
        print("Car type : "   +  self.carType.title() + "\n"
              "Car milage : " +  self.milage.title() + "\n"
              )         


tesla = Car('Tesla','Model S', 2016,'Electric','250 miles' )

tesla.printCarinfo()    
tesla.printTechnicalinfo()  