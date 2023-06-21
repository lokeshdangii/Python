# var1 = open("intro.txt","a")
# var1.write("Lokesh Dangi")
# var1.write("MCA -6th Semester")
# var1.close()


# var1 = open("intro.txt","r")
# data = var1.read()
# print(data)
# var1.close

f = open("telephone.txt","a")
f.close()

f = open("telephone.txt","a")
name =input("Enter your name:")
age = input("Enter your age:")
city =input("Enter your city:")

detail = "Hi I am {}.\nI am {} year old.\nI live in {}.".format(name,age,city)

#print(detail)
# f.write(detail)
f.close()

f = open("telephone.txt","r")
data = f.read()
print(data)
f.close()