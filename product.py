class Product:
    def __init__(self,name,year,type):
        self.name=name
        self.year=year
        self.type = type

    def info(self):
        print("Name : " + self.name +
              " year : " , self.year)

        print("Type : " + self.type )          


coke= Product("coca-cola",2017,'beverage') 

coke.info()       