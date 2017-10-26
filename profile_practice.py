def user(first,last,**info):
    profile = {}

    profile['first name'] = first
    profile['last name'] = last

    for key,range in info.items():
        profile[key] = range

    return profile


bezos = user('Jeff','Bezos',location = 'california',networth='50 Billion',job='Amazon ceo')

print(bezos)    