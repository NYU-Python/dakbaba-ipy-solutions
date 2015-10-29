#!/usr/bin/env python

import sys, os, time


#The priority levels should probably be converted to an integer scale
class Logger(object):
	def __init__(self, filename, priority, datetime, scriptname):
		self.filename = filename
		self.priority = priority
		self.datetime = datetime
		self.scriptname = scriptname

	#may not need number in write_log
	def debug(self, msg):
		self.write_log(msg, 1)
	def info(self, msg):
		self.write_log(msg, 2)
	def warning(self, msg):
		self.write_log(msg, 3)
	def error(self, msg):
		self.write_log(msg, 4)
	def critical(self, msg):
		self.write_log(msg, 5)

	#this will take in the priorities argument, and go from there
	#calls compose_prepend() to retrieve data and/por filename
	#opens the file and write the log line
	def write_log(self, msg, priority):
		if self.priority <= priority:
			self.compose_prepend(msg)
		else:
			print ("Can't run")


	#checks the instance to see whether a date and/or filename are desired
	def compose_prepend(self, msg):
		log_line_spacer = "    "
		#open file
		fh = open(self.filename, 'wb')
		#write msg in file
		if self.datetime:
			#prepend file with
			time_date =  time.ctime().encode()
			fh.write(time_date + log_line_spacer.encode())
		if self.scriptname:
			#prepend file with
			fh.write(self.filename.encode() + log_line_spacer.encode())
		fh.write(msg.encode())
		
		fh.close()
