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
