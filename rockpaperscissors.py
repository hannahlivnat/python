# print("Let's play Rock Paper Scissors!")

# player_1 = input("Player 1, choose your weapon: ")
# player_2 = input("Player 2, choose your weapon: ")

# print("Shoot!")

# if player_1.lower() not in ["rock", "paper", "scissors"]:
# 	print("Player 1, that is not a valid choice")
# 	player_1 = input("Player 1, please enter new value.")
# elif player_2.lower() not in ["rock", "paper", "scissors"]:
# 	print("Player 2, that is not a valid choice")
# 	player_2 = input("Player 2, please enter new value.")
# elif player_1.lower() == player_2.lower():
# 	print("It's a draw!")
# elif player_1.lower() == "rock" and player_2.lower() == "scissors":
# 	print("Player1 wins!")
# elif player_1.lower() == "paper" and player_2.lower() == "rock":
# 	print("Player1 wins!")
# elif player_1.lower() == "scissors" and player_2.lower() == "paper":
# 	print("Player1 wins!")
# else: 
# 	print("Player 2 wins!")

#AI verion

print("Let's play Rock Paper Scissors!")

from random import randint


while True: 
	real_player = input("Choose your weapon: ")
	real_player = real_player.lower()
	a = randint(1,3)
	if a == 1:
		robot_player = 'rock'
	elif a == 2:
		robot_player = 'paper'
	elif a == 3:
		robot_player = 'scissors'

	print("Shoot!")

	if real_player not in ["rock", "paper", "scissors"]:
		print("That is not a valid choice")
	elif real_player == robot_player:
		print("It's a draw!")
	elif robot_player == "rock" and real_player == "scissors":
		print(real_player + " vs. " + robot_player + " the computer wins!")
	elif robot_player == "paper" and real_player == "rock":
		print(real_player + " vs. " + robot_player + " the computer wins!")
	elif robot_player == "scissors" and real_player == "paper":
		print(real_player + " vs. " + robot_player + " the computer wins!")
	else: 
		play_again = input("You Win! Would you like to play again? (y/n): ")
		if play_again == "y":
			a = randint(1,3)
		else: 
			print("Fine, Goodbye")
			break
