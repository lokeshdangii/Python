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
    
# e1 = employee()
# e1.show_detail()
# e1.dwrite()

m1 = Manager()
# m1.show_detail()
m1.dwrite()
m1.dept_employee_detail()