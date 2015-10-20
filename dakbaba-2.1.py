#!/usr/bin/env python

import os
import sys

sendmail_prog = '/usr/sbin/sendmail'

required_args = set(['to', 'from'])
valid_args = set(['to', 'from', 'subject', 'body'])
args = sys.argv[1:]

#initialize dictionary
argdict = {}

#create dictionary
for item in args:
	elements = item.split('=')
	argdict[elements[0]] = elements[1]


#check to see that entered fields are valid
entered_args = set([argdict.keys()])
if valid_args.issuperset(entered_args):
	print 'Valid arguments!"
else:
	sys.exit('ERROR: Info missing. Please try again')

#check that required fields are there
missing_required_args = required_args.difference(argdict)
if len(missing) > 0:
	sys.exit('ERROR: Info missing. Please try again')

template = '''From: {0}
To: {1}
subject: {2}'''

header = template.format(argdict['from'],argdict['to'],argdict['subject'])

print header


msg = header + argdict['body']
sendmail = os.popen(sendmail_prog + " -t", "w")
sendmail.write(msg)
sendmail.close()
