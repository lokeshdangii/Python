'''
def summation(a,b):
	sum = a+b
	return sum

def subtraction(a,b):
	sub = a-b
	return sub

def multiplication(a,b):
	mul = a*b 
	return mul

def division(a,b):
	divi = a/b 
	return divi 

a=5
b=8
add = summation(a,b)
print("Sum of {} and {} is {}".format(a,b,add))
'''
def calculator(n):
	if n==1:
		a= int(input("Enter the value of a:"))
		b= int(input("Enter the value of b:"))
		add= a+b
		return add
		#print("Sum of {} and {} is {}".format(a,b,add))
		
	
	elif n==2:
		a= int(input("Enter the value of a:"))
		b= int(input("Enter the value of b:"))
		sub = a-b
		return sub
		#print("Subtraction of {} and {} is {}".format(a,b,sub))
	
	elif n==3:
		a= int(input("Enter the value of a:"))
		b= int(input("Enter the value of b:"))
		mul = a*b
		return mul
		print("Multiplication of {} and {} is {}".format(a,b,mul))
	
	elif n==4:
		a= int(input("Enter the value of a:"))
		b= int(input("Enter the value of b:"))
		divi = a/b 
		return divi
		print("Division of {} and {} is {}".format(a,b,divi))
	 	
	else:
		print("Wrong Input")

ans = calculator(choice)
print("answer is :",ans)
		



