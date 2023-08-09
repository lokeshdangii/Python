for i in range(3):
    name = input("enter name of student = ")
    classe = input("enter the class of student = ")
    contact_no = input("enter the contact no. of student = ")
    email_id = input("enter the email id of student = ")

    if i == 0:
        List1 = [name,classe,contact_no,email_id]
        print("My name is {},\nmy class is {},\nmy mob no. is {},\nand my email is {}" .format(name,classe,contact_no,email_id))
       
    if i == 1:
        List2 = [name,classe,contact_no,email_id]
        print("My name is {},\nmy class is {},\nmy mob no. is {},\nand my email is {}" .format(name,classe,contact_no,email_id))
    if i == 2:
        List3 = [name,classe,contact_no,email_id]
        print("My name is {},\nmy class is {},\nmy mob no. is {},\nand my email is {}" .format(name,classe,contact_no,email_id))

print(List1)
print(List2)
print(List3)

    



