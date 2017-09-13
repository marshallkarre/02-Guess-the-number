#!/Library/Frameworks/Python.framework/Versions/3.6/bin

import sys
import random
assert sys.version_info >= (3,4), "This script requires at least Python 3.4"

guessesMade = 0
maxGuesses = 5
numRange = 15

insertname = input('Karre ')

number = random.randint(1,numRange)
print('Hello, ' + insertname + '! I am thinking of a number between 1 and ' + str(numRange) + '.')

for guessesMade in range(maxGuesses):
	guess = input ('Can you guess what it is?')
	try:

		guess = int(guess)


		if guess < number:
			print('Too low!')

		if guess > number:
			print('Too high!')

		if guess == number:
			break


	except ValueError:
		print('Please enter a whole number.')

if guess == number:
	guessesMade = str(guessesMade + 1)
	print('Excellent work, ' + insertname + '! You read my mind in ' + guessesMade + 'guesses!')

if guess != number:
	number = str(number)
	print('Sorry. The number I was looking for was ' + number + '.')
