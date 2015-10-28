#!/usr/bin/env python

import sys
import os
import time


#The priority levels should probably be converted to an integer scale
class Logger(object):
	def __init__(self, filename, priority, datetime, scriptname):
		self.filename = filename
		self.priority = priority
		self.datetime = datetime
		self.scriptname = scriptname

	#may not need number in write_log
	def debug(self, msg):
		if self.priority >= 1: 
			self.write_log(msg, 1)
		else:
			print ("Can't run")
	def info(self, msg):
		if self.priority >= 2:
			self.write_log(msg, 2)
		else:
			print ("Can't run")
	def warning(self, msg):
		if self.priority >= 3:
			self.write_log(msg, 3)
		else:
			print ("Can't run")
	def error(self, msg):
		if self.priority >= 4:
			self.write_log(msg, 4)
		else:
			print ("Can't run")	
	def critical(self, msg):
		if self.priority == 5:
			self.write_log(msg, 5)
		else:
			print ("Can't run")

	#this will take in the priorities argument, and go from there
	#calls compose_prepend() to retrieve data and/por filename
	#opens the file and write the log line
	def write_log(self, msg, priorities):
		self.compose_prepend


	#checks the instance to see whether a date and/or filename are desired
	def compose_prepend():
		log_line_spacer = "    "
		#open file
		fh = open(self.filename, 'w')
		#write msg in file
		if self.datetime:
			#prepend file with
			time_date =  time.ctime()
			fh.write(time_date + log_line_spacer)
		if self.scriptname:
			#prepend file with
			fh.write(self.filename + log_line_spacer)
		fh.close()