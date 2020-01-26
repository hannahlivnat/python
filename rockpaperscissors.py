print("Let's play Rock Paper Scissors!")

player_1 = input("Player 1, choose your weapon: ")
player_2 = input("Player 2, choose your weapon: ")

print("Shoot!")

if player_1.lower() not in ["rock", "paper", "scissors"]:
	print("Player 1, that is not a valid choice")
	player_1 = input("Player 1, please enter new value.")
elif player_2.lower() not in ["rock", "paper", "scissors"]:
	print("Player 2, that is not a valid choice")
	player_2 = input("Player 2, please enter new value.")
elif player_1.lower() == player_2.lower():
	print("It's a draw!")
elif player_1.lower() == "rock" and player_2.lower() == "scissors":
	print("Player1 wins!")
elif player_1.lower() == "paper" and player_2.lower() == "rock":
	print("Player1 wins!")
elif player_1.lower() == "scissors" and player_2.lower() == "paper":
	print("Player1 wins!")
else: 
	print("Player 2 wins!")

#AI verion

print("Let's play Rock Paper Scissors!")

real_player = input("Choose your weapon: ")

from random import randint
a = randint(1,3)
if a == 1:
	robot_player = 'rock'
elif a == 2:
	robot_player = 'paper'
elif a == 3:
	robot_player = 'scissors'

print("Shoot!")

if real_player.lower() not in ["rock", "paper", "scissors"]:
	print("That is not a valid choice")
	real_player = input("Player 1, please enter new value.")
elif real_player.lower() == robot_player.lower():
	print("It's a draw!")
elif real_player.lower() == "rock" and robot_player.lower() == "scissors":
	print("Rock vs. Scissors, You win!")
elif real_player.lower() == "paper" and robot_player.lower() == "rock":
	print("Paper vs. Rock, You win!")
elif real_player.lower() == "scissors" and robot_player.lower() == "paper":
	print("Scissors vs. Paper, You win!")
else: 
	print(real_player + " vs. " + robot_player + " the computer wins!")
