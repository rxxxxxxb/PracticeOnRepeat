def Artist(first,mid,last,**info):
    profile = {}

    profile['First name']  = first
    profile['Middle name'] = mid
    profile['Last name']   = last
    
    for key,range in info.items():
        profile[key] = range

    return range

mozart = Artist('Wolfgang','Amadeus','Mozart',
                Location = 'Austria' , BirthYear = 1745)    


#create composed music function

print(mozart)
