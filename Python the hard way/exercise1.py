cars = 100
space_in_car = 4.0
drivers = 30
passengers = 4
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven


print("there are",cars,"Cars available")
print("there are only ",drivers,"drivers available")
print("there will be",cars_not_driven,"empty cars today")
print("we can transport",carpool_capacity,"people today")
print("WE have",passengers,"to carpool today")
print("We need to put aboput",average_passengers_per_car,"in each car")