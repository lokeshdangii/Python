# program for a Calculator
# A mini calculator that perform only addition, substraction, multiplication and division

# a calculator function that checks the user choice and perform operation
 
def calculator():

	print("Welcome to My Calculator")

	var1 = int(input("Enter Value1 : "))
	var2 = int(input("Enter Value2 : "))

	operation_choice = input("Please in Operation of your choice :\n1 for Addition \n2 for Substraction \n3 for Multiplication \n4 for Division\n Please Enter Your Choice :  ")

	if operation_choice == "1" : 
		result = var1 + var2
		print(result) 
	elif operation_choice == "2":
		result = var1 - var2
		print(result)
	elif operation_choice == "3":
		result = var1 * var2 
		print(result)
	elif operation_choice == "4":
		result = var1/var2
		print(result)
	else : 
		print("invalid operation given")
		calculator()


# next_move function to check user want to continue operation or want to exit

def next_move():
	next_choice = input("Enter y to continue or n to close : ")
	if next_choice == "y":
		return True
	elif next_choice == "n":
		return False
	else : 
		print("Invalid Input")
		next_move()


# Driver code

while True : 
	calculator()
	var3 = next_move()
	if var3 == True :
		calculator()

	elif var3 == False: 
		print("Thanks for using my calculator")
		break
