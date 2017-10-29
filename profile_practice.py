def user(first,middle,last,**info):
    profile = {}

    profile['First name'] = first
    profile['middle name'] = middle
    profile['Last name'] = last

    for key,range in info.items():
        profile[key] = range

    return profile

mozart = user("wolfgang",'amadeus','mozart',location='Austria',DOB='1756')

print(mozart)    
    
    