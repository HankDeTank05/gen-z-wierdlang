range_min = 1 # inclusive
range_max = 100 # inclusive

my_num = 27 # this is the number they are trying to guess
guess_num = None # they haven't guessed yet

while True:
	guess_numstr = input("Guess a number: ")

	# make sure they typed a number
	if guess_numstr.isdigit():
		# convert to int
		guess_num = int(guess_numstr)
	else:
		print(f"{guess_numstr} is not a number. Guess again.")
		continue

	# make sure their number is in the guessing range
	# check lower bound
	if guess_num < range_min:
		print(f"Your number ({guess_num}) was too small. You may not guess lower than {range_min}. Guess again.")
		continue
	
	# check upper bound
	elif guess_num > range_max:
		print(f"Your number ({guess_num}) was too large. You may not guess higher than {range_max}. Guess again.")
		continue
	
	# check if guess is below my number
	if guess_num < my_num:
		print("Too low. Guess again.")
		continue
	
	# check if guess is above my number
	elif guess_num > my_num:
		print("Too high. Guess again.")
		continue

	else:
		print("Correct! Good guessing!")
		break
