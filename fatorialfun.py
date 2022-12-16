def factorial(x):
	fact=1
	if x==0 or x==1:
		fact = 1
	else:
		for i in range(1,x+1):
			fact = fact*i
	return fact

for i in range(4):
	choice = int(input("Enter value:"))
	factorial_value= factorial(choice)
	print("factorial of {} is {}".format(choice,factorial_value))