
from sys import argv

script, input_file = argv

# create a function named print_all
def print_all(f):
# read the file 
	print f.read()

# create  function rewind with variable-f as the argument
def rewind(f):
# seek the first character
	f.seek(0)

# create a function called print_a_line with two arguments: line_count and f
def print_a_line(line_count, f):
	print line_count, f.readline()

# Open the file	
current_file = open(input_file)

print "First lets print the whole file:\n"

# Call print_all function
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# Call rewind function 
rewind(current_file)

print "Let's print three lines:"

# adds 1 to the variable current_line
current_line = 1
# Call print_a_line function 
print_a_line(current_line, current_file)

# add 1 more to current line (total: 2)
current_line += 1
# Again, call function. Same variables serve as the functions arguments
print_a_line(current_line, current_file)

# add 1 more to current line (total: 3)
current_line += 1
#call function. Same variables serve as function's arguments.
print_a_line(current_line, current_file)