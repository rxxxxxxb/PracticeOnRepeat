# animals = ['cat','dog','bird']
# for index, value in enumerate(animals):
#     print (index, value)


animals = ['cat','dog','bird']
l = len(animals)

for index ,v in enumerate(animals):
    print(animals[index])


#f=animals[0]

print("there are " +str(l)+ " animals")

# for suits in ["Spades","Clubs","Diamonds","Hearts"]:
#     for value in range(1, 15):
#         print(suits,value)
# import random
        
# for index in range((50)-1,0,-1): #is Even
#     print("----",index)
#     r = random.randint(0,index)
#     print(r)        # self.cards[index],self.cards[r] = self.cards[r],self.cards[index]  

disk = ["Spades","Clubs","Diamonds","Hearts"]
index = (index ) % len(disk)
print(index)

def function_that_prints():
    print("I printed")

def function_that_returns():
    return( "I returned")

f1 = function_that_prints()
f2 = function_that_returns()
print("Now let us see what the values of f1 and f2 are")
print(f1)
print(f2)