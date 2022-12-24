def fact(x):
    if x==0 or x==1:
        return 1
    else:
        return x*fact(x-1)

var1 = int(input("Enter Value: "))
result= fact(var1)
print("Factorial of {} is {}".format(var1,result)) 