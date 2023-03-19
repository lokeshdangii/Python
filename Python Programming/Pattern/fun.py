# def f1():
#     print("Hello")
#     def f2():
#         print("Anna")
#     return f2()



# str = f1()
# print("f2 = ",str)

def enhanced(func):
    def inner(a,b):
        if b==0:
            return "can not divide by zero"
        else:
            return func(a,b)
    return inner  
@enhanced
def f1(a,b):
    return a/b

a = f1(10,0)
print(a)
