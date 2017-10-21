class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(self.name.title() + ' is now sitting down')

    def roll(self):
        print(self.name.title()+ ' has rolled over')

mydog = Dog('Alex',8)

mydog.sit()
mydog.roll()
print('Age is '+ str(mydog.age) )                
