#!/usr/bin/env python

print "I will try to guess what you are thinking!"
raw_input("Think of a number between 0 and 100, and I will try to guess it. Hit [enter] to start")


counter = 0
guess = 50
upper = 100
lower = 0
guess_temp = 50

while counter < 10:
	answer = raw_input("Is it %d (yes/no/quit)?" % guess)
	if answer == 'yes':
		print "Told you I was a mind reader!"
		counter = 11
	elif answer == 'no':
		second_answer = raw_input("Is it higher or lower?")
		if second_answer == 'higher':
			guess_temp = guess
			guess = (upper - guess)/2 + guess
			lower = guess_temp
		else:
			guess_temp = guess
			guess = guess - (guess - lower)/2 
			upper = guess_temp
		counter =+ 1
	else:
		counter = 11
		print "Thanks for playing!"
