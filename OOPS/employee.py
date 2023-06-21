class employee:
    def __init__(self):
        self.name = input("Name of the Employee : ")
        self.employee_Id = input("Employee ID:")
        self.contact = input("Contact no:")
        self.address = input("Adress:")
        self.depart = input("Department Name :")

    def show_detail(self):
        print("Employee ID :",self.employee_Id)
        print("Name :",self.name)
        print("Adress :",self.address)
        print("Contact :",self.contact)
        print("Department Name :",self.depart)

    def dwrite(self):
        f = open("employee.txt","a")
        data = self.employee_Id + ","+ self.name + "," + self.contact + "," + self.address + "," + self.depart + "\n"
        f.write(data)
        print("Data Entered Successfully")
    

class Manager(employee):
    # employee().__init__()

    def dept_employee_detail(self):
        f = open("employee.txt","r")
        data = f.read()
        data_row = data.split("\n")
        data_row.pop()
        valid_row = []

        for i in data_row:
            x = i.split(",")
            if self.depart == x[len(x)-1]:
                valid_row.append(i)

class owner(Manager,employee):
    def show_all(self):
        f = open("employee.txt","r")
        data = f.read()
        data_row = data.split("\n")
        data_row.pop()
        for i in data_row:
            x = i.split(",")
            print("-------------------------------------")
            print("Employee ID :",x[0])
            print("Name:",x[1])
            print("Contact : ", x[2])
            print("Adress : ",x[3])
            print("Department :",x[4])
    print("-----------------------------")

s1 = employee()
s2 = Manager()
s3 = owner()
s1.dwrite()
s2.dwrite()
s3.dwrite()

s1.show_detail()
s2.show_detail()
s2.dept_employee_detail()
s3.show_detail()
s3.dept_employee_detail()
s3.show_all()