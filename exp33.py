def number_loop(number, inn):
	i = 0
	numbers = []

	while i < number:
		print "At the top i is %d" % i
		numbers.append(i)
		i = i + inn

		print "Numbers now: ", numbers
		print "At the bottom of i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num


number_loop(10, 100)