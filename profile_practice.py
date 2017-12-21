def user(first,last,**info):
    profile = {}

    profile["First name"] = first
    profile["Last name"] = last

    for key,range in info.items():
        profile[key] = range

    return profile

dawking = user("Richard","Dawking",book ="God Delusion") 
harris = user("Sam","Harris",book = "Waking Up")
yuval = user("Yuval","Noah Harrari", book = "Sapiens, Homo Deus")

print(dawking)   
print(harris)
print(yuval)

writersInfo = [dawking,harris,yuval]

# Books = [book["book"] for book in writersInfo]
# print("All the book" ,Books)

writers = [writer["First name" and "Last name"] for writer in writersInfo]
print(writers)

#students = [student["mark"] for student in collection.find({}) if student["mark"] == 900]
