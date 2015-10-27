#!/usr/bin/env python

import argparse
import os
import time

#The priority levels should probably be converted to an integer scale
class Logger(object):
	def __init__(self, filename, priority, datetime, scriptname):
		parser = argparse.ArgumentParser()

		parser.add_argument('priority',  action ='store',default='DEBUG', help='What priority is this doc?')
		parser.add_argument('datetime', action='store', default='TRUE', help='Do you want to log the date and time?')
		parser.add_argument('scriptname', action='store', default='TRUE', help='Do you want to log the file name?')

		args = parser.parse_args()


		filename = os.path.basename(args[0])
		priority = args[1].upper()
		priorities = {'DEBUG': 1, 'INFO': 2, 'WARNING': 3, 'ERROR': 4, 'CRITICAL': 5}
		priority = int(priorities.get(priority))
		write_date = args[2]
		write_scriptname = args[3]


	#may not need number in write_log
	def debug(self, msg):
		if priority >= 1: 
			self.write_log(msg, 1)
		else:
			print "Can't run"
	def info(self, msg):
		if priority >= 2:
			self.write_log(msg, 2)
		else:
			print "Can't run"
	def warning(self, msg):
		if priority >= 3:
			self.write_log(msg, 3)
		else:
			print "Can't run"
	def error(self, msg):
		if priority >= 4:
			self.write_log(msg, 4)
		else:
			print "Can't run"	
	def critical(self, msg):
		if priority == 5:
			self.write_log(msg, 5)
		else:
			print "Can't run"

	#this will take in the priorities argument, and go from there
	#calls compose_prepend() to retrieve data and/por filename
	#opens the file and write the log line
	def write_log(self, msg, priorities):
		self.compose_prepend()


	#checks the instance to see whether a date and/or filename are desired
	def compose_prepend():
		log_line_spacer = "    "
		#open file
		fh = open(filename, 'w')
		#write msg in file
		if write_date:
			#prepend file with
			time_date =  time.ctime()
			fh.write(time_date + log_line_spacer)
		if write_scriptname:
			#prepend file with
			fh.write(filename + log_line_spacer)
