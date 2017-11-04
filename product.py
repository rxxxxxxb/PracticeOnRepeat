class Bottle():
    def __init__(self,brand,name,size):
        self.brand = brand
        self.size = size
        self.name= name

    def info(self):
        print("Brand name : " + self.brand.title() +
              "Size : " + self.size.title() +
              "Name : " + self.name.title() )    


Coke = Bottle("COca COla","DIet","2.5 Litre")

Coke.info()