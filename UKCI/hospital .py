from tkinter import *

class Window(Tk):
    def __init__(self, *args, **kwargs):
         Tk.__init__(self, *args, **kwargs)
         container = Frame(self)

         container.pack(side="top", fill="both", expand=True)

         container.grid_rowconfigure(0, weight=1)
         container.grid_columnconfigure(0, weight=1)
         

         self.frames = {}

         for F in (Main, Index, Patient, Doctor, Admin):
            frame = F(container, self)           
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
         self.show_frame(Main)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Main(Frame):
    # Quit_Function
    def quit():
        exit()

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='aliceblue')
    # Homepage Introduction
        labelTitle= Label(self, text="Welcome To Hopital Management System",
                          bg="white", width = "1000",
                          height = "2", font="Poppins, 26")
        labelTitle.pack()
    
    # Start Button
    # Button1_Start
        btnStart = Button(self, text="Start", fg="purple", height=5, width=15, 
                          font="Poppins, 20", borderwidth="0", 
                          command=lambda: controller.show_frame(Index))
        btnStart.place(relx=0.5, rely=0.3, anchor=CENTER)
        
    # Button2_Quit
        btnQuit = Button(self, text="Quit", fg="purple", height=5, width=15, 
                         font="Poppins, 20", borderwidth="0", command=quit)
        btnQuit.place(relx=0.5, rely=0.6, anchor=CENTER)
    
    # NAME + ID 
        labelStudentID= Label(self, text=" Student ID: 22225867",
                            bg="white", width = "1000",
                            height = "2", font="Poppins, 15")                    
        labelStudentID.pack(side="bottom", fill="x")
        labelCredits= Label(self, text="By Dishita Naik",
                            bg="white", width = "1000",
                            height = "1", font="Poppins, 18")
        labelCredits.pack(side="bottom", fill="x")

class Index(Frame):   
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='aliceblue')
    # Index Introduction
        labelTitle2= Label(self, text="Please Select Role:", 
                            width = "1000", bg="white",
                          height = "2", font="Poppins, 26")
        labelTitle2.pack()
    # 3 Main Menu Buttons
    # Button1_Admin
        btnAdmin = Button(self, text="ADMIN Login", fg="purple",
                  height=5, width=15, font="Poppins, 20", borderwidth="0",
                  command=lambda: controller.show_frame(Admin))
        btnAdmin.pack(padx=35, pady=35)
    # Button2_Doctor   
        btnDoctor = Button(self, text="DOCTORS Login", fg="purple",
                   height=5, width=15, font="Poppins, 20", borderwidth="0",
                   command=lambda: controller.show_frame(Doctor))
        btnDoctor.pack(padx=35, pady=35)
    # Button3_Patient
        btnPatient = Button(self, text="PATIENTS Login", fg="purple",
                    height=5, width=15, font="Poppins, 20", borderwidth="0",
                    command=lambda: controller.show_frame(Patient))
        btnPatient.pack(padx=35, pady=35)
     
     # Back Button
        backButton =Button(self, text="Back To Home", height=2, width=8, 
                           borderwidth="0", command=lambda: controller.show_frame(Main))
        backButton.pack()

class Patient(Frame): 
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='aliceblue')
    # Patient Introduction
    # Heading
        labelTitle6= Label(self, text="Welcome To The Patient Page", 
                        bg = "white", width = "1000",
                        height = "2", font="Poppins, 26")
        labelTitle6.pack(side=TOP, fill="x")
        # Select Option
        labelTitle6= Label(self, text="Please Select The Following Options:", 
                           bg="aliceblue", width = "1000", font="Poppins, 26")
        labelTitle6.pack(pady=10)
    
    # Option Buttons
    # Button1_Appointment2
        btnAppointment2 = Button(self, text="Create Appointment", fg="purple",
                height=5, width=15, borderwidth="0", font="Poppins, 20",) 
                # command=lambda: controller.show_frame())
        btnAppointment2.pack(pady=10)
    # Button2_Appointment_Status
        btnView_Appointment_Status = Button(self, text="Appointment Status", fg="purple",
                    height=5, width=15, borderwidth="0", font="Poppins, 20",) 
                    # command=lambda: controller.show_frame())
        btnView_Appointment_Status.pack(pady=10)
    # Button3_Update_Patien2
        btnUpdate_Patient2 = Button(self, text="Update Your Information", fg="purple",
                    height=5, width=15, borderwidth="0", font="Poppins, 20",) 
                    # command=lambda: controller.show_frame())
        btnUpdate_Patient2.pack(pady=10)
    # Button4_View_Doctor2
        btnView_Doctor2 = Button(self, text="View Assigned Doctor", fg="purple",
                    height=5, width=15, borderwidth="0", font="Poppins, 20",)
                    # command=lambda: controller.show_frame())
        btnView_Doctor2.pack(pady=10)
    
    # Back Button
        backButton =Button(self, text="Back To Previous Window", height=2, width=15, font="Poppins, 16",
                           borderwidth="0", command=lambda: controller.show_frame(Index))
        backButton.pack(pady=10)

