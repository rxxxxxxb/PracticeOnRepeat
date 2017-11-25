things = "HARAMBE, he was not just a gorilla."

more = "Rest in peace sweet Prince."

thingsArray = things.split(' ')
moreArray = more.split(' ')

moreArray.reverse() # Revesred it to make both sentences sensible

print(thingsArray)
print("Reversed : ",moreArray)

while len(thingsArray) != 12:
    next = moreArray.pop()
    print("more :",next)
    thingsArray.append(next)
    print("length of things %d " %len(thingsArray) )

#next = thingsArray[1:]


print(thingsArray)
for value in enumerate(thingsArray,1):
    print(value)
#print(thingsArray.pop())

print(' '.join(thingsArray))
print(' # '.join(thingsArray[2:5]))