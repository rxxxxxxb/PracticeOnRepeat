class Product:
    def __init__(self,Brand,Line,nam):
        self.Brand = Brand
        self.Line = Line
        self.name = nam
        # self.price = price

    def info(self):
        print("Brand : " + self.Brand)    
        print("Line : " + self.Line)
        print("name : " + self.name)

        print("Price : " + self.price)

Coke = Product("COca Cola","Beverage","DIet Coke")

Coke.price = "220 bdt"

Coke.info()
