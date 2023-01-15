def calc():
    var1 = int(input("Enter value 1:"))
    var2 = int(input("Enter value 2:"))
    choice = input("Enter 1 for addition \n 2 for substraction \n 3 for multiplication \n 4 for division\n")

    if choice =="1":
        result = var1+var2
        print("Result= ",result)
    elif choice == "2":
        result= var1 - var2
        print("Result=",result)
    elif choice == "3":
        result = var1*var2
        print("Result=",result)
    elif choice=="4":
        result = var1/var2
        print("Result=",result)
    else:
        print("Entered wrong choice")
        calc()