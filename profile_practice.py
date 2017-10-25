def user(first,last,**info):
    profile= {}

    profile['first name']=first
    profile['last name'] =last

    for key,range in info.items():
        profile[key]=range

    return profile    

elon = user('Elon','Musk',location = "california",job="changing humanity")

print(elon)