# Program for calculator

import calctypecheck as ct
  
num1= input("enter the value of num1: ")
num2= input("enter the value of num2: ")

num1 = ct.typecheck(num1)
num2 = ct.typecheck(num2)

def calculator(n):
	if n==1:
		add = num1+num2

		print("Addition of {} and {} is {}".format(num1,num2,add))
		return add
	elif n==2:
		
		sub = num1-num2
		print("Subtraction of {} and {} is {}".format(num1,num2,sub))
		return sub

	elif n==3:
		
		mul = num1*num2
		print("Multiplication of {} and {} is {}".format(num1,num2,))
		return mul

	elif n==4:
		
		div = num1/num2
		print("Division of {} and {} is {}".format(num1,num2,div))
		return div

	else:
		print("Wrong Choice...!")

def sqcalc(n):
    square = n**n
    return square

choice =int(input("Enter choice:"))
output = calculator(choice)
print(output)

output = ct.tnum2pecheck(output)
print("type of output:", type(output))


