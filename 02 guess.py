#!/Library/Frameworks/Python.framework/Versions/3.6/bin

import sys
import random
assert sys.version_info >= (3,4), "This script requires at least Python 3.4"

guessesTaken = 0
maxGuesses = 6
numRange = 20

myName = input('Hi! What is your name? ')

number = random.randint(1,numRange)
print('Greetings, ' + myName + '! I am thinking of a number between 1 and ' + str(numRange) + '.')

for guessesTaken in range(maxGuesses):
	guess = input('Try to guess the number: ')
	try:
		guess = int(guess)
		
		if guess < number:
			print('Your guess is too low.')
		
		if guess > number:
			print('Your guess is too high.')
		
		if guess == number:
			break
	except ValueError:
		print('Please enter a number.')
		
if guess == number:
	guessesTaken = str(guessesTaken + 1)
	print('Good job, ' + myName + '! You guessed the number in ' + guessesTaken + ' guesses!')
	
if guess != number:
	number = str(number)
	print('Sorry. The number I was thinking of was ' + number + '.')