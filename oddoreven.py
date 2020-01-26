number = input("Give me a number!")

if int(number) % 2 == 0:
	print("Your number is even!")
else: 
	print("Your number is odd")

if int(number) % 4 == 0:
	print("Your number is a multiple of 4!")
else: 
	print("Your number is not a multiple of 4!")

num = input("Give me a number.")
check = input("Give me a number to divide by")

if int(num) % int(check) == 0:
	print("Your number divides evenly")
else: 
	print(check + " is not divisible by " + num)