# writing marks to internal.txt
marks = open("internal.txt","w")
name = input("Enter the name of student:")
roll = input("Enter the roll no. of student:")
test1 = int(input("enter marks of test1:"))
test2 = int(input("enter marks of test2:"))
test3 = int(input("Enter marks of test3:"))
details = "{},{},{},{},{}".format(name,roll,test1,test2,test3)
# print(details)
# print(type(details))

marks.write(details)
marks.close()
