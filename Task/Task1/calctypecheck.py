# program to check the value given by user and conver it accordingly to int or float
#  this program is imported as a module and function typecheck is used calculator function in calulator proram(calculator.py)

def typecheck(user_value): #function for checking the user value

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

