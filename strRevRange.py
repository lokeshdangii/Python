userStr = input("Enter your string:")
reverse = ""
for i in range(len(userStr)-1,-1,-1):
	reverse = reverse + userStr[i]

print("user given str is {}".format(userStr))
print("Reverse string is {}".format(reverse))