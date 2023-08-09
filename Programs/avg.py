choice = int(input("Enter no. of terms:"))
sum = 0
for i in range(choice):
	value = int(input("Enter value : "))
	sum = sum + value
average = sum/choice
print("Average=",average)