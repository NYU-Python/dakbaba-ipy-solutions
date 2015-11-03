#!/usr/bin/env python

import sys, os


#Create a class PersistDict that inherits from dict and provides a persistent dictionary
class PersistDict(dict):
	#opens the supplied file and, if it exists, reads the keys and values in the file into the dictionary
	def __init__(self, filename):
		mydict = {}
		with open(filename) as fh:
			for line in fh:
				if line:
					key, value = line.split('=', 1)
					mydict.__setitem__(key, value)
					print (mydict)
				else:
					print ('Dictionary does not exist in {}'.format(filename))

	#sets the key and value in the dictionary, then writes the entire dictionary to the file	
	def __setitem__(self, key, value):
		mydict = dict.__setitem__(self, key, value)
		mydict.write_file()

	#removes the key/value pair from the dictionary, then writes the entire dict to the fle
	def __delitem__(self, key):
		mydict = dict.__delitem__(self, key)
		mydict.write_file()

	#empties the entire dictionary, then writes the entire dict to the file
	def clear(self):
		mydict = {}
		mydict.write_file()

	#performs the customary dict.__setdefault__ behavior, then writes the entire dict to the file 
	def setdefault(self, key, value):
		mydict = dict.__setdefault__(self, key, value)
		mydict.write_file()


	#performs the customary dict.update() behavior, then writes the entire dict to the file
	def update(self, newdict):
		mydict = dict.update(self, newdict)
		mydict.write_file()

	#simply writes the entire dictionary to the file. This is an internal method that is called by all of the above methods 
	def write_file(self):
		with open(filename) as fh:
			for line in fh:
				fh.write(mydict + '\n')
		fh.close()
