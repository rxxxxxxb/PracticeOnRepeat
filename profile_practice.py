def writer(first,last,**info):
    profile = {}

    profile['First name'] = first
    profile['last name'] = last

    for key, range in info.items():
        profile[key]=range

    return profile

malcolm = writer('Malcolm','Gladwell',location ='Canada',book='David and Goliath',published = '2013')

print(malcolm)
