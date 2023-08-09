value1 = input("Enter the String: ")
value2 = " "

for i in range(len(value1)):
    if i != 1:
        value2 = value2 + value1[i].lower()
    else:
        value2 = value2 + value1[i].upper()
print("user given value = ",value1)
print("Camel case of given value ", value2)
