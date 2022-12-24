def typecheck(user_value):

	num_char = ["0","1","2","3","4","5","6","7","8","9"]
	num_count = 0
	dot_count = 0

	for i in user_value:
		if i in num_char:
			num_count += 1
		
		elif i ==".":
			dot_count +=1
		

	if num_char==1 and dot_count ==0:
		user_value = int(user_value)

	else:
		user_value = float(user_value)

	return user_value


def calculator(n):
	if n==1:
		add= a+b
		print("Sum of {} and {} is {}".format(a,b,add))
		
	
	elif n==2:
		
		sub = a-b
		print("Subtraction of {} and {} is {}".format(a,b,sub))
	
	elif n==3:
		
		mul = a*b
		print("Multiplication of {} and {} is {}".format(a,b,mul))
	
	elif n==4:
		divi = a/b 
		print("Division of {} and {} is {}".format(a,b,divi))
	 	
	else:
		print("Wrong Input")

a = (input("Enter the value of a:"))
b = (input("Enter the value of b:"))
a = typecheck(a)
b = typecheck(b)
print("Type of a:",type(a))
print("Type of b:",type(b))

choice =int(input("Enter choice:"))
calculator(choice)



