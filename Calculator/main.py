from arithmetic import *
from check import *

test = True
while True:
    if test == True:
        calc()
        test=take_choice()
    else:
        print("Thank you for using my calculator")
        break