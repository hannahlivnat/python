number = input("Please enter a number, and I'll give you it's divisors: ")
number = int(number)

divisor_list = []

for num in range(1,number+1):
	if number % num == 0:
		divisor_list.append(num) 
print(divisor_list)
