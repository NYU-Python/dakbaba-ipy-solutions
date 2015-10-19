#!/usr/bin/env python
import sys


fh = open('bitly.tsv')
list_of_valid_args = ['timestamp', 'short_url_cname', 'long_url', 'geo_city_name','country_code','geo_region','timezone','lat','longitude'] 


filename, number, inner, outer = sys.argv

#validate arguments
def validate(number, inner, outer):
	number = int(number)
	if inner in list_of_valid_args:
		print 'Valid Inner Argument'
	else:
		print 'Please try again. Valid arguments include {}'.format(list_of_valid_args)
	if outer in list_of_valid_args:
		print 'Valid Outer Argument'
	else:
		print 'Please try again. Valid arguments include {}'.format(list_of_valid_args)

#create function that takes user input sorts through data to create dictionary of dictionary
"""
For "5 most popular platforms by country_code". 

OUTER: is the "by" field (in this example, country_code)

INNER: other field (in this example, platform).  

"""
def dict_of_dict(inner, outer, value):
	outer_dict = {}
	index_dic = {}
	i = 0

	lines = fh.readlines()
	data_lines = lines[1:]

	for el in lines[0].split('\t'):
		index_dic[el] = i
		i += 1	

	inner_key = index_dic[inner]
	outer_key = index_dic[outer]
	print inner_key
	print outer_key


	for line in data_lines:
		timestamp, short_url_cname, long_url, geo_city_name,country_code,geo_region,timezone,lat,longitude = line.split('\t')

		outer_dict[outer_key][inner_key] = 0

		if outer_key not in outer_dict:
			outer_dict[outer_key] += 1
			outer_dict[outer_key][inner_key] += 1
		else:
			if inner_key not in outer_dict[outer_key][inner_key]:
				outer_dict[outer_key][inner_key] = 1
			else:
				outer_dict[outer_key][inner_key] += 1
	
	for innerdict in outer_dict:
		for key in innerdict:
			innerdict = sorted(innerdict, key=innerdict.get)

	printed_values = outer_dict[:value + 1]

	print 'Here is what you asked for: {}',format(printed_values)

####################
#now time for fun
####################

validate(number, inner, outer)
dict_of_dict(inner, outer, number)
