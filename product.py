class Product():
    def __init__(self,name,type,weight,country):
        self.name = name
        self.type = type
        self.weight = weight
        self.country = country

    def ProductInfo(self):
        print("Name : " + self.name.title() )
        print("type : " + self.type.title() )
        print("weight : " + self.weight.title() )
        print("country : " + self.country.title() )

coke = Product('coca-cola','Beverage',' 1.5 litre','Bangladesh')

coke.ProductInfo()
