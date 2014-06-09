
# Creating variables for people, cars, and buses
people = 30
cars = 40
buses = 15

# If cars are greater than people, print this statement
if cars > people :
	print "We should take the cars."
	# Else, if cars are less than people
elif cars < people:
	print "We should not take the cars."
# Otherwise
else:
	print "We can't decide"

# If buses are greater than cars
if buses > cars:
	print "That's too many buses."
# Else if buses are less than cars
elif buses < cars:
	print "Maybe we could take the buses."
# Otherwise
else:
	print "We can't decide"

#If people are greater than buses
if people > buses:
	print "Alright, lets just take the buses."
# Otherwise
else:
	print "Fine, lets just stay home then."