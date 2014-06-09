from sys import exit

def winners_room():
	"""The room where you are congratulated!"""
	print "A man in a wizard's outfit joins you."
	print "At first, you are startled until you notice his calming aura."
	dead ("He says to you: \"Congratulations! You win.\" Then transports you home.")

def choice_room():
	"""One final choice for the winner. Will it be left or right??"""

	print "Again, youre in a dark room. There's a door to your right, and to your left."
	print "Which door will you take?"

	next = raw_input("> ")

	if next == "left":
		dead("You open the door and are immediately sucked into the void.")
	elif next == "right":
		winners_room()
	else:
		print "Dude, you've come this far, and now you wanna do this?"


def gold_room():
	"""This is the gold room. It asks you how much money you want to take."""
	print "This room is full of gold. How much do you take?"

	next = raw_input(">")
	if next.isdigit():
		how_much = int(next)
	else:
		dead("Man, learn to type a number...")


	if how_much <= 50:
		print "Nice, you're not greedy. You win!"
		exit(0)
	else:
		dead("You greedy bastard!")


def bear_room():
	"""The bear in the room needs to be moved before you can go through the door."""
	print "There is a bear in here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		next = raw_input("> ")

		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chomps your legs clean off.")
		elif next == "open door" and bear_moved:
			gold_room()
		elif next == "eat bear":
			print "Are you serious??"
		elif next == "what?":
			bear_room()
		else:
			print "I got no idea what that means. Try to speak in simple terms - This is a simple program."


def cthulhu_room():
	"""The great and evil cthulhu lives here. I don't think you want to be here too long..."""
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever... stares at you and you go insane."
	print "Do you flee for your life or eat your head?"

	next = raw_input("> ")

	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	elif "what?" in next:
		dead("Cthulhu wastes no time while you dilly-dally and eats you.")
	else:
		cthulhu_room()


def dead(why):
	"""Upon death, this function gets called to end game."""
	print why, "Good job!"
	exit(0)


def start():
	"""This is where the player starts."""
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"

	next = raw_input("> ")

	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")


start()
"""Call the start function, cuz it wont do it by it's self."""