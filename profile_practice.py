def user(first,last,age,**info):
    profile = {}

    profile['first name '] = first
    profile['last name '] = last
    profile['age '] = age
    
    for key,range in info.items():
        profile[key] = range

    return profile

bill = user('Bill','Gates','50',
         location = "california",networth = "60 billion" )    

print(bill)
