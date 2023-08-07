import data_entry as de

#reading marks from internal.txt and calculating best of two
data_file = open("internal.txt", "r")
data = data_file.read()
#print(data)

data_list = data.split(",")
# print(data_list)
marks_list = []
for i in range(2,len(data_list)):
    marks_list.append(int(data_list[i]))

# print(marks_list)

min_mark = min(marks_list)
# print(min_mark)
marks_list.remove(min_mark)
# print(marks_list)
best_two = sum(marks_list)
# print("best of two:",best_two)

if best_two>= 30:
    grade = "A"
elif best_two >= 20 and best_two <= 30:
    grade = "B"
elif best_two >= 10 and best_two <= 20:
    grade = "C"
else:
    grade = "Fail"

# print("Grade of Student:",grade)

data_list.append(str(best_two))
data_list.append(grade)
# print(data_list)
data_file.close()

#writing marks in result.txt
file = open("result.txt","w")
record = data_list[0]
for i in range(1,len(data_list)):
    record = record +","+ data_list[i]
file.write(record)
file.close()





