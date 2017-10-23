def user(first,last,**info):
    profile = {}
    profile['first name']=first
    profile['last name'] =last

    for key,range in info.items():
        profile[key]=range

    return profile


justin = user('justin','trudau',
                location = 'Canada',job='Prime mininster')

print(justin)