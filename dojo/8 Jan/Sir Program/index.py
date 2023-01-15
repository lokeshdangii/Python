from marks_entry import *
from result_process import *



# for student's marks entry

print("WELCOME TO OUR RESULT PORTAL ")
print("Please enter a valid choice")
print("Press 1 for making student's marks entry")
print("Press 2 for result processing")
print("Press 3 for displaying result ")
function_choice = int(input("Please enter your choice : "))
if function_choice == 1:	
	choice = True
	while True:
		if choice == True:
			row_entry()
			choice = takechoice()
		else:
			break
elif function_choice == 2:
	result()
elif function_choice == 3:
	display_result()
else:
	print("INVALID CHOICE")
