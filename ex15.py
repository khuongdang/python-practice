from sys import argv

# red the text file imputed direct from command line
script, filename = argv
txt = open(filename)
print "Here is your file %r" %filename
print txt.read()
txt.close()

# read the text file from input
print "Type the file name again: "
file_again = raw_input("Your file name: ")
txt_again = open(file_again)
print txt_again.read()
txt_again.close()
