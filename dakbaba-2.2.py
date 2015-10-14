#!/usr/bin/env python

fh = 'bitly.tsv'

#A set of unique cities represented in the data, sorted by name
def cities():
	city_set = {}
	
	lines = fh.readlines():
	data_lines = lines[1:]
	
	for line in data_lines:
		elements = line.split('\t')
		city_set.add(elements[3])



	print "This is the list of sorted, unique cities: {}".format(city_set.sort())

#The "top ten" country_code values (use a dictionary sorted by value)
def top_countries():
	country_dict = {}

	for line in open(fh)[1:]:
		data = line.split('\t')

	country_code = data[4]
	if country_code in country_dict:
		country_dict[country_code] += 1
	else:
		country_dict[country_code] = 1

	sorted_countries_by_value = sorted(country_dict, country_dict.get)

	print 'These are the top ten country_code values:{}'.format(country_dict[:9])

#The "top ten" machine_name values (derived from the long_url field)
def machine():
	machine_dict = {}

	for line in open(fh)[1:]:
		data = line.split('\t')

	long_url = data[2]
	machine = long_url.split('/')[2]

	if machine in machine_dict:
		machine_dict[machine] += 1
	else:
		machine_dict[machine] = 1

	sorted_machines_by_value = sorted(machine_dict, machine_dict.get)

	print 'These are the top ten machine values:{}'.format(machine_dict[:9])


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
