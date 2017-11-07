class Product():
    def __init__(self,name,brand,type,price):
        self.name = name
        self.brand = brand
        self.type = type
        self.price = price

    def productInfo(self):
        print(" Brand name :" ,self.brand )
        print(" Product name :" ,self.name )
        print(" Type :" ,self.type )
        print('Price :' + self.price)

    def PrintPrice(self):
        print('Price :' + self.price)
        


coke = Product("Coke","Coca-Cola",'Beverage',"50 bdt") 
           
coke.productInfo()           
coke.PrintPrice()