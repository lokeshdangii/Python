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



# print('user_input = '  ,user_input)
# print(type(user_input))