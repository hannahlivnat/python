import random
random_number = random.randint(1,10) #numbers 1-10
user_guess = 0

print("I'm thinking of a number between 1 and 10...")

#if guess is wrong, tell them if they are too high or too low
while True:
	user_guess = input("What number am I thinking of?: ")
	user_guess = int(user_guess)
	if user_guess > random_number:
		print("Too High")
	elif user_guess < random_number: 
		print("Too Low")
	#If correct, tell them they won and break out of while loop.
	else: 
		print("You Won!")
		#Bonus - let player play again if they want!
		play_again = input("Do you want to play again? (y/n) ")
		if play_again == "y":
			random_number = random.randint(1,10) #numbers 1-10
			guess = None
		else:
			print("Thank you for playing!")
			break

