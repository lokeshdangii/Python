f = open("marks.txt ","a")
math = int(input("Enter Maths marks: "))
english = int(input("Enter English Marks: "))
hindi = int(input("Enter hindi marks: "))

avg = (math+english+hindi)/3
result = "Math marks is {}.\nEnglish marks is {} .\nHindi marks is {}.\nAvrage of marks is {} ".format(math,english,hindi,avg)
print(result)
f.write(result)
f.close()