class Doctor(Frame): 
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='aliceblue')
    # Doctor Introduction
    # Heading
        labelTitle6= Label(self, text="Welcome To The Doctor's Page", 
                        bg = "white", width = "1000",
                        height = "2", font="Poppins, 26")
        labelTitle6.pack()
        # Select Option
        labelTitle6= Label(self, text="Please Select The Following Options:", 
                           bg="aliceblue", width = "1000", font="Poppins, 26")
        labelTitle6.pack(pady=10)
    
    # Button1_View_Patient2
        btnView_Patient2 = Button(self, text="View Patients", fg="purple",
                    height=5, width=25, borderwidth="0", font="Poppins, 20",) 
                    # command=lambda: controller.show_frame())
        btnView_Patient2.pack(pady=10)
    # Button2_Update_Patient3
        btnUpdate_Patient3 = Button(self, text="Update Patient Information", fg="purple",
                    height=5, width=25, borderwidth="0", font="Poppins, 20",) 
                    # command=lambda: controller.show_frame())
        btnUpdate_Patient3.pack(pady=10)
    # Button3_Appointment3
        btnAppointment3 = Button(self, text="View Appointments", fg="purple",
                height=5, width=25, borderwidth="0", font="Poppins, 20", )
                # command=lambda: controller.show_frame())
        btnAppointment3.pack(pady=10)
    
    # Back Button
        backButton =Button(self, text="Back To Previous Window",height=2, width=15, font="Poppins, 16", 
                           borderwidth="0", command=lambda: controller.show_frame(Index))
        backButton.pack(pady=10)

class Admin(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='aliceblue')
# Admin Introduction
    # Heading
        labelTitle6= Label(self, text="Welcome To The Admin Page", 
                    bg = "white", width = "1000",
                    height = "2", font="Poppins, 26")
        labelTitle6.pack()
    # Select Option
        labelTitle6= Label(self, text="Please Select The Following Options:", 
                    bg = "aliceblue", width = "1000",
                    height = "2", font="Poppins, 26")
        labelTitle6.pack()


# Option Buttons
# Button1_Appointment
        btnAppointment = Button(self, text="Create Appointment", fg="purple",
            height=2, width=15, borderwidth="0", font="Poppins, 20",) 
##            command=lambda: controller.show_frame())
        btnAppointment.pack(pady =10)
# Button2_Discharge_Patient  
        btnDischarge_Patient = Button(self, text="Discharge Patient", fg="purple",
            height=2, width=15, borderwidth="0", font="Poppins, 20",) 
##            command=lambda: controller.show_frame())
        btnDischarge_Patient.pack(pady =10)

# Button3_Update_Patient
        btnUpdate_Patient = Button(self, text="Update Patient Info", fg="purple",
                height=2, width=15, borderwidth="0", font="Poppins, 20",) 
                # command=lambda: controller.show_frame())
        btnUpdate_Patient.pack(pady =10)
# Button4_View_Patient
        btnView_Patient = Button(self, text="View Patient Info", fg="purple",
                    height=2, width=15, borderwidth="0", font="Poppins, 20",) 
                    # command=lambda: controller.show_frame())
        btnView_Patient.pack(pady =10)

# Button5_Update_Doctor
        btnUpdate_Doctor = Button(self, text="Update Doctor Info", fg="purple",
                    height=2, width=15, borderwidth="0", font="Poppins, 20",) 
                    # command=lambda: controller.show_frame())
        btnUpdate_Doctor.pack(pady =10)
# Button6_View_Doctor
        btnView_Doctor = Button(self, text="View Doctor Info", fg="purple",
                    height=2, width=15, borderwidth="0", font="Poppins, 20",) 
                    # command=lambda: controller.show_frame())
        btnView_Doctor.pack(pady =10)

# Button7_Update_Admin
        btnUpdate_Admin = Button(self, text="Update Admin Info", fg="purple",
                    height=2, width=15, borderwidth="0", font="Poppins, 20",)
                    # command=lambda: controller.show_frame())
        btnUpdate_Admin.pack(pady =10)

# Back Button
        backButton =Button(self, text="Back To Home",height=2, width=15, font="Poppins, 16", 
                           borderwidth="0", command=lambda: controller.show_frame(Main))
        backButton.pack(pady =10)


app = Window()
app.title("Medical Management System")
app.geometry("1000x1200+300+300")
app.mainloop()
