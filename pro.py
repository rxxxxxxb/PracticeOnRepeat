def create_user(f,l,**u_i):
    profile ={}
    profile["frist"]=f
    profile['last'] =l
    for key,range in u_i.items():
        profile[key]=range
    
    return profile

run= create_user("vald", 'putin',
                  location='russia',job='president')

print(run)                  


