def row_entry():
	name = input("Enter student's name : ")
	roll_no = input("Enter student's roll number : ")
	first_internal = input("Enter first internal marks : ")
	second_internal = input("Enter second internal marks : ")
	third_internal = input("Enter third internal marks : ")
	file = open("marks.txt","a")
	entry = "{},{},{},{},{}\n".format(name,roll_no,first_internal,second_internal,third_internal)
	file.write(entry)
	file.close()
	print("record added successfully")

def takechoice():
	choice = input("Enter y for adding another student or n for EXIT : ")
	if choice == "y" or choice == "Y":
		return True
	elif choice == "n" or choice == "N":
		return False
	else:
		takechoice()
	

