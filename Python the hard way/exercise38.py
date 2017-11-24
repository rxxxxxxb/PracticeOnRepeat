tenThings = "Apples Oranges Crows Telephone Light Sugar"
print(tenThings)

print("Need more items")

stuff = tenThings.split(" ")

more = ["Day","night","Song","Frisbee","Corn","Banana"]


print(stuff)

# for stuff in more: #code doesnt work whren this line run.
#     print(stuff)

while len(stuff) != 10:
    nextOne = more.pop()
    print("Adding", nextOne)
    stuff.append(nextOne)
    print("Items no %d " % len(stuff))

print("Done")

print(stuff[1]) #Print the first element 

print(stuff[-1]) #Counts array from end point and works like pop() 
  

print(stuff.pop())

print(' '.join(stuff))
print('#'.join(stuff[2:5]))

