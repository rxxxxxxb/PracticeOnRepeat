tenThings = "Apples Oranges Crows Telephone Light Sugar"
print(tenThings)

print("Need more items")

stuff = tenThings.split(" ")

more = ["Day","night","Song","Frisbee","Corn","Banana"]

while len(stuff) != 10:
    nextOne = more.pop()
    print("Adding", nextOne)
    stuff.append(next)
    print("Items no %d " % len(stuff))

print("Done")

print(stuff[1])
print(stuff[-1])

print(stuff.pop())

print(' '.join(stuff))
print('#'.join(stuff[3:5]))

