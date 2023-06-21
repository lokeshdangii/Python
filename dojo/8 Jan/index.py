# import data_entry as de
import result_creation as rc

# read  data and display to the user

file = open("result.txt","r")
data = file.read()
record_list = data.split(",")

#printing the data of result.txt

print("\n---------RESULT------------ ")
print("\nStudent Name :",record_list[0])
print("Roll no. of student",record_list[1])
print("Marks in Test1 :",record_list[2])
print("Marks in Test2 :",record_list[3])
print("Marks in Test3:", record_list[4])
print("Best of Two : ",record_list[5])
print("Grade of Student:",record_list[6])