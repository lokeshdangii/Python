"""f = open("marks.txt ","a")
math = int(input("Enter Maths marks: "))
english = int(input("Enter English Marks: "))
hindi = int(input("Enter hindi marks: "))

avg = (math+english+hindi)/3
result = "Math marks is {}.\nEnglish marks is {} .\nHindi marks is {}.\nAvrage of marks is {} ".format(math,english,hindi,avg)
print(result)
f.write(result)
f.close()
"""

#step1 = writing marks to marks.txt
marks = open("marks.txt","w")
student_name = input("Enter Student Name:")
english_marks = int(input("Enter marks obtained in English:"))
hindi_marks = int(input("Enter marks obtained in Hindi:"))
maths_marks = int(input("Enter marks obtained in maths:"))

details = "{},{},{},{}".format(student_name,english_marks,hindi_marks,maths_marks)
marks.write(details)
marks.close()


#step2 = reading marks from marks.txt and calculating average and total marks
data_file = open("marks.txt","r")
data = data_file.read()
# print(data)
record = data.split(",")
# print(record)
total =0
for i in range(1,len(record)):
    total = total + int(record[i])
average = total/(len(record)-1)
# print(total,average)
data_file.close()

# step3
file = open("results.txt","w")
record.append(str(total))
record.append(str(average))
# print(record)

details = record[0]
for i in range(1,(len(record))):
    details = details +"," + record[i]

# print(details)
file.write(details)
file.close()

#step4: read result data and display to the user

file = open("results.txt","r")
data = file.read()
record = data.split(",")
print("Welcome to our portal ")
print("Here is your result ")
print("Student Name :",record[0])
print("Marks in English :",record[1])
print("Marks in Hindi :",record[2])
print("Marks in Maths:", record[3])
print("Total Marks: ",record[4])
print("Average Marks:",record[5])