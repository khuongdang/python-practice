def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(26, 2)
height = subtract(78, 4)
weight = multiply(95, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "here is a puzzle:"

what = multiply(age, add(height, divide(weight, multiply(iq, 2))))

what2 = age * (height + (weight / (iq * 2)) ) 

print "That becomes: ", what, "Can you do it by hand?"
print "And by using a different formula, hopefully we can come up with the same answer:"
print "Is it?: %d" % (what2)