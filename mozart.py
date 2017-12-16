def Artist(first,last,**info):
    profile = {}

    profile["First Name"] = first
    profile["Last Name"] = last

    for key,range in info.items():
        profile[key] = range

    return profile

mozart = Artist("Amadeus","Mozart",Piece = " Lacrimosa") 
beethooven = Artist("Luidwig","Beethoven",Piece = "Moonlight SOnata")

print(mozart)   
print(beethooven)