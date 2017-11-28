def user(first,last,**info):
    profile = {}

    profile["FIrst name"] = first
    profile["Last name "] = last

    for key,range in info.items():
        profile[key] = range

    return profile

dawking = user("Richard","Dawking",Book ="God Delusion") 

print(dawking)   

