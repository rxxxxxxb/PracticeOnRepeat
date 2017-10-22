class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def name_(self):
        print("Name of the dog is " + self.name.title() ) 

    def age_(self):
        print("age of the dog " + str(self.age))

mydog=Dog('alfred',8)

 
mydog.name_()
mydog.age_()               