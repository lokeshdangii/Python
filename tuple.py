tuple1 = (25,10,25.5,"Star Wars")
Epic = ((25,10,11,0.75,"Thor"))
print(Epic,tuple1)

print(Epic)
print(type(Epic))
print(tuple1)
print(type(tuple1))
print("\n")

for i in tuple1:
	print("Index = ", tuple1.index(i))
	print("Value = ", i)
	print("Type = ", type((i)))
	print("Id = ", id(i))
	print("\n")

#tuple1.append("LOKESH")
tuple1.pop()