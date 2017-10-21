class Dog():
    def __init__(self, name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(self.name.title() + "is now sitting")

    def roll_over(self):
        print(self.name.title() + "rolled over ")   

dog=Dog('lol',8)

print("Name is " + dog.name.title() + " and  " + dog.name.title() + " is now sitting")
print("Age is " + str(dog.age) + " and  " + dog.name.title() + " is now sitting")             