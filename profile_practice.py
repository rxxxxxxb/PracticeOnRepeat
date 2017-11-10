def artist(first,last,**info):
    profile = {}

    profile['First name']= first
    profile['last name' ]= last

    for key,range in info.items():
        profile [key] = range

    return profile

mozart = artist("Amadeus","Mozart",location = "Austria",Birth = 1745)

print(mozart)