# file = open('demofile.txt', 'w')
# file.write('''ThankYou!!!!!!''')
# file.close()

# file = open('demofile.txt', 'r')
# print(file.read())

# file = open('newfile.txt', 'x')
# file.write("I am writing")

file = open('demofile.txt','r+')
print(file.read())
file.write("Once Again Thankyou")
print(file.read())
# print(file.read())

# data = file.read()
# print(data)
