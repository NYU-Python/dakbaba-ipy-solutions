#!/usr/bin/env python


fh = open('bitly.tsv')

#A set of unique cities represented in the data, sorted by name
def cities():
	city_set = set([])
	
	lines = fh.readlines()
	data_lines = lines[1:]
	
	for line in data_lines:
		elements = line.split('\t')
		city_set.add(elements[3])

	sorted_cities = sorted(list(city_set))

	print "This is the list of sorted, unique cities: {}"
	print sorted_cities

#The "top ten" country_code values (use a dictionary sorted by value)
def top_countries():
	country_dict = {}
	
	lines = fh.readlines()
	data_lines = lines[1:]


	for line in data_lines:
		data = line.split('\t')
		country_code = data[4]
		country_dict[country_code] = 0
		if country_code in country_dict:
			country_dict[country_code] += 1
		else:
			country_dict[country_code] = 1

	country_dict = sorted(country_dict, key=country_dict.get)

	printed_values = list(country_dict)[:9]

	print 'These are the top ten country_code values:{}'.format(printed_values)

#The "top ten" machine_name values (derived from the long_url field)
def machine():
	machine_dict = {}

	lines = fh.readlines()
	data_lines = lines[1:]

	for line in data_lines:
		data = line.split('\t')

		long_url = data[2]
		machine = long_url.split('/')[2]

		machine_dict[machine] = 0

		if machine in machine_dict:
			machine_dict[machine] += 1
		else:
			machine_dict[machine] = 1

	machine_dict = sorted(machine_dict, key = machine_dict.get)

	printed_values = list(machine_dict)[:9] 

	print 'These are the top ten machine values: {}'.format(printed_values)


####################
#now time for fun
####################
print "Please tell me if you'd like to see info about cities, countries, or machines"
answer = raw_input(' ')

if answer == 'cities':
	cities()
elif answer == 'countries':
	top_countries()
elif answer == 'machines':
	machine()
else:
	print 'Sorry, could not compute'
