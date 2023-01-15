import calctypecheck as ct
x= input("enter the value of x: ")
y= input("enter the value of y: ")

x = ct.typecheck(x)
y = ct.typecheck(y)

def calculator(n):
	if n==1:
		add = x+y

		print("Addition of {} and {} is {}".format(x,y,add))
		return add
	elif n==2:
		
		sub = x-y
		print("Subtraction of {} and {} is {}".format(x,y,sub))
		return sub

	elif n==3:
		
		mul = x*y
		print("Multiplication of {} and {} is {}".format(x,y,))
		return mul

	elif n==4:
		
		div = x/y
		print("Division of {} and {} is {}".format(x,y,div))
		return div

	else:
		print("Wrong Choice...!")

def sqcalc(n):
    sqre = n**n
    return sqre

choice =int(input("Enter choice:"))
ouput = calculator(choice)
print(ouput)

ouput = ct.typecheck(ouput)
print("type of output:", type(ouput))


