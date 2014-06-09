# Dictionary
cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

cities ['NY'] = 'New York'
cities ['OR'] = 'Portland'
cities ['VN'] = 'Vietnam'

def find_city(city_name, abbrev):
	""" Check the abbrev of the city"""
	if abbrev in city_name:
	# if has return item
		return city_name[abbrev]
	else:
	# if not , return "not found"
		return "Not Found."


while True:
	print "The abbrev of the city? (ENTER to quit)",
	abbrev = raw_input("> ")

	# if not found : return
	if not abbrev: break

    #run functions and return abbrev if exist and not found if not exist
	city_found = find_city(cities, abbrev)
	print city_found