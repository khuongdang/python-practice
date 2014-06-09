# defines the function cheese_and_crackers with its argument variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# displays how many cheeses 
	#  string formatter %d 
	print "You have %d cheeses!" % cheese_count
	# displays how many boxes of crackers one 
	#  string formatter %d
	print "You have %d boxes of crackers!" % boxes_of_crackers
	# print 
	print "Man, that's enough for a party!"
	print "Get a blanket.\n"



print "We can just give the function numbers directly."
# calls the function with cheese_count  20, boxes_of_crackers  30
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
# a variable holding the number 10
amount_of_cheese = 10
# another variable holding the number 50
amount_of_crackers = 50

# calls the function with the variable above
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
# Calls the function and does the math for each argument variable
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"

# Adds 100 to amount_of_cheese variable which was set at 10
# And adds 1000 to amount_of_crackers which was set at 50.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)