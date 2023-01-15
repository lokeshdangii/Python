def fact(x):
	fact=1
	if x==0 or x==1:
		fact = 1
	else:
		for i in range(1,x+1):
			fact = fact*i
	return fact
#print(fact(5))

