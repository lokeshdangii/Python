def checktype(n):
	if type(n) is int:
		print("given {} is integer".format(n))
	elif type(n) is str:
		print("given {} is String".format(n))
	elif type(n) is bool:
		print("given {} is boolean".format(n))
	elif type(n) is complex:
		print("given {} is complex".format(n))
	else:
		print("given {} is float".format(n))


choice = input("Enter a choice:")
checktype(choice)


