x = input("Enter value : ")
y = ""
for i in x:
	if ord(i)>=65 and ord(i)<= 90:
		a = ord(i)+32
		b = chr(a)
		y = y+b
	# elif ord(i)>=97 and ord(i)<=122:
	# 	y=y+i

	else:
		y = y+i
print("Value before Conversion =", x)
print("value after Conversion = ", y)
