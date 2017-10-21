def user(first,last,**info):
    profile = {}
    profile['first name']=first
    profile['last name']= last

    for key,range in info.items():
        profile[key]=range
    return profile

Obama = user('Barack','Obama',
             Job='President',location='Washington DC')

print(Obama)                 