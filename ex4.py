#define car number
cars = 100
#define pace in car
space_in_car = 4.0
#define drivers 
drivers = 30
#define passengers 
passengers = 90
#define car not driven
cars_not_driven = cars - drivers
#define cars driven
cars_driven = drivers
#define carpool_capacity
carpool_capacity = cars_driven * passengers
#define average passengers per car
average_passengers_per_car = passengers / cars_driven

#show the numbers of car
print "There are", cars, "cars available"
#show the driver number
print "There are only", drivers, "drivers available"
#show the cars not driven
print "There will be", cars_not_driven, "empty cars today."
#show the capacity of car
print "We can transport", carpool_capacity, "people today."
#show the passenger number
print "We have", passengers, "to carpool today."
#show the average passenger per car
print "We need to put about", average_passengers_per_car, "in each car."





