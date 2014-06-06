from sys import argv
script, first, second, third = argv
print "the script is called", script
print "the first variable is ", first
print "the second is called", second
print "the third is called", third

# run the command line : python ex13.py Kent Quang Hien

#Combine raw_input with argv to make a script that gets more input from a user.
your_name = raw_input("What's your name ")
your_position = raw_input("What is your position? ")

print "Your name is  %r and your position is  %r." % (your_name, your_position)