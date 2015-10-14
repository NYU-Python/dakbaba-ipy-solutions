import os
import sys

sendmail_prog = '/usr/sbin/sendmail'

required_args = set(['to', 'from'])
valid_args = set(['to', 'from', 'subject', 'body'])
args = sys.argv[1:]

#initialize dictionary
argdict = {}
#split the inputs given that '=' is used
key, val = arg.split('=')
#set the key
argdict[key] = val

#check that required fields are there
missing = required_args.difference(argdict)
print 'ERROR: {} missing. Please try again'.format(missing)

#how do I only ask for a certain piece of info?

template = '''From: {0}
To: {1}
subject: {2}'''

header = template.format(argdict['from'],argdict['to'],argdict['subject'])

msg = header + argdict['body']
sendmail = os.popen(sendmail_prog + " -t", "w")
sendmail.write(msg)
sendmail.close(
