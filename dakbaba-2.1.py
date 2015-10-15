#!/usr/bin/env python

import os
import sys

sendmail_prog = '/usr/sbin/sendmail'

required_args = set(['to', 'from'])
valid_args = set(['to', 'from', 'subject', 'body'])
args = sys.argv[1:]

#initialize dictionary
argdict = {}

for item in args:
	elements = item.split('=')
	argdict[elements[0]] = elements[1]


#check that required fields are there
missing = required_args.difference(argdict)

if len(missing) > 0:
	print 'ERROR: Info missing. Please try again'
	if 'to' in missing:
		recipient = raw_input('Who will this email be sent to?:' )
		argdict['to'] = recipient
	else:
		sender = raw_input('Who is sending this email?:' )
		argdict['from'] = sender
else:
	print 'Sending message'

#how do I only ask for a certain piece of info?

template = '''From: {0}
To: {1}
subject: {2}'''

header = template.format(argdict['from'],argdict['to'],argdict['subject'])

print header


msg = header + argdict['body']
sendmail = os.popen(sendmail_prog + " -t", "w")
sendmail.write(msg)
sendmail.close()
