stuff = ['Test', 'This', 'Out']
print ' '.join(stuff)

class TheThing(object):

	def __init__(self):
		# After initialialization, self.number becomes 0
		self.number = 0

	def some_function(self):
		# Simple function that prints a string
		print "I got called."

	def add_me_up(self, more):
		# takes self.number (0) and adds more (20 in object a, 30 in object b)
		# returns the sum of self.number and more.
		self.number += more
		return self.number

# two different things. Why? Because b is a different object than a.
# Im sure of it.
a = TheThing()
b = TheThing()

# This will call some_function and print "I got called" for both object a & b
print "This is a.some_function():"
a.some_function()
print "\n"
print "This is b.some_function():"
b.some_function()
print "\n"

# Object a calls add_me_up() function/method which does this:
# 0 + 20 (self.number + more)
print "This is a.add_me_up(20):"
print a.add_me_up(20)
print "\n"
print "This is b.add_me_up(30):"
print b.add_me_up(30)
print "\n"

# Because a.number is in the same scope of the class,
# you can call it and it will still be 20 for object a,
# and 30 for object b.
print "This is a.number:"
print a.number
print "\n"
print "This is b.number:"
print b.number
print "\n"

# Study this. This is how you pass a variable
# from one class to another. You will need this.
class TheMultiplier(object):

	# Takes the value of base and it becomes self.base
	# In this case, it would be a.number - 20
	def __init__(self, base):
		self.base = base

	# This takes the value of m - b.number (30)
	# and multiplies it by the base number - a.number (20)
	# returns 600 (30 * 20)
	def do_it(self, m):
		return m * self.base

x = TheMultiplier(a.number) # a.number = base
print x.do_it(b.number) # b.number = m