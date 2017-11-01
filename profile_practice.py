def user(first,mid,last,**info):
    profile = {}

    profile['first name'] = first
    profile['middle name'] = mid
    profile['last name'] = last

    for key, range in info.items():
        profile[key]=range

    return profile


beethoven = user("Ludwig","Van","Beethoven",Country = "Germany",DateofBirth="1770")    

print(beethoven)