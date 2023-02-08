rollno = 0
class Student:
    def __init__(self):
        self.name = input("Enter Student's Name :")
        self.fathername = input("Enter Student's Father name :")
        self.age = input("Enter age :")
        self.year = input("Enter year:")
        self.course = input("Enter course :")
        self.contact = input("Enter Contact : ")
    
    def show_detail(self):
        print("Name: ",self.name)
        print("Father's Name:",self.fathername)
        print("Age: ",self.age)
        print("Year of Joining :",self.year)
        print("Course:",self.course)
        print("Contact Details: ",self.contact)
    
    def generate_rollno(self):
        global rollno
        rollno = rollno + 1
        self.rollno = rollno 
        print("Roll no. of Student: ",self.rollno)   


print(rollno)
s1 = Student()
s1.generate_rollno()
s1.show_detail()
print(rollno)
