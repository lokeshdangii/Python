#import sample1 as s
from sample1 import *
# calculating permutation 

n,r = int(input("Enter value of n:")),int(input("enter value of r:"))
if n>=r:
    result = fact(n)/fact(n-r)
    print("result:",result)
else:
    print("r should not be greater")
    n,r = int(input("Enter value of n:")),int(input("enter value of r:"))
    if n>=r:
        result = fact(n)/fact(n-r)
        print("result:",result)
    else:
        print("r is greater")

# calculating combination

ncr = fact(n)/(fact(r)*(fact(n-r)))
print("combination:",ncr)
        
    
