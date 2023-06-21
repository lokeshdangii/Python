def myfunction():
    global i
    # x = int(input("Enter value:"))
    # y = int(input("Enter value:"))
    # z = x+y
    # print(z)
    i = "I am inside"
    print(i)
    print(id(i))


i = "I am Outside"
print(i)
print(id(i))
myfunction()
print(i)
print(id(i))




