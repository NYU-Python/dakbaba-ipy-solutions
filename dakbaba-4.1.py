#!/usr/bin/env python

import sys
import argparse
import os
import time

parser = argparse.ArgumentParser("Please list the file you would like to open, the priority level, whether you want a timestamp and filename on new text")
parser.add_argument('--filename', action ='store', help='What file would you like to log too?')
parser.add_argument('--priority',  action ='store',choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], default='DEBUG', help='What priority is this doc?')
parser.add_argument('--datetime', action='store', default='TRUE', help='Do you want to log the date and time?')
parser.add_argument('--scriptname', action='store', default='TRUE', help='Do you want to log the file name?')

args = parser.parse_args()

filename = args.filename
priority = args.priority
priorities = {'DEBUG': 1, 'INFO': 2, 'WARNING': 3, 'ERROR': 4, 'CRITICAL': 5}
priority = int(priorities.get(priority))
datetime = args.datetime
scriptname = args.scriptname

from mylib import Logger 

mylog = Logger(filename, priority, datetime, scriptname)

mylog.debug('will log if priority is DEBUG only')
mylog.info('will log if priority is INFO or DEBUG')
mylog.warning('will log if priority is INFO,DEBUG,WARNING')
mylog.error('will log if priority is INFO,DEBUG,WARNING,ERROR')
mylog.critical('will log in any case')
