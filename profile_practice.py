def user(first,last,**info):
    profile = {}

    profile['first name'] = first
    profile['last name'] = last

    for key,range in info.items():
        profile[key] = range

    return profile

mozart = user("Wolagang amadeus \n","Mozart\n",place = "Austria/n",Birthyear = "1756/n")    

print(mozart)