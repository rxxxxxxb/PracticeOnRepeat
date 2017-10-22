def create(first,last,**info):
    profile={}

    profile['first name']=first
    profile['last name']=last

    for k,range in info.items():
        profile[k]=range
    return profile

user=create ('Barack','Obama' ,location='washington',profession='president') 


print(user)   