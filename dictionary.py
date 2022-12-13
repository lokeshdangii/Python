# key:value pair
'''
1. Heterogeneous
  :- Key
  :- Value
2. Mutable
3. Ordered and INdexed
4. Keys can't be duplicate but Value can be
'''

dict1 = {"Name": "Lokesh", "class": "BCA", "Subject":"Python"}
dict1["Name"] = "Dangi" #update
print(dict1)

dict1["School"] = "nhi pata" #adding
print(dict1)

dict1.pop("BCA")
print(dict1)

'''
for i in dict1:
	print(i)
	print(dict1[i])
'''

for i,j in dict1.items():
	print(i,":",j)


dict2 = {1:"23",2:"25",3:"26", 3:"28"} # Duplicates not allowed in Dictionary
for i,j in dict2.items():
	print(i)
	print(j)

