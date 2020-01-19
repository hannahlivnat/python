# Practice Python Exercise 1: Create a program that asks the user to enter
#their name and age. Print out a message addressed to them that tells them 
#the year that they will turn 100 years old. 
# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

name = input("Give me your name: ")
print("Your name is " + name)

age = int(input("Enter your age: "))
yearsTill100 = 100 - age
yearTurning100 = 2020 + yearsTill100
year100 = str(yearTurning100)

print("You will turn 100 in " + year100)