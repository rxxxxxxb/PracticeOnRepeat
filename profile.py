def user_profile(first,last, **user_info):
    profile = {}
    profile["first_name"]=first
    profile['last_name'] =last

    for key,range in user_info.items():
        profile[key]= range

    return profile

create_user = user_profile('albert','einstein',
                           location="princeton",field='physics')
print(create_user)
