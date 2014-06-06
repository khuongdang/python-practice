from sys import argv
script, username, status = argv
prompt = 'Your answer: '
print "Hi %s, I'm the  %s script " %(username,script
)
print "So your status is %s" %status
print "I will ask you some question"
print "Do you like me %s?" %username
likes = raw_input(prompt)

print "Where do you live %s?" %username
lives = raw_input(prompt)

print "What is your position %s?" %username
position  = raw_input(prompt)
print """So you're said to me %r about liking me, you live in %r. \nYour position is %r and your status is %r
""" %(likes, lives, position, status)