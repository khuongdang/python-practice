from sys import argv
script, filename = argv

print "We are going to erase %r" % filename
print " if you don't want that you can use CTRL + C \n"
print "If you want that jut hit RETURN \n"
raw_input("?")

#open file
print ("Opening the file...")
target = open(filename, 'w')

#truncate file

print("Truncating the file, Good bye!")
target.truncate()

print("Now we're going to create and add the file content")

line1 = raw_input("Line1: ")
line2 = raw_input("Line2: ")

print("Now we're writing these line to the file")

target.write(line1)
target.write("\n")
target.write(line2)

print ("Finally we have the new file with new content! Then we will close it!")

target.close()








