def take_choice():
    choice = input("Enter y for yes and n for no:")
    
    if choice == "y" or choice =="Y":
        return True
    elif choice == "n" or choice == "N":
        return False
    else:
        print("Invalid choice")
        take_choice()
