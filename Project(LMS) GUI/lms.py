from tkinter import*
from tkinter import ttk
import mysql.connector as c
import tkinter
from tkinter import messagebox

class main:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1366x768+0+0")

        tplab = Label(self.root, text = "ABC Library", bg="black", fg="sky blue", bd=20, relief=RIDGE, font=("italic" , 40, "bold"), padx=2, pady=6)
        tplab.pack(side=TOP, fill=X)

        frame = Frame(self.root, bg="black", bd=12, relief=RIDGE, padx=20)
        frame.place(x=0, y=105, width=1360, height=330)

        #-----------------------Variable-----------------------------------

        self.member = StringVar()
        self.idn = StringVar()
        self.f_name = StringVar()
        self.l_name = StringVar()
        self.address = StringVar()
        self.post_c = StringVar()
        self.mobilen = StringVar()
        self.bookid = StringVar()
        self.bookname = StringVar()
        self.authorname = StringVar()
        self.dateb = StringVar()
        self.dated = StringVar()
        self.latefine = StringVar()
        self.daysdue = StringVar()
        self.dateover = StringVar()
        self.bookcost = StringVar()
        
        #-----------------------Dataframe Left------------------------------

        dataframeleft = LabelFrame(self.root, text="Member's Information", bd=6, bg="black", fg="white", padx=20, font=("italic", 12, "bold"))
        dataframeleft.place(x=15, y=120, width=750, height=300)
        
        lbmember = Label(dataframeleft, text="Member Type:", font=("italic", 12, "bold"), bg="black", fg="light blue", padx=2, pady=6)
        lbmember.grid(row=0, column=0, sticky=W)
        comMember = ttk.Combobox(dataframeleft, font=("italic", 12, "bold"), textvariable=self.member, width=22, state="readonly")
        comMember["value"] = ("Student", "Lecturer")
        comMember.grid(row=0, column=1, sticky=W)

        lbid = Label(dataframeleft, text="ID No.:", font=("italic", 12, "bold"), bg="black", fg="light blue", padx=2, pady=6)
        lbid.grid(row=1, column=0, sticky=W)
        txtId = Entry(dataframeleft, font=("italic", 12, "bold"), textvariable=self.idn, width=24)
        txtId.grid(row=1, column=1)

        lbid = Label(dataframeleft, text="First Name:", font=("italic", 12, "bold"), bg="black", fg="light blue", padx=2, pady=6)
        lbid.grid(row=2, column=0, sticky=W)
        txtId = Entry(dataframeleft, font=("italic", 12, "bold"), textvariable=self.f_name, width=24)
        txtId.grid(row=2, column=1)

        lbid = Label(dataframeleft, text="Last Name:", font=("italic", 12, "bold"), bg="black", fg="light blue", padx=2, pady=6)
        lbid.grid(row=3, column=0, sticky=W)
        txtId = Entry(dataframeleft, font=("italic", 12, "bold"), textvariable=self.l_name, width=24)
        txtId.grid(row=3, column=1)

        lbid = Label(dataframeleft, text="Address:", font=("italic", 12, "bold"), bg="black", fg="light blue", padx=2, pady=6)
        lbid.grid(row=4, column=0, sticky=W)
        txtId = Entry(dataframeleft, font=("italic", 12, "bold"), textvariable=self.address, width=24)
        txtId.grid(row=4, column=1)

        lbid = Label(dataframeleft, text="Post Code:", font=("italic", 12, "bold"), bg="black", fg="light blue", padx=2, pady=6)
        lbid.grid(row=5, column=0, sticky=W)
        txtId = Entry(dataframeleft, font=("italic", 12, "bold"), textvariable=self.post_c, width=24)
        txtId.grid(row=5, column=1)

        lbid = Label(dataframeleft, text="Mobile No.:", font=("italic", 12, "bold"), bg="black", fg="light blue", padx=2, pady=6)
        lbid.grid(row=6, column=0, sticky=W)
        txtId = Entry(dataframeleft, font=("italic", 12, "bold"), textvariable=self.mobilen, width=24)
        txtId.grid(row=6, column=1)

        lbid = Label(dataframeleft, text="Book ID:", font=("italic", 12, "bold"), bg="black", fg="light blue", padx=2, pady=6)
        lbid.grid(row=7, column=0, sticky=W)
        txtId = Entry(dataframeleft, font=("italic", 12, "bold"), textvariable=self.bookid, width=24)
        txtId.grid(row=7, column=1)

        lbid = Label(dataframeleft, text="Book Name:", font=("italic", 12, "bold"), bg="black", fg="light blue", padx=2, pady=6)
        lbid.grid(row=0, column=2, sticky=W)
        txtId = Entry(dataframeleft, font=("italic", 12, "bold"), textvariable=self.bookname, width=24)
        txtId.grid(row=0, column=3)

        lbid = Label(dataframeleft, text="Author Name:", font=("italic", 12, "bold"), bg="black", fg="light blue", padx=2, pady=6)
        lbid.grid(row=1, column=2, sticky=W)
        txtId = Entry(dataframeleft, font=("italic", 12, "bold"), textvariable=self.authorname, width=24)
        txtId.grid(row=1, column=3)

        lbid = Label(dataframeleft, text="Date Borrowed:", font=("italic", 12, "bold"), bg="black", fg="light blue", padx=2, pady=6)
        lbid.grid(row=2, column=2, sticky=W)
        txtId = Entry(dataframeleft, font=("italic", 12, "bold"), textvariable=self.dateb, width=24)
        txtId.grid(row=2, column=3)

        lbid = Label(dataframeleft, text="Date Due:", font=("italic", 12, "bold"), bg="black", fg="light blue", padx=2, pady=6)
        lbid.grid(row=3, column=2, sticky=W)
        txtId = Entry(dataframeleft, font=("italic", 12, "bold"), textvariable=self.dated, width=24)
        txtId.grid(row=3, column=3)

        lbid = Label(dataframeleft, text="Late Fine:", font=("italic", 12, "bold"), bg="black", fg="light blue", padx=2, pady=6)
        lbid.grid(row=4, column=2, sticky=W)
        txtId = Entry(dataframeleft, font=("italic", 12, "bold"), textvariable=self.latefine, width=24)
        txtId.grid(row=4, column=3)

        lbid = Label(dataframeleft, text="Days on Book:", font=("italic", 12, "bold"), bg="black", fg="light blue", padx=2, pady=6)
        lbid.grid(row=5, column=2, sticky=W)
        txtId = Entry(dataframeleft, font=("italic", 12, "bold"), textvariable=self.daysdue, width=24)
        txtId.grid(row=5, column=3)

        lbid = Label(dataframeleft, text="Date Overdue:", font=("italic", 12, "bold"), bg="black", fg="light blue", padx=2, pady=6)
        lbid.grid(row=6, column=2, sticky=W)
        txtId = Entry(dataframeleft, font=("italic", 12, "bold"), textvariable=self.dateover, width=24)
        txtId.grid(row=6, column=3)

        lbid = Label(dataframeleft, text="Cost of Book:", font=("italic", 12, "bold"), bg="black", fg="light blue", padx=2, pady=6)
        lbid.grid(row=7, column=2, sticky=W)
        txtId = Entry(dataframeleft, font=("italic", 12, "bold"), textvariable=self.bookcost, width=24)
        txtId.grid(row=7, column=3)

        #-----------------------Dataframe Right------------------------------

        dataframeright = LabelFrame(self.root, text="Display for Infromation", bd=6, bg="black", fg="white", padx=20, font=("italic", 12, "bold"))
        dataframeright.place(x=770, y=120, width=575, height=300)

        self.txtbox = Text(dataframeright, font=("italic", 12, "bold"), width=55, height=13.5, bg="white", fg="black")
        self.txtbox.grid(row=0, column=0)

        #------------------------Button Frame--------------------------------

        framebutton = Frame(self.root, bg="black", bd=6, relief=RIDGE, padx=20)
        framebutton.place(x=0, y=425, width=1360, height=50)

        btnAdd = Button(framebutton, text="Add Data", font=("italic", 12, "bold"), width=21, bg="grey", fg="white", command=self.add_data)
        btnAdd.grid(row=0, column=0)

        btnShow = Button(framebutton, text="Show Data", font=("italic", 12, "bold"), width=21, bg="grey", fg="white", command=self.showData)
        btnShow.grid(row=0, column=1)

        btnUpdate = Button(framebutton, text="Update Data", font=("italic", 12, "bold"), width=21, bg="grey", fg="white", command=self.update_data)
        btnUpdate.grid(row=0, column=2)

        btnDel = Button(framebutton, text="Delete Data", font=("italic", 12, "bold"), width=21, bg="grey", fg="white", command=self.delete)
        btnDel.grid(row=0, column=3)

        btnReset = Button(framebutton, text="Reset", font=("italic", 12, "bold"), width=21, bg="grey", fg="white", command=self.reset)
        btnReset.grid(row=0, column=4)

        btnExit = Button(framebutton, text="EXIT", font=("italic", 12, "bold"), width=20, bg="grey", fg="white", command=self.iExit)
        btnExit.grid(row=0, column=5)

        #------------------------Details Frame--------------------------------

        framedetails = Frame(self.root, bg="black", bd=12, relief=RIDGE, padx=20)
        framedetails.place(x=0, y=468, width=1360, height=230)

        #within framedetails another frame is used to show the data saved 
        tableframe = Frame(framedetails, bg="black", bd=6, relief=RIDGE)
        tableframe.place(x=0, y=5, width=1295, height=196)
        
        #Scrollbar- both Horizontally and Vertically
        xscroll = ttk.Scrollbar(tableframe, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(tableframe, orient=VERTICAL)

        #using treeview(ttk- widget) to see/set columns of the table to be shown 
        self.libTab = ttk.Treeview(tableframe, columns=("memtyp", "id", "fname", "lname", "add", "post", "mobile", "bkid",
                                                     "bkname", "athrname", "db", "dd", "fine", "dobk", "dover", "cost"),
                                                      xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
 
        #packing the scrollbar(or designating it's loaction on the grid)   
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)
        
        #configuring the scrollbar with the library table 
        xscroll.config(command=self.libTab.xview)
        yscroll.config(command=self.libTab.yview)

        #inserting the column names to be shown
        self.libTab.heading("memtyp", text="Member Type")
        self.libTab.heading("id", text="ID No.")
        self.libTab.heading("fname", text="First Name")
        self.libTab.heading("lname", text="Last Name")
        self.libTab.heading("add", text="Address")
        self.libTab.heading("post", text="Post Code")
        self.libTab.heading("mobile", text="Mobile No.")
        self.libTab.heading("bkid", text="Book ID")
        self.libTab.heading("bkname", text="Book Name")
        self.libTab.heading("athrname", text="Author Name")
        self.libTab.heading("db", text="Date Borrowed")
        self.libTab.heading("dd", text="Date Due")
        self.libTab.heading("fine", text="Late Fine")
        self.libTab.heading("dobk", text="Days on Book")
        self.libTab.heading("dover", text="Date Overdue")                                           
        self.libTab.heading("cost", text="Cost of Book")

        #here "show" is used to let us see/show the column names given
        self.libTab["show"] = "headings"
        self.libTab.pack(fill=BOTH, expand=True)

        #setting the width of the heading columns
        self.libTab.column("memtyp", width=90)
        self.libTab.column("id", width=90)
        self.libTab.column("fname", width=90)
        self.libTab.column("lname", width=90)
        self.libTab.column("add", width=90)
        self.libTab.column("post", width=90)
        self.libTab.column("mobile", width=90)
        self.libTab.column("bkid", width=90)
        self.libTab.column("bkname", width=90)
        self.libTab.column("athrname", width=90)  
        self.libTab.column("db", width=90)
        self.libTab.column("dd", width=90)
        self.libTab.column("fine", width=90)
        self.libTab.column("dobk", width=90)
        self.libTab.column("dover", width=90)
        self.libTab.column("cost", width=90)

        self.fetch_data()
        self.libTab.bind("<ButtonRelease-1>", self.get_info)

    #------------------Function to Add Data in Database-----------------------------

    def add_data(self):
        conn = c.connect(host="localhost", user="root", passwd="*******", database="database1")
        my_cursor = conn.cursor()    
        my_cursor.execute("insert into library values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
            (self.member.get(), self.idn.get(), self.f_name.get(), self.l_name.get(), self.address.get(), self.post_c.get(),
            self.mobilen.get(), self.bookid.get(), self.bookname.get(), self.authorname.get(), self.dateb.get(),
            self.dated.get(), self.latefine.get(), self.daysdue.get(), self.dateover.get(), self.bookcost.get()))

        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()    

        messagebox.showinfo("Success!", "Member Added Sucessfully!")  

    #------------------Function to Update the Info in the Database--------------------------------------
     
    def update_data(self):
        conn = c.connect(host="localhost", user="root", passwd="*******", database="database1")
        my_cursor = conn.cursor() 
        libUpdate = ("update library set Member=%s,First_Name=%s,Last_Name=%s,Address=%s,Post_Code=%s,Mobile_No=%s,Book_ID=%s,Book_Title=%s,Author_Name=%s,Date_Borrowed=%s,Date_Due=%s,Late_Fine=%s,Days_on_Book=%s,Date_Overdue=%s,Cost_of_Book=%s where ID=%s")    
        val = (self.member.get(), self.f_name.get(), self.l_name.get(), self.address.get(), self.post_c.get(), self.mobilen.get(), self.bookid.get(), self.bookname.get(), self.authorname.get(), self.dateb.get(), self.dated.get(), self.latefine.get(), self.daysdue.get(), self.dateover.get(), self.bookcost.get(), self.idn.get())
        my_cursor.execute(libUpdate , val)

        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success!", "Member has been  Updated!")   

    #-------------------Function to Delete a Member's Information--------------------------------------
     
    def delete(self):
        if self.idn.get() == "":
            messagebox.showerror("ERROR", "Member Not Selected.")
        else:
            conn = c.connect(host="localhost", user="root", passwd="*******", database="database1")
            my_cursor = conn.cursor()
            dlt = ("delete from library where ID=%s")
            val = (self.idn.get(),)
            my_cursor.execute(dlt, val)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close() 

            messagebox.showinfo("Success", "Member has been Deleted.")

    #------------------Function to Fetch Data from the Database for Details's frame---------------------

    def fetch_data(self):
            conn = c.connect(host="localhost", user="root", passwd="*******", database="database1")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from library")
            rows = my_cursor.fetchall()

            if len(rows)!=0:
                self.libTab.delete(*self.libTab.get_children())
                for i in rows:
                    self.libTab.insert("", END, values=i)
                conn.commit()
            conn.close()     

    #-------------------Function to Display Fetched Data in the Detail's Frame---------------------------

    def get_info(self, event=""):
        c_row = self.libTab.focus()
        content = self.libTab.item(c_row)
        row = content["values"] 

        self.member.set(row[0]),  
        self.idn.set(row[1]),
        self.f_name.set(row[2]),
        self.l_name.set(row[3]),
        self.address.set(row[4]),
        self.post_c.set(row[5]),
        self.mobilen.set(row[6]),
        self.bookid.set(row[7]),
        self.bookname.set(row[8]),
        self.authorname.set(row[9]),
        self.dateb.set(row[10]),
        self.dated.set(row[11]),
        self.latefine.set(row[12]),
        self.daysdue.set(row[13]),
        self.dateover.set(row[14]),
        self.bookcost.set(row[15])

    #---------------------Function to Display the Data in the Text Frame using ShowButton-----------------------------
 
    def showData(self):
        self.txtbox.insert(END, "Member Type:\t" + self.member.get() + "\t\t\t" + "ID No.:\t" + self.idn.get() + "\n")
        self.txtbox.insert(END, "First Name:\t" + self.f_name.get() + "\t\t\t" + "Last Name:\t" + self.l_name.get() + "\n")
        self.txtbox.insert(END, "Address:\t" + self.address.get() + "\t\t\t" + "Postal Code:\t" + self.post_c.get() + "\n")
        self.txtbox.insert(END, "Mobile Number:\t" + self.mobilen.get() + "\t\t\t" + "Book ID:\t" + self.bookid.get() + "\n")
        self.txtbox.insert(END, "Book Title:\t" + self.bookname.get() + "\t\t\t" + "Author Name:\t" + self.authorname.get() + "\n")
        self.txtbox.insert(END, "Date Borrowed:\t" + self.dateb.get() + "\t\t\t" + "Date Due:\t" + self.dated.get() + "\n") 
        self.txtbox.insert(END, "Late Fine:\t" + self.latefine.get() + "\t\t\t" + "Days Due:\t" + self.daysdue.get() + "\n")   
        self.txtbox.insert(END, "Date Overdue:\t" + self.dateover.get() + "\t\t\t" + "Cost of Book:\t" + self.bookcost.get() + "\n\n")

    #------------------------Function to Reset the Member's Information-------------------------------
        
    def reset(self):
        self.member.set(""),  
        self.idn.set(""),
        self.f_name.set(""),
        self.l_name.set(""),
        self.address.set(""),
        self.post_c.set(""),
        self.mobilen.set(""),
        self.bookid.set(""),
        self.bookname.set(""),
        self.authorname.set(""),
        self.dateb.set(""),
        self.dated.set(""),
        self.latefine.set(""),
        self.daysdue.set(""),
        self.dateover.set(""),
        self.bookcost.set(""),
        self.txtbox.delete("1.0", END)  

    #-----------------Function to Exit the System---------------------------------------

    def iExit(self):
        iExit = tkinter.messagebox.askyesno("ABC Library", "Do you want to Exit the System?")
        if iExit>0:
            self.root.destroy()
            return          

       
root = Tk()
obj = main(root)
root.mainloop()