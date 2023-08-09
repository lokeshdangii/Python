'''list1 = [15,12,13,14,15,16]
list1.append(23)

print(list1)
print(id(list1))
list1.remove(15)
print(list1)
print(id(list1))
'''
'''
l1 = [15,12,13,14]
l2 = [21,16,11]
l1.append(l2)
print(l1)
'''

l1 = [15,12,13,14]
l2 = [21,16,11]
print(l1,l2)
for i in l2:
	l1.append(i)
print(l1,l2)