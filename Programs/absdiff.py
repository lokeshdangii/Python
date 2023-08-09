# Program to calculate the absolute difference in a list

arr = [9,4,1,6,1,6,35,8]
difflist = []   # list to store the difference

for i in range(0,len(arr)):

	if i == len(arr)-1:
		break
	else:
		diff = arr[i+1]-arr[i]
		difflist.append(diff)


print("list is :", difflist)

max1 = max(difflist)
maxpos = difflist.index(max(difflist))
print(" maximum position at index of list:",maxpos)
print("The maximum absolute difference is :",max1)

print(arr[maxpos])
print(arr[maxpos+1])

print("{} is the absolute difference of {} and {}".format(max1,arr[maxpos],arr[maxpos+1]))

