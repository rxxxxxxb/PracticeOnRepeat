def profile(first,last,**info):
    user = {}

    user['First name'] = first
    user['last name'] = last

    for key,range in info.items():
        user[key] = range
        print(key,range)
    

    return user

rkib = profile("rkib","rkb",DOB = '1992',UNI = "AIUB")

print(rkib)    


