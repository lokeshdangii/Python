"""i = 6
while True :
	print(i)
	i = i + 1
	if i > 5 : 
		break
"""
def calculator():
	print("Welcome to My Calculator")
	var1 = int(input("Enter Value1 : "))
	var2 = int(input("Enter Value2 : "))
	oper_choice = input("Please in Operation of your choice :\n1 for Addition \n2 for Substraction \n3 for Multiplication \n4 for Division\n Please Enter Your Choice :  ")
	if oper_choice == "1" : 
		result = var1 + var2
		print(result) 
	elif oper_choice == "2":
		result = var1 - var2
		print(result)
	elif oper_choice == "3":
		result = var1 * var2 
		print(result)
	elif oper_choice == "4":
		result = var1/var2
		print(result)
	else : 
		print("invalid operation given")
		calculator()

def next_move():
	next_choice = input("Enter y to continue or n to close : ")
	if next_choice == "y":
		return True
	elif next_choice == "n":
		return False
	else : 
		print("Invalid Input")
		next_move()

while True : 
	calculator()
	var3 = next_move()
	if var3 == True :
		calculator()

	elif var3 == False: 
		print("Thanks for using my calculator")
		break
