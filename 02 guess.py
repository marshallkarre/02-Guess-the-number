#!/Library/Frameworks/Python.framework/Versions/3.6/bin

import sys
import random
assert sys.version_info >= (3,4), "This script requires at least Python 3.4"

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1,20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

for guessesTaken in range(6):
	print('Take a guess')
	guess = input()
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
	print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
	
if guess != number:
	number = str(number)
	print('Nope. The number I was thinking of was ' + number + '.')