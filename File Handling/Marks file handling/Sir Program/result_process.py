def assign_grade(x):
	if x>=45 and x<=50:
		return "OUTSTANDING"
	elif x>=40 and x<=44:
		return "A+"
	elif x>=35 and x<=39:
		return "A"
	elif x>=30 and x<=34:
		return "B+"
	elif x>=25 and x<=29:
		return "B"
	elif x>=20 and x<=24:
		return "C"
	elif x>=0 and x<=19:
		return "FAIL"
	else:
		print("INVALID MARKS TOTAL")




def total_marks(x):
	row_elements = x.split(",")
	#print(row_elements)
	smallest = row_elements[2]
	sum = 0
	for i in range(2,5):
		sum = sum + int(row_elements[i])
		if smallest > row_elements[i]:
			smallest = row_elements[i]
	#print(smallest)	
	#print(sum)
	total = sum - int(smallest)
	#print(total)
	return total



#print(file_data)

def result():
	file = open("marks.txt","r")
	file_data = file.read()
	print(file_data)
	file.close()
	row_data = file_data.split("\n")
	print(row_data)
	row_data.pop()
	print(row_data)

	process_data = []
	for i in row_data:
		print(i)
		marks = total_marks(i)
		grade = assign_grade(marks)
	#	i = i + "," + str(marks) +"\n"
		i = "{},{},{} \n".format(i,str(marks),grade)
		
		print(i)
		process_data.append(i)

	file = open("result.txt","w")
	for i in process_data:
		file.write(i)
	file.close()

def display_result():
	file = open("result.txt","r")
	file_data = file.read()
	row_data = file_data.split("\n")
	row_data.pop()
	print(row_data)
	print("*****Result*****")
	for i in row_data:
		row_items = i.split(",")
		print("Name : ",row_items[0])
		print("Roll Number : ",row_items[1])
		print("First Internal marks : ",row_items[2])
		print("Second Internal marks : ",row_items[3])
		print("Third Internal marks : ",row_items[4])
		print("Total Marks : ",row_items[5])
		print("Grade : ",row_items[6])
		print("----------------------------")


