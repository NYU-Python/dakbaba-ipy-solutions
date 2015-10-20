#!/usr/bin/env python

import argparse
import os
import time

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--dir',  default='.', help='What directory do you want to explore?')
parser.add_argument('--by', action='store', choices=['size', 'mtime', 'name'], default='name', help='Pick by what youd like to sort: size, mtime, or name')
parser.add_argument('--results', action='store', type=int, default=10, help='How many options do you want to see?')
parser.add_argument('--direction', action='store', choices=['ascending','descending'], default='descending', help='How would you like to see the results: ascending or descending?')

args = parser.parse_args()

this_dir = args.dir
filedic = {}
filelist = []


if args.dir == '.':
	this_dir = os.getcwd()
else:
    this_dir = args.dir

try:
   fh = open(this_dir)
except IOError:
   print 'The directory {} does not exist'.format(this_dir)
   exit()

def create_dict(directory):
	for listing in os.listdir(this_dir):
	    filepath = os.path.join(this_dir, listing)
	    if os.path.isfile(filepath):
	        moddate = time.ctime(os.path.getmtime(filepath))
	        filelen = os.path.getsize(filepath)
	        filename = os.path.basename(filepath)
	    filedic[filename]={'filesize':filelen, 'filedate':moddate}


def create_list(dictionary):
	for fn in dictionary:
		filelist.append(fn,dictionary[fn])

def sorting(by, how, howmany):
	if how == 'ascending':
		filelist.sort(key=lambda e: e[1][by])
	else:
		filelist.sort(key=lambda e: e[1][by], reverse=True)
	print filelist[:howmany+1]


####################################
#run code
####################################

create_dict(this_dir)
create_list(filedic)
sorting(args.by, args.direction, args.results)
