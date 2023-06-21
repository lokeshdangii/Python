class Student:
    def __init__(self):
        self.name   = input("enter name:")
        self.course = input("enter course: ")
        self.subject= input("enter Subject :")
    
    def show(self):
        print( "name    : ",self.name)
        print( "course  : ",self.course)
        print( "subject :" ,self.subject)
    
s1 = Student()
s2 = Student()
s1.show()
s2.show()