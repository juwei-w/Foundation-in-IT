# *********************************************************
# Program: GROUP_10.py #
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN 
# Class: TLX# Trimester: 2115# Year: 2021/22 Trimester 1 
# Member_1: 1211104210  | WONG JU WEI |    0162703913
# Member_2: 1211102387  | FOONG WEI PIN |  0133500103
# Member_3: 1211103997  | SHAKTISH |       0125062547
# Member_4: 1211103927  | SHINLY EU |      0136630012 
# *********************************************************
# Task Distribution
# Member_1: (WONG JU WEI)         USER PAGE & BACKEND DATA EXTRACT & FLOWCHARTS (CODE COMBINER)
# Member_2: (FOONG WEI PIN)       GUI
# Member_3: (SHAKTISH PILLAI)     ADMIN PAGE
# Member_4: (SHINLY EU)           LOG IN PAGE & FLOWCHARTS
# *********************************************************

# =================================================================================================================================================================== #
# =================================================================================================================================================================== #
# =================================================================================================================================================================== #

# User #                                             # Admin #
# Name = Jeremy                                      Name = MMU
# Ic = 0000000001                                    Password = 12111
# Password = 123

import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox
import json

# Global Variable
filename = "Info.json"
Empty = [" " * i for i in range(15)]

# =================================================================================================================================================================== #
# =================================================================================================================================================================== #
# =================================================================================================================================================================== #
# BACKEND DATA EXTRACT
# (JU WEI)


class UserData(object):
    def __init__(self):
        self.users = load_user()                         # Contains all attributes/properties of user

    # This method will add new user through sign in
    def add_user(self, new_user):
        with open(filename, "r+") as data:               # Reading and Writting mode
            jsonData = json.load(data)
            jsonData.append(new_user)
            data.seek(0)                                 # Move the cursor back to the beginning of the file then start writing
            json.dump(jsonData, data, indent=4)

    # This method will get user object based on IC.NO
    def get_user(self, Ic):
        for user in self.users:                          # Iterating all attributes and finding user using Ic
            if(user.Ic == Ic):
                return user

    # This method will update json file with latest data
    def update_user(self):
        with open(filename,"w") as info:
            json.dump(self.users, info, indent = 4, default=encode_user) # Encoding and rewriting json file as dictionary
                                                                         # default=vars  *AND*  default=lambda user : user.__dict__  does the same thing as well

# Assigning values to each user object
class Process:
    def __init__(self, Name, Age, Ic, Address, PostCode, PhoneNum, Occupation, Category, Password, Status, MedHistory, Priority, VaccStatus, VaccCenter, VaccDate, VaccTime, Rsvp):
        self.Name = Name
        self.Age = Age
        self.Ic = Ic
        self.Address = Address
        self.PostCode = PostCode
        self.PhoneNum = PhoneNum
        self.Occupation = Occupation
        self.Category = Category
        self.Password = Password
        self.Status = Status
        self.MedHistory = MedHistory
        self.Priority = Priority
        self.VaccStatus = VaccStatus
        self.VaccCenter = VaccCenter
        self.VaccDate = VaccDate
        self.VaccTime = VaccTime
        self.Rsvp = Rsvp


# Load user from json file
def load_user():
    with open(filename, "r") as data:
        jsonData = json.load(data)                        # Returns json objects as dictionary (key/value pair)
        users = [Process(**k) for k in jsonData]          # Iterating & passing all values into class "Process"
    return users #


# This is use to convert User Class to json.
def encode_user(obj):
    if isinstance(obj, Process):                          # Checking whether object is an instance of Process
        return obj.__dict__                               # Converts into dictionary
    return obj


# Method read "users.json" and returns data as str
def user():
    with open(filename, "r") as info:
        data = json.loads(info.read())
        return data


# =================================================================================================================================================================== #
# =================================================================================================================================================================== #
# =================================================================================================================================================================== #
# USER LOG IN, REGISTER / SIGN UP, ADMIN LOG IN 
# (SHINLY)


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where stack a bunch of frames
        # on top of each other, then the one visible
        # will be raised above the others

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Login, Admin, SignUp):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


# The first page that appear
class StartPage(tk.Frame):

    # setting up the frame with title , geometry and etc
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title('Mysejahtera')

        # create buttons to go to another frame
        button1 = tk.Button(self, text="Public User Login", width=20, height=2,
                            command=lambda: controller.show_frame("Login"))

        button2 = tk.Button(self, text="Sign Up", width=20, height=2,
                            command=lambda: controller.show_frame("SignUp"))

        button3 = tk.Button(self, text="Admin Login", width=20, height=2,
                            command=lambda: controller.show_frame("Admin"))
        

        button1.pack(padx=10, pady=130)
        button2.pack(padx=10, pady=30)
        button3.pack(padx=10, pady=120)


class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # To guide user to type their Ic number
        label1 = tk.Label(self, text="Ic :")
        label1.place(x=70, y=34)

        #  To guide user to type their Password
        label2 = tk.Label(self, text="Password :")
        label2.place(x=70, y=110)

        #  To get User's Ic
        global ic
        ic = tk.StringVar()
        e1 = tk.Entry(self,textvariable = ic, show="", width=100)
        e1.pack(padx=25, pady=30)

        # To get User's Password
        global pw
        pw = tk.StringVar()
        e2 = tk.Entry(self,textvariable= pw, show="", width=100)
        e2.pack(padx=25, pady=30)


        # Create Buttons with login and back function
        button1 = tk.Button(self, text="Login", width=20,
                            height=2, command=lambda: self.login())
        button1.pack(padx=50, pady=130)

        button2 = tk.Button(self, text="Back", width=20, height=2,
                            command=lambda: controller.show_frame("StartPage"))
        button2.pack(padx=10, pady=20)

    # Login Function
    def login(self):
        LogInFlag = True
        while LogInFlag:
            Ic = ic.get()
            Pw = pw.get()
            database = UserData()
            user = database.get_user(Ic)
            try:
                if user.Ic == Ic:
                    try:
                        if user.Password == Pw:
                            LogInFlag = False
                            messagebox.showinfo("Mysejahtera", "Login success")
                            self.controller.destroy()
                            UserPage(Ic)
                            return True
                        else:
                            messagebox.showinfo("Mysejahtera", "Incorrect Password")
                            return True
                    except:
                        messagebox.showinfo("Mysejahtera", "Incorrect Password")
                        return True
                else:
                    PromtFlag = True
                    while PromtFlag:
                        messagebox.showinfo("Mysejahtera", "User Doesnt Exist")
                        return True
            except:
                messagebox.showinfo("Mysejahtera", "User Doesnt Exist")
                return True


# Sign up Page
class SignUp(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.geometry("1000x750")

        # To guide the user where to type their name
        Label1 = tk.Label(self, text="Name :")
        Label1.place(x=22, y=34)

        # To guide the user where to type their age
        Label2 = tk.Label(self, text="Age :")
        Label2.place(x=22, y=110)

        # To guide the user where to type their Ic number
        Label3 = tk.Label(self, text="Ic :")
        Label3.place(x=22, y=190)

        # To guide the user where to type their Password
        Label4 = tk.Label(self, text="Password :")
        Label4.place(x=22, y=270)

        # To guide the user where to type their Phone Number
        Label5 = tk.Label(self, text="Phone Number :")
        Label5.place(x=22, y=346)

        # To guide the user where to type their address
        Label6 = tk.Label(self, text="Address :")
        Label6.place(x=22, y=422)

        # To guide the user where to type their postcode
        Label7 = tk.Label(self, text="Postcode :")
        Label7.place(x=22, y=498)

        # To guide the user where to choose their occupation
        Label8 = tk.Label(self, text="Occupation category :")
        Label8.place(x=22, y=574)

        # To get and global user Name
        global e1
        e1 = tk.Entry(self, show="", width=120)
        e1.pack(padx=22, pady=30)

        # To get and global user age
        global e2
        e2 = tk.Entry(self, show="", width=120)
        e2.pack(padx=22, pady=30)

        # To get and global user Ic
        global e3
        e3 = tk.Entry(self, show="", width=120)
        e3.pack(padx=22, pady=30)

        # To get and global user Password
        global e4
        e4 = tk.Entry(self, show="", width=120)
        e4.pack(padx=22, pady=30)

        # To get and global user Phone number
        global e5
        e5 = tk.Entry(self, show="", width=120)
        e5.pack(padx=22, pady=30)

        # To get and global user Address
        global e6
        e6 = tk.Entry(self, show="", width=120)
        e6.pack(padx=22, pady=30)

        # To get and global user Postcode
        global e7
        e7 = tk.Entry(self, show="", width=120)
        e7.pack(padx=22, pady=30)

        def callback(selection):
            global Category
            global Priority
            Category = selection
            try:
                if Category == "Frontliner (Major)":
                    Priority = "5"
                elif Category == "Frontliner (Minor)":
                    Priority = "4"
                elif Category == "Midliner (Major)":
                    Priority = "3"
                elif Category == "Midliner (Minor)":
                    Priority = "2"
                elif Category == "Backliner":
                    Priority = "1"
                else:
                    Priority = "-"
            except NameError:
                messagebox.showerror("Mysejahtera","Choose Category")



        # To let user to choose their Occupation
        OccupationList = ["Frontliner (Major)", "Frontliner (Minor)", "Midliner (Major)", "Midliner (Minor)", "Backliner"]
        value_inside = tk.StringVar(self)
        value_inside.set("Choose an Occupation category")
        question_menu = tk.OptionMenu(self, value_inside, *OccupationList, command=callback)
        question_menu.pack(pady=20)

        # Button with Sign Up function
        button1 = tk.Button(self, text="Sign Up", width=20, height=2,
                            command=lambda:self.signup())
        button1.pack()

        button2 = tk.Button(self, text="Back", width=20, height=2,
                            command=lambda: controller.show_frame("StartPage"))
        button2.pack()


    # Sign Up function
    # Global all the info and store in Json file with the format
    def signup(self):
        global Name, Age, Ic, Password, Priority, Postcode, Address, new_user
        try:
            N1 = e1.get()
            N2 = e2.get()
            N3 = e3.get()
            N4 = e4.get()
            N5 = e5.get()
            N6 = e6.get()
            N7 = e7.get()
            Name = N1
            Age = N2
            Ic = N3
            Password = N4
            PhoneNum = N5
            Address = N6
            Postcode = N7
            database = UserData()
            new_user = {
                "Name": Name,
                "Age": Age,
                "Ic": Ic,
                "Address": Address,
                "PostCode": Postcode,
                "PhoneNum": PhoneNum,
                "Occupation": "-",
                "Category": Category,
                "Password": Password,
                "Status": "-",
                "MedHistory": "-",
                "Priority": Priority,
                "VaccStatus": "-",
                "VaccCenter": "-",
                "VaccDate": "-",
                "VaccTime": "-",
                "Rsvp": "-"
            }
        except NameError:
            messagebox.showerror("Mysejahtera", "Choose Your Occupation Category")
            return True
        try:
            if Name in Empty or Age in Empty or Ic in Empty or Password in Empty or Postcode in Empty or PhoneNum in Empty or Address in Empty:
                messagebox.showerror("Mysejahtera", "Please Fill In All the Information Required")
            else:
                with open(filename, "r+") as data:
                    jsonData = json.load(data)
                    jsonData.append(new_user)
                    data.seek(0)
                    json.dump(jsonData, data, indent=4)
                messagebox.showinfo("Mysejahtera", "You have successfully registered!")

                # To clear the text after the user Sign Up
                def clear_text():
                    e1.delete(0, 'end')
                    e2.delete(0, 'end')
                    e3.delete(0, 'end')
                    e4.delete(0, 'end')
                    e5.delete(0, 'end')
                    e6.delete(0, 'end')
                    e7.delete(0, 'end')
                clear_text()
                self.controller.show_frame(("StartPage"))
        except NameError:
            messagebox.showerror("Mysejahtera", "Something went Wrong")


# Admin page
class Admin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #  To guide the user where to type their name
        Label1 = tk.Label(self, text="Admin Name :")
        Label1.place(x=70, y=34)

        # To guide the user where to type their password
        Label2 = tk.Label(self, text="Password :")
        Label2.place(x=70, y=110)

        # To get User Name
        global name
        name = tk.StringVar()
        e1 = tk.Entry(self,textvariable=name, show="", width=100)
        e1.pack(padx=22, pady=30)

        # To get User's Password
        global Pas
        Pas = tk.StringVar()
        e2 = tk.Entry(self,textvariable=Pas, show="", width=100)
        e2.pack(padx=22, pady=30)

        # Button with Login function
        Button1 = tk.Button(self, text="Login", width=20,
                            height=2, command=lambda: self.admin_login())
        Button1.pack(padx=50, pady=10)

        # Button with back function
        Button1 = tk.Button(self, text="Back", width=20,
                            height=2, command=lambda: controller.show_frame("StartPage"))
        Button1.pack(padx=50, pady=20)

    # To check user name and password
    def admin_login(self):
        Admin_name = name.get()
        Password = Pas.get()
        file = open("AdministratorPassword.txt", "r")
        for i in file:
            nm, pas = i.split(", ")
            pas = pas.strip()
            if nm == Admin_name and pas == Password:
                messagebox.showinfo("Mysejahtera", "Login Success")
                self.controller.destroy()
                AdminPage(Admin_name)
                return True
            else:
                messagebox.showerror("Mysejahtera", "Incorrect Name or Password")
                return True



# =================================================================================================================================================================== #
# =================================================================================================================================================================== #
# =================================================================================================================================================================== #
# USER PAGE / INTERFACE
# (JU WEI)


def UserPage(Ic):
    try:
        database = UserData()
        user = database.get_user(Ic)
        print( "\n" * 35 )
        print("Login successful.")
        print("")
        print("Welcome! " + user.Name)
        UserFlag = True
        while UserFlag:
            print("")
            print("---User Menu---")
            print("1. Update Medical History")        # Update MedHistory (Risk Group)
            print("2. View & Update Information")     # View and update user's information
            print("3. View Appointment")              # View appointment information
            print("4. Log Out")
            print("\n------------------------------------------------------------")
            print("Enter A Number To Proceed.")
            print("------------------------------------------------------------\n")
            UserAction = input(">> ")
            print("\n")

            if UserAction == "1": # -------------------------------------------------------------------------------------(1. Medical Update)
                print( "\n" * 35 )
                print("---Medical Update---")
                print("1. Have you experiece any Covid-19 symptoms?")
                print("2. Are you exhibiting any difficulty breathing?")
                print("3. Have you attend any event with known Covid-19 cluster?")
                print("4. Have you traveled abroad recently?")
                print("5. Have you had close contact with any confirmed or suspected cases?")
                print("\nEnter the number if you experienced any of it.")
                MedInput = input(">> ").split()

                # Update MedHistory
                if len(MedInput) <= 2:
                    user.MedHistory = "Low Risk"
                    print("\nRisk Group >> " + user.MedHistory)
                    database.update_user()

                else:
                    user.MedHistory = "High Risk"
                    print("\nRisk Group >> " + user.MedHistory)
                    database.update_user()

                print("\n------------------------------------------------------------")
                print("Press Enter To Continue.")
                print("------------------------------------------------------------\n")
                EnterInput = input("")
                print( "\n" * 35 )

            elif UserAction == "2": # -----------------------------------------------------------------------------------(2. View User Info)
                print( "\n" * 35 )
                ViewInfoFlag = True
                while ViewInfoFlag:
                    print("---View Information---")
                    print("Name                 : " + user.Name)
                    print("Age                  : " + user.Age)
                    print("IC Number            : " + user.Ic)
                    print("Address              : " + user.Address)
                    print("PostCode             : " + user.PostCode)
                    print("PhoneNum             : " + user.PhoneNum)
                    print("Covid Status         : " + user.Status)
                    print("Occupation           : " + user.Occupation)
                    print("Occupation Category  : " + user.Category)
                    print("Password             : " + user.Password)
                    print("\n------------------------------------------------------------")
                    print("1. Update Information.")
                    print("2. Back.")
                    print("------------------------------------------------------------\n")
                    print("Enter A Number To Proceed.")
                    ViewInfoInput = input(">> ")

                    if ViewInfoInput == "1": # Update User Information (ViewInfoFlag = True)
                        print( "\n" * 35 )
                        InfoNotEmpty = True
                        while InfoNotEmpty:
                            user.Name = input("Enter Name: ")
                            user.Age = input("Enter Age: ")
                            user.Address = input("Enter New Address: ")
                            user.PostCode = input("Enter New Postcode: ")
                            user.PhoneNum = input("Enter New Phone Number: ")
                            user.Occupation = input("Enter New Occupation: ")
                            CategoryFlag = True
                            while CategoryFlag:
                                print("Enter New Occupation Category")
                                print("1. Frontliner (Major)")
                                print("2. Frontliner (Minor)")
                                print("3. Midliner (Major)")
                                print("4. Midliner (Minor)")
                                print("5. Backliner")
                                Category = input(">> ")
                                if Category == "1":
                                    user.Category = "Frontliner (Major)"
                                    user.Priority = "5"
                                    CategoryFlag = False
                                elif Category == "2":
                                    user.Category = "Frontliner (Minor)"
                                    user.Priority = "4"
                                    CategoryFlag = False
                                elif Category == "3":
                                    user.Category = "Midliner (Major)"
                                    user.Priority = "3"
                                    CategoryFlag = False
                                elif Category == "4":
                                    user.Category = "Midliner (Minor)"
                                    user.Priority = "2"
                                    CategoryFlag = False
                                elif Category == "5":
                                    user.Category = "Backliner"
                                    user.Priority = "1"
                                    CategoryFlag = False
                                    
                                else:
                                    print("Invalid Input")
                                    print("\n")
                            StatusFlag = True
                            while StatusFlag:
                                print("Enter New Covid Status")
                                print("1. Normal")
                                print("2. Under Quarantine")
                                print("3. Covid Positive")
                                Status = input(">> ")
                                if Status == "1":
                                    user.Status = "Normal"
                                    StatusFlag = False
                                elif Status == "2":
                                    user.Status = "Quarantine"
                                    StatusFlag = False
                                elif Status == "3":
                                    user.Status = "Covid"
                                    StatusFlag = False
                                else:
                                    print("Invalid Input")
                                    print("\n")
                            user.Password = input("Enter New Password: ")
                            if user.Name not in Empty and user.Age not in Empty and user.Address not in Empty and user.PostCode not in Empty and user.PhoneNum not in Empty and user.Occupation not in Empty and user.Password not in Empty:
                                database.update_user()
                                InfoNotEmpty = False
                                print( "\n" * 35 )
                            else:
                                print( "\n" * 35 )
                                print("Input Cannot Be Empty")
                                print("\n")

                    elif ViewInfoInput == "2": # Back
                        ViewInfoFlag = False
                        print( "\n" * 35 )

                    else:
                        print( "\n" * 35 )
                        print("Invalid Input\n")

            elif UserAction == "3": # ---------------------------------------------------------------------------------(3. View Appointment)
                print( "\n" * 35 )
                ViewAppointmentFlag = True
                while ViewAppointmentFlag:
                    print("---View Appointment---")
                    print("Vaccine Status                  : " + user.VaccStatus)
                    print("Vaccination Appointment Location: " + user.VaccCenter)
                    print("Vaccination Appointment Date    : " + user.VaccDate)
                    print("Vaccination Time                : " + user.VaccTime)
                    print("RSVP Vaccination                : " + user.Rsvp)
                    print("\n------------------------------------------------------------")
                    print("1. Respond to RSVP.")
                    print("2. Back.")
                    print("------------------------------------------------------------\n")
                    print("Enter A Number To Proceed.")
                    ViewAppointmentInput = input(">> ")

                    if ViewAppointmentInput == "1": # Respond RSVP (RsvpFlag = True)

                        RsvpFlag = True
                        while RsvpFlag:
                            print( "\n" * 35 )
                            if user.VaccStatus == "Vaccinated":
                                print( "\n" * 35 )
                                RsvpFlag = False
                                print("You Had Been Vaccinated.")
                                print("\n------------------------------------------------------------")
                                print("Press Enter To Continue.")
                                print("------------------------------------------------------------\n")
                                EnterInput = input("")
                                print( "\n" * 35 )

                            elif user.Rsvp == "Yes":    
                                RsvpFlag = False
                                print( "\n" * 35 )
                                print("The Appointment Is Already Accepted.")
                                print("\n------------------------------------------------------------")
                                print("Press Enter To Continue.")
                                print("------------------------------------------------------------\n")
                                EnterInput = input("")
                                print( "\n" * 35 )
                                
                            elif user.VaccStatus == "Assigned" and user.Rsvp == "-":
                                print("1. Accept")
                                print("2. Decline")
                                print("\n------------------------------------------------------------")
                                print("Enter A Number To Proceed.")
                                print("------------------------------------------------------------\n")
                                RsvpInput = input(">> ")

                                if RsvpInput == "1":
                                    print( "\n" * 35 )
                                    user.Rsvp = "Yes"
                                    database.update_user()
                                    RsvpFlag = False
                                    print("Appointment Accepted.")
                                    print("\n------------------------------------------------------------")
                                    print("Press Enter To Continue.")
                                    print("------------------------------------------------------------\n")
                                    EnterInput = input("")
                                    print( "\n" * 35 )

                                elif RsvpInput == "2":
                                    print( "\n" * 35 )
                                    user.VaccStatus = "-"
                                    user.Rsvp = "-"
                                    user.VaccCenter = "-"
                                    user.VaccDate = "-"
                                    user.VaccTime = "-"
                                    database.update_user()
                                    RsvpFlag = False
                                    print("Appointment Declined.")
                                    print("\n------------------------------------------------------------")
                                    print("Press Enter To Continue.")
                                    print("------------------------------------------------------------\n")
                                    EnterInput = input("")
                                    print( "\n" * 35 )

                                else: # (RsvpFlag = True)
                                    print("Invalid Input\n")
                            
                            else:
                                database = UserData()
                                print( "\n" * 35 )
                                RsvpFlag = False
                                print("You Have No Appointment Yet.\n")
                                print("\n------------------------------------------------------------")
                                print("Press Enter To Continue.")
                                print("------------------------------------------------------------\n")
                                EnterInput = input("")
                                print( "\n" * 35 )

                    elif ViewAppointmentInput == "2":
                        RsvpFlag = False
                        ViewAppointmentFlag = False
                        print( "\n" * 35 )
                    
                    else:
                        print( "\n" * 35 )
                        print("Invalid Input\n")
            
            elif UserAction == "4":
                print( "\n" * 35 )
                print("Successfully Logged Out")
                print("\n------------------------------------------------------------")
                print("Press Enter To Continue.")
                print("------------------------------------------------------------\n")
                EnterInput = input("")
                UserFlag = False
                database.update_user()
                print( "\n" * 35 )
                app = SampleApp()
                app.mainloop()
            
            else:
                print( "\n" * 35 )
                print("Invalid Input\n")
    except:
        print("Something Went Wrong.. :(") 


# =================================================================================================================================================================== #
# =================================================================================================================================================================== #
# =================================================================================================================================================================== #
# ADMIN PAGE / INTERFACE
# SHAKTISH


def AdminPage(Name):
    print( "\n" * 35 )
    print("Login successful.")
    print("")
    print("Welcome back, " + Name + ".")
    print("\n")
    AdminFlag = True
    while AdminFlag:
        print("---Admin Menu---")
        print("1. Assign Appointment")               # Assign appointment
        print("2. View & Add Vaccination Center")    # VIew and add VaccCenter
        print("3. Generate User List")               # Sorting users
        print("4. Log Out")
        print("\n------------------------------------------------------------")
        print("Enter A Number To Proceed.")
        print("------------------------------------------------------------\n")
        AdminAction = input(">> ")
        print("\n")
        if AdminAction == "1":
            Appointment()
        elif AdminAction == "2":
            VaccCenter()
        elif AdminAction == "3":
            List()
        elif AdminAction == "4":
            AdminFlag = False
            print( "\n" * 35 )
            print("Successfully Logged Out")
            print("\n------------------------------------------------------------")
            print("Press Enter To Continue.")
            print("------------------------------------------------------------\n")
            EnterInput = input("")
            print( "\n" * 35 )
            app = SampleApp()
            app.mainloop()
        else:
            print( "\n" * 35 )
            print("Invalid Input")
            print("\n")


def Appointment(): # ------------------------------------------------------------------------------------------------(1. Assign Appointment)
    print( "\n" * 35 )
    AppointFlag = True
    while AppointFlag:
        print("Enter User's IC Number: ")
        UserIc = input(">> ")
        
        database = UserData()
        user = database.get_user(UserIc)
        try:
            if user.Ic == UserIc:
                if user.VaccStatus == "Assigned":
                    print( "\n" *35 )
                    print("This User Has Assigned Vaccination Appointment.")
                    AssignFlag = True
                    while AssignFlag:
                        print("\n------------------------------------------------------------")
                        print("1. Assign Another User.")
                        print("2. Back.")
                        print("------------------------------------------------------------\n")
                        print("Enter A Number To Proceed.")
                        AssignInput = input(">> ")
                        if AssignInput == "1":
                            AssignFlag = False
                            print( "\n" *35 )
                        elif AssignInput == "2":
                            AssignFlag = False
                            AppointFlag = False
                            print( "\n" *35 )
                        else:
                            print( "\n" *35 )
                            print("Invalid Input")

                
                elif user.VaccStatus == "Vaccinated":
                    print( "\n" *35 )
                    print("This User Is Vaccinated.")
                    AssignFlag = True
                    while AssignFlag:
                        print("\n------------------------------------------------------------")
                        print("1. Assign Another User.")
                        print("2. Back.")
                        print("------------------------------------------------------------\n")
                        print("Enter A Number To Proceed.")
                        AssignInput = input(">> ")
                        if AssignInput == "1":
                            AssignFlag = False
                            print( "\n" *35 )
                        elif AssignInput == "2":
                            AssignFlag = False
                            AppointFlag = False
                            print( "\n" *35 )
                        else:
                            print( "\n" *35 )
                            print("Invalid Input")

                else:
                    Center = AssignVaccCenter(UserIc)
                    Date, Time = AssignVaccDateTime(UserIc)

                    user.VaccStatus = "Assigned"
                    user.VaccCenter = Center
                    user.VaccDate = Date
                    user.VaccTime = Time
                    database.update_user()

                    print( "\n" *35 )
                    print("Appointment Assigned Succesfully")
                    print("\n------------------------------------------------------------")
                    print("Press Enter To Continue.")
                    print("------------------------------------------------------------\n")
                    EnterInput = input("")
                    AppointFlag = False
                    print( "\n" *35 )
            else:
                print( "\n" *35 )
                print("User Ic Doesn't Exist.")
                AssignFlag = True
                while AssignFlag:
                    print("\n------------------------------------------------------------")
                    print("1. Assign Another User.")
                    print("2. Back.")
                    print("------------------------------------------------------------\n")
                    print("Enter A Number To Proceed.")
                    AssignInput = input(">> ")
                    if AssignInput == "1":
                        AssignFlag = False
                        print( "\n" *35 )
                    elif AssignInput == "2":
                        AssignFlag = False
                        AppointFlag = False
                        print( "\n" *35 )
                    else:
                        print( "\n" *35 )
                        print("Invalid Input")
        except:
            print( "\n" *35 )
            print("User Ic Doesn't Exist.")
            AssignFlag = True
            while AssignFlag:
                print("\n------------------------------------------------------------")
                print("1. Assign Another User.")
                print("2. Back.")
                print("------------------------------------------------------------\n")
                print("Enter A Number To Proceed.")
                AssignInput = input(">> ")
                if AssignInput == "1":
                    AssignFlag = False
                    print( "\n" *35 )
                elif AssignInput == "2":
                    AssignFlag = False
                    AppointFlag = False
                    print( "\n" *35 )
                else:
                    print( "\n" *35 )
                    print("Invalid Input")
# -----TESTING-----
# print("Vaccination Center = " + user.VaccCenter)
# print("Vaccination Date = " + user.VaccDate)
# print("Vaccination Time = " + user.VaccTime)


def AssignVaccCenter(Ic):
    database = UserData()
    user = database.get_user(Ic)

    Centers = []
    Rates = []
    Nums = []

    # Load Centers into lists
    with open("VaccCenter.txt", "r") as file:

        # Appending Centers and Rates
        for i in file:
            Center, Rate = i.split(", ")
            Rate = Rate.strip()
            Centers.append(Center)
            Rates.append(Rate)
        Rates = [float(rate) for rate in Rates]
        Vacc = dict(zip(Centers, Rates))

        # Appending Nums
        for num in range (len(Centers)):
            num = num + 1
            Nums.append(num)

    # Choosing Vaccination Center
    print( "\n" *35 )
    VaccCenterFlag = True
    while VaccCenterFlag:
        for num in Nums:
            Hour = Rates[num - 1]
            Day = Rates[num - 1]*24
            print("{number}. Vaccination Center  : {location}".format(number = num, location = Centers[num - 1]))
            print("   Rate of vaccination : {hour} Vaccinator/Hour, {day:.1f} Vaccinator/Day".format(hour = Hour, day = Day))
            print("\n")
        print("------------------------------------------------------------")
        print("Select A Vaccination Center Number")
        print("------------------------------------------------------------\n")
        VaccNum = input(">> ")

        # checking if input is digit & in Nums
        if VaccNum.isdigit() == True:
            VaccNum = int(VaccNum)
            while VaccNum not in Nums:
                print( "\n" *35 )
                print("Please Enter A Valid Number")
                print("\n")
                for num in Nums:
                    Hour = Rates[num - 1]
                    Day = Rates[num - 1]*24
                    print("{number}. Vaccination Center  : {location}".format(number = num, location = Centers[num - 1]))
                    print("   Rate of vaccination : {hour} Vaccinator/Hour, {day:.1f} Vaccinator/Day".format(hour = Hour, day = Day))
                    print("\n")
                print("------------------------------------------------------------")
                print("Select A Vaccination Center Number")
                print("------------------------------------------------------------\n")
                VaccNum = input(">> ")
                if VaccNum.isdigit() == True:
                    VaccNum = int(VaccNum)
                else:
                    pass
        else:
            # checking if input is in Nums
            while VaccNum not in Nums:
                print( "\n" *35 )
                print("Please Enter A Valid Number")
                print("\n")
                for num in Nums:
                    Hour = Rates[num - 1]
                    Day = Rates[num - 1]*24
                    print("{number}. Vaccination Center  : {location}".format(number = num, location = Centers[num - 1]))
                    print("   Rate of vaccination : {hour} Vaccinator/Hour, {day:.1f} Vaccinator/Day".format(hour = Hour, day = Day))
                    print("\n")
                print("------------------------------------------------------------")
                print("Select A Vaccination Center Number")
                print("------------------------------------------------------------\n")
                VaccNum = input(">> ")
                if VaccNum.isdigit() == True:
                    VaccNum = int(VaccNum)
                else:
                    pass

        # Checking if input is in selection
        print( "\n" *35 )
        ConfirmCenter = True
        while ConfirmCenter:
            for num in Nums:
                Hour = Rates[num - 1]
                Day = Rates[num - 1]*24
                if VaccNum == num:
                    print("Vaccination Center Chosen")
                    print("\n")
                    print("Vaccination Center  : {location}".format(number = VaccNum, location = Centers[VaccNum - 1]))
                    print("Rate of vaccination : {hour} Vaccinator/Hour, {day:.1f} Vaccinator/Day".format(hour = Hour, day = Day))
                    print("------------------------------------------------------------")
                    print("Confirm Selection")
                    print("1. Confirm")
                    print("2. Back")
                    print("------------------------------------------------------------\n")
                    VaccInput = input(">> ")

                    if VaccInput == "1":
                        user.VaccCenter = Centers[VaccNum - 1]
                        ConfirmCenter = False
                        VaccCenterFlag = False
                        print( "\n" *35 )
                        return user.VaccCenter
                    elif VaccInput == "2":
                        ConfirmCenter = False
                        print( "\n" *35 )
                    else:
                        print( "\n" *35 )
                        print("Invalid Input")
                        print("\n")
                else:
                    pass


        # -----TESTING-----
        # print(user.VaccCenter)
        # print("\n")
        # print("Vaccination Center Assigned")


def AssignVaccDateTime(Ic):
    database = UserData()
    user = database.get_user(Ic)

    DateTimeFlag = True
    while DateTimeFlag:
        print( "\n" *35 )
        print("Enter Vaccination Date xx/xx/xxxx")
        user.VaccDate = input(">> ")
        print("Enter Vaccination Time (24 Hour System, 00:00)")
        user.VaccTime = input(">> ")
        
        ComfirmDateTime = True
        while ComfirmDateTime:
            print( "\n" *35 )
            print("Vaccination Date: " + user.VaccDate)
            print("Vaccination Time: " + user.VaccTime)
            print("------------------------------------------------------------")
            print("Confirm Date & Time")
            print("1. Confirm")
            print("2. Back")
            print("------------------------------------------------------------\n")
            VaccInput = input(">> ")
            if VaccInput == "1":
                ComfirmDateTime = False
                DateTimeFlag = False
                return user.VaccDate, user.VaccTime;
            elif VaccInput == "2":
                ComfirmDateTime = False
                pass
            else:
                print("Invalid Input")
                print("\n")


def VaccCenter(): # ------------------------------------------------------------------------------------(2. View and Add Vaccination Center)
    print( "\n" *35 )
    VaccCenterFlag = True
    while VaccCenterFlag:
        print("---View & Add Vaccination Center---")
        print("1. View Vaccination Centers")
        print("2. Add Vaccination Centers")
        print("3. Back")
        print("\n------------------------------------------------------------")
        print("Enter A Number To Proceed.")
        print("------------------------------------------------------------\n")
        UpdateVaccInput = input(">> ")

        if UpdateVaccInput == "1":
            ViewVaccCenter()

        elif UpdateVaccInput == "2":
            print( "\n" *35 )
            NotEmptyFlag = True
            while NotEmptyFlag:
                print("Enter New Vaccination Center Location : ")
                center = input(">> ")
                print("Enter The Rate of Vaccination (Vaccinator/Hour): ")
                rate = input(">> ")
                if center not in Empty and rate not in Empty:
                    with open("VaccCenter.txt", "a") as file:
                        file.write("\n" + center + ", " + rate)
                    print("\n")
                    print("New Vaccination Center Added Successfully!")
                    print("\n------------------------------------------------------------")
                    print("Press Enter To Continue.")
                    print("------------------------------------------------------------\n")
                    EnterInput = input("")
                    NotEmptyFlag = False
                    print( "\n" *35 )
                else:
                    print( "\n" *35 )
                    AddVaccFlag = True
                    while AddVaccFlag:
                        print("Inputs cannot be empty.")
                        print("")
                        print("1. Try Add Vaccination Centers Again")
                        print("2. Back")
                        print("\n------------------------------------------------------------")
                        print("Enter A Number To Proceed.")
                        print("------------------------------------------------------------\n")
                        AddVaccInput = input(">> ")
                        if AddVaccInput == "1":
                            AddVaccFlag = False
                            print( "\n" *35 )
                        elif AddVaccInput == "2":
                            AddVaccFlag = False
                            NotEmptyFlag = False
                            print( "\n" *35 )
                        else:
                            print( "\n" *35 )
                            print("Invalid Input")
                            print("\n")

        elif UpdateVaccInput == "3":
            VaccCenterFlag = False
            print( "\n" *35 )

        else:
            print( "\n" *35 )
            print("Invalid Input")
            print("\n")


def ViewVaccCenter():
    # Load Centers Rates & Nums into lists
    with open("VaccCenter.txt", "r") as file:
        Centers =[]
        Rates = []
        Nums = []

        # Appending Centers and Rates
        for i in file:
            Center, Rate = i.split(", ")
            Rate = Rate.strip()
            Centers.append(Center)
            Rates.append(Rate)
        Rates = [float(rate) for rate in Rates]
        Vacc = dict(zip(Centers, Rates))

        # Appending Nums
        for num in range (len(Centers)):
            num = num + 1
            Nums.append(num)

        print( "\n" *35 )
        for num in Nums:
            Hour = Rates[num - 1]
            Day = Rates[num - 1]*24
            print("{number}. Vaccination Center  : {location}".format(number = num, location = Centers[num - 1]))
            print("   Rate of vaccination : {hour} Vaccinator/Hour, {day:.1f} Vaccinator/Day".format(hour = Hour, day = Day))
            print("\n")
        print("------------------------------------------------------------")
        print("Press Enter To Continue.")
        print("------------------------------------------------------------\n")
        EnterInput = input("")
        print( "\n" *35 )


def List(): # ------------------------------------------------------------------------------------------------------(3. Generate User List)
    print( "\n" * 35 )
    SortUserFlag = True
    while SortUserFlag:
        print("---List Users---")
        print("1. View All Users")
        print("2. View Assigned Users")
        print("3. Sort By Age")
        print("4. Sort By Risk Group")
        print("5. Sort By Priority")
        print("6. Sort By Postcode")
        print("7. Sort By Vaccination Status")
        print("8. Sort By RSVP")
        print("9. Return To Admin Menu")
        print("\n------------------------------------------------------------")
        print("Enter A Number To Proceed.")
        print("------------------------------------------------------------\n")
        x = input(">> ")
        print("\n")
        if x == "1":
            sort_all_user()
        elif x == "2":
            sort_assigned_user()
        elif x == "3":
            sort_user_age()
            print("\n")
        elif x == "4":
            sort_user_risk()
            print("\n")
        elif x == "5":
            sort_user_priority()
            print("\n")
        elif x == "6":
            sort_user_postcode()
            print("\n")
        elif x == "7":
            sort_user_status()
            print("\n")
        elif x == "8":
            sort_user_rsvp()
            print("\n")
        elif x == "9":
            SortUserFlag = False
            print( "\n" * 35 )
        else:
            print( "\n" * 35 )
            print("Invalid Input")
            print("\n")
        # Dont Have As Option (Name Age Ic Category Address Password Occupation)


# Function to view all user information
def sort_all_user():
    info = user()
    userName  = sorted(info, key = lambda k: k["Ic"], reverse= False)
    userName  = userName[:]
    print( "\n" * 35 )
    print ("{:<10} {:<4} {:<11} {:<8} {:<11} {:<14} {:<11} {:<18} {:<10} {:<8} {:<11} {:<38} {:<10} {:<9} {:<6}".format('Name', 'Age', 'Ic', 'PostCode', 'Phone Num', 'Occupation', 'Status', 'Category', 'Risk Group', 'Priority', 'Vacc Status', 'Vaccination Center', 'Vacc Date', 'Vacc Time', 'Rsvp'))
    print ("{:<10} {:<4} {:<11} {:<8} {:<11} {:<14} {:<11} {:<18} {:<10} {:<8} {:<11} {:<38} {:<10} {:<9} {:<6}".format('-'*10, '-'*4, '-'*11, '-'*8, '-'*11, '-'*14, '-'*11, '-'*18, '-'*10, '-'*8, '-'*11, '-'*38, '-'*10, '-'*9, '-'*6))
    for i in userName:
        Name = i["Name"]              #{:<10}   '-'*10
        Age = i["Age"]                #{:<4}    '-'*4
        Ic = i["Ic"]                  #{:<10}   '-'*10
        PostCode = i["PostCode"]      #{:<8}    '-'*8
        PhoneNum = i["PhoneNum"]      #{:<11}   '-'*11
        Occupation = i["Occupation"]  #{:<14}   '-'*14
        Status = i["Status"]          #{:<11}   '-'*11
        Category = i["Category"]      #{:<18}   '-'*18
        MedHistory = i["MedHistory"]  #{:<10}   '-'*10
        Priority = i["Priority"]      #{:<8}    '-'*8
        VaccStatus = i["VaccStatus"]  #{:<11}   '-'*11
        VaccCenter = i["VaccCenter"]  #{:<38}   '-'*38
        VaccDate = i["VaccDate"]      #{:<10}   '-'*10
        VaccTime = i["VaccTime"]      #{:<9}    '-'*9
        Rsvp = i["Rsvp"]              #{:<6}    '-'*6
        print ("{:<10} {:<4} {:<11} {:<8} {:<11} {:<14} {:<11} {:<18} {:<10} {:<8} {:<11} {:<38} {:<10} {:<9} {:<6}".format(Name, Age, Ic, PostCode, PhoneNum, Occupation, Status, Category, MedHistory, Priority, VaccStatus, VaccCenter, VaccDate, VaccTime, Rsvp))
        # print("")
    print("\n------------------------------------------------------------")
    print("Press Enter To Continue.")
    print("------------------------------------------------------------\n")
    EnterInput = input("")
    print( "\n" *35 )

# -----TESTING-----
# sort_all_user()


# Function to sort users by assigned
def sort_assigned_user():
    print( "\n" *35 )
    info = user()
    userDate = sorted(info, key = lambda k: (k['VaccDate'], k['VaccTime']), reverse= True)
    userDate = userDate[:]
    print("Assigned Users \n")
    print ("{:<11} {:<10} {:<12} {:<11} {:<11} {:<11} {:<38} {:<11} {:<9} {:<6}".format('Ic', 'Name', 'Phone Num', 'Risk Group', 'Status', 'Vacc Status', 'Vaccination Center', 'Vacc Date', 'Vacc Time', 'Rsvp'))
    print ("{:<11} {:<10} {:<12} {:<11} {:<11} {:<11} {:<38} {:<11} {:<9} {:<6}".format('-'*11, '-'*10, '-'*12, '-'*11, '-'*11, '-'*11, '-'*38, '-'*11, '-'*9, '-'*6))
    for i in userDate:
        Ic = i["Ic"]                  #{:<11}   '-'*11
        Name = i["Name"]              #{:<10}   '-'*10
        PhoneNum = i["PhoneNum"]      #{:<12}   '-'*12
        MedHistory = i["MedHistory"]  #{:<11}   '-'*11
        Status = i["Status"]          #{:<11}   '-'*11
        VaccStatus = i["VaccStatus"]  #{:<11}   '-'*11
        VaccCenter = i["VaccCenter"]  #{:<38}   '-'*38
        VaccDate = i["VaccDate"]      #{:<11}   '-'*11
        VaccTime = i["VaccTime"]      #{:<9}    '-'*9
        Rsvp = i["Rsvp"]              #{:<6}    '-'*6
        if VaccStatus == "Assigned":                            # Only prints "Assigned" users
            print ("{:<11} {:<10} {:<12} {:<11} {:<11} {:<11} {:<38} {:<11} {:<9} {:<6}".format(Ic, Name, PhoneNum, MedHistory, Status, VaccStatus, VaccCenter, VaccDate, VaccTime, Rsvp))
    print("\n------------------------------------------------------------")
    print("Press Enter To Continue.")
    print("------------------------------------------------------------\n")
    EnterInput = input("")
    print( "\n" *35 )

# -----TESTING-----
# sort_assigned_user()


# Function to sort users by Age
def sort_user_age():
    print( "\n" *35 )
    AgeFlag = True
    while AgeFlag:
        print("Age")
        print("1. Lower To Higher")
        print("2. Higher To Lower")
        print("\n------------------------------------------------------------")
        print("Enter A Number To Proceed.")
        print("------------------------------------------------------------\n")
        x = input(">> ")
        if x == "1":
            info = user()
            userAge  = sorted(info, key = lambda k: k["Age"], reverse= False)
            userAge  = userAge[:]
            print( "\n" *35 )
            print("Age - Lower To Higher\n")
            print ("{:<11} {:<10} {:<4} {:<11}".format('Ic', 'Name', 'Age', 'Vacc Status'))
            print ("{:<11} {:<10} {:<4} {:<11}".format('-'*11, '-'*10, '-'*4, '-'*11))
            for i in userAge:
                Name = i["Name"]              #{:<10}   '-'*10
                Age = i["Age"]                #{:<4}    '-'*4
                Ic = i["Ic"]                  #{:<11}   '-'*11
                VaccStatus = i["VaccStatus"]  #{:<11}   '-'*11
                print ("{:<11} {:<10} {:<4} {:<11}".format(Ic, Name, Age, VaccStatus))
            print("\n------------------------------------------------------------")
            print("Press Enter To Continue.")
            print("------------------------------------------------------------\n")
            EnterInput = input("")
            AgeFlag = False
            print( "\n" *35 )
        elif x == "2":
            info = user()
            userAge  = sorted(info, key = lambda k: k["Age"], reverse= True)
            userAge  = userAge[:]
            print( "\n" *35 )
            print("Age - Higher To Lower\n")
            print ("{:<11} {:<10} {:<4} {:<11}".format('Ic', 'Name', 'Age', 'Vacc Status'))
            print ("{:<11} {:<10} {:<4} {:<11}".format('-'*11, '-'*10, '-'*4, '-'*11))
            for i in userAge:
                Name = i["Name"]              #{:<10}   '-'*10
                Age = i["Age"]                #{:<4}    '-'*4
                Ic = i["Ic"]                  #{:<11}   '-'*11
                VaccStatus = i["VaccStatus"]  #{:<11}   '-'*11
                print ("{:<11} {:<10} {:<4} {:<11}".format(Ic, Name, Age, VaccStatus))
            print("\n------------------------------------------------------------")
            print("Press Enter To Continue.")
            print("------------------------------------------------------------\n")
            EnterInput = input("")
            AgeFlag = False
            print( "\n" *35 )
        else:
            print( "\n" *35 )
            print("Invalid Input")
            print("\n")

# -----TESTING-----
# sort_user_age()


# Function sorts users by High Risk and Low Risk
def sort_user_risk():
    print( "\n" *35 )
    RiskFlag = True
    while RiskFlag:
        print("Risk")
        print("1. Low Risk To High Risk")
        print("2. High Risk To Low Risk")
        print("\n------------------------------------------------------------")
        print("Enter A Number To Proceed.")
        print("------------------------------------------------------------\n")
        x = input(">> ")
        if x == "1":
            info = user()
            userRisk = sorted(info, key = lambda k: k["MedHistory"], reverse= True)
            userRisk = userRisk[:]
            print( "\n" *35 )
            print("Risk Group - Low To High\n")
            print ("{:<11} {:<10} {:<11} {:<11}".format('Ic', 'Name', 'Risk Group', 'Vacc Status'))
            print ("{:<11} {:<10} {:<11} {:<11}".format('-'*11, '-'*10, '-'*11, '-'*11))
            for i in userRisk:
                Ic = i["Ic"]                  #{:<11}   '-'*11
                Name = i["Name"]              #{:<10}   '-'*10
                MedHistory = i["MedHistory"]  #{:<11}   '-'*11
                VaccStatus = i["VaccStatus"]  #{:<11}   '-'*11
                print ("{:<11} {:<10} {:<11} {:<11}".format(Ic, Name, MedHistory, VaccStatus))
            print("\n------------------------------------------------------------")
            print("Press Enter To Continue.")
            print("------------------------------------------------------------\n")
            EnterInput = input("")
            RiskFlag = False
            print( "\n" *35 )
        elif x == "2":
            info = user()
            userRisk = sorted(info, key = lambda k: k["MedHistory"], reverse= False)
            userRisk = userRisk[:]
            print( "\n" *35 )
            print("Risk Group - High To Low\n")
            print ("{:<11} {:<10} {:<11} {:<11}".format('Ic', 'Name', 'Risk Group', 'Vacc Status'))
            print ("{:<11} {:<10} {:<11} {:<11}".format('-'*11, '-'*10, '-'*11, '-'*11))
            for i in userRisk:
                Ic = i["Ic"]                  #{:<11}   '-'*11
                Name = i["Name"]              #{:<10}   '-'*10
                MedHistory = i["MedHistory"]  #{:<11}   '-'*11
                VaccStatus = i["VaccStatus"]  #{:<11}   '-'*11
                print ("{:<11} {:<10} {:<11} {:<11}".format(Ic, Name, MedHistory, VaccStatus))
            print("\n------------------------------------------------------------")
            print("Press Enter To Continue.")
            print("------------------------------------------------------------\n")
            EnterInput = input("")
            RiskFlag = False
            print( "\n" *35 )
        else:
            print( "\n" *35 )
            print("Invalid Input")
            print("\n")

# -----TESTING-----
# sort_user_risk()


# Function sorts users by Priority
def sort_user_priority():
    print( "\n" *35 )
    PriorityFlag = True
    while PriorityFlag:
        print("Priority")
        print("1. 1 To 5")
        print("2. 5 To 1")
        print("\n------------------------------------------------------------")
        print("Enter A Number To Proceed.")
        print("------------------------------------------------------------\n")
        x = input(">> ")
        if x == "1":
            database = UserData()
            info = user()
            userPr = sorted(info, key = lambda k: k["Priority"], reverse= False)
            userPr = userPr[:]
            print( "\n" *35 )
            print("Priority - 1 to 5\n")
            print ("{:<11} {:<10} {:<18} {:<9} {:<11}".format('Ic', 'Name', 'Category', 'Priority', 'Vacc Status'))
            print ("{:<11} {:<10} {:<18} {:<9} {:<11}".format('-'*11, '-'*10, '-'*18, '-'*9, '-'*11))
            for i in userPr:
                Ic = i["Ic"]                  #{:<11}   '-'*11
                Name = i["Name"]              #{:<10}   '-'*10
                Category = i["Category"]      #{:<18}   '-'*18
                Priority = i["Priority"]      #{:<9}    '-'*9
                VaccStatus = i["VaccStatus"]  #{:<11}   '-'*11
                print ("{:<11} {:<10} {:<18} {:<9} {:<11}".format(Ic, Name, Category, Priority, VaccStatus))
            print("\n------------------------------------------------------------")
            print("Press Enter To Continue.")
            print("------------------------------------------------------------\n")
            EnterInput = input("")
            PriorityFlag = False
            print( "\n" *35 )
        elif x == "2":
            database = UserData()
            info = user()
            userPr = sorted(info, key = lambda k: k["Priority"], reverse= True)
            userPr = userPr[:]
            print( "\n" *35 )
            print("Priority - 5 to 1\n")
            print ("{:<11} {:<10} {:<18} {:<9} {:<11}".format('Ic', 'Name', 'Category', 'Priority', 'Vacc Status'))
            print ("{:<11} {:<10} {:<18} {:<9} {:<11}".format('-'*11, '-'*10, '-'*18, '-'*9, '-'*11))
            for i in userPr:
                Ic = i["Ic"]                  #{:<11}   '-'*11
                Name = i["Name"]              #{:<10}   '-'*10
                Category = i["Category"]      #{:<18}   '-'*18
                Priority = i["Priority"]      #{:<9}    '-'*9
                VaccStatus = i["VaccStatus"]  #{:<11}   '-'*11
                print ("{:<11} {:<10} {:<18} {:<9} {:<11}".format(Ic, Name, Category, Priority, VaccStatus))
            print("\n------------------------------------------------------------")
            print("Press Enter To Continue.")
            print("------------------------------------------------------------\n")
            EnterInput = input("")
            PriorityFlag = False
            print( "\n" *35 )
        else:
            print( "\n" *35 )
            print("Invalid Input")
            print("\n")

# -----TESTING-----
# sort_user_priority()


# Function to sort users by PostCode
def sort_user_postcode():
    print( "\n" *35 )
    PostCodeFlag = True
    while PostCodeFlag:
        print("PostCode")
        print("1. Lower To Higher")
        print("2. Higher To Lower")
        print("\n------------------------------------------------------------")
        print("Enter A Number To Proceed.")
        print("------------------------------------------------------------\n")
        x = input(">> ")
        if x == "1":
            print( "\n" *35 )
            database = UserData()
            info = user()
            userPostCode  = sorted(info, key = lambda k: k["PostCode"], reverse= False)
            userPostCode  = userPostCode[:]
            print("PostCode - Lower To Higher\n")
            print ("{:<11} {:<10} {:<9} {:<11}".format('Ic', 'Name', 'PostCode', 'Vacc Status'))
            print ("{:<11} {:<10} {:<9} {:<11}".format('-'*11, '-'*10, '-'*9, '-'*11))
            for i in userPostCode:
                Ic = i["Ic"]                  #{:<11}   '-'*11
                Name = i["Name"]              #{:<10}   '-'*10
                PostCode = i["PostCode"]      #{:<9}    '-'*9
                VaccStatus = i["VaccStatus"]  #{:<11}   '-'*11
                print ("{:<11} {:<10} {:<9} {:<11}".format(Ic, Name, PostCode, VaccStatus))
            print("\n------------------------------------------------------------")
            print("Press Enter To Continue.")
            print("------------------------------------------------------------\n")
            EnterInput = input("")
            PostCodeFlag = False
            print( "\n" *35 )
        elif x == "2":
            print( "\n" *35 )
            database = UserData()
            info = user()
            userPostCode  = sorted(info, key = lambda k: k["PostCode"], reverse= True)
            userPostCode  = userPostCode[:]
            print("PostCode - Higher To Lower\n")
            print ("{:<11} {:<10} {:<9} {:<11}".format('Ic', 'Name', 'PostCode', 'Vacc Status'))
            print ("{:<11} {:<10} {:<9} {:<11}".format('-'*11, '-'*10, '-'*9, '-'*11))
            for i in userPostCode:
                Ic = i["Ic"]                  #{:<11}   '-'*11
                Name = i["Name"]              #{:<10}   '-'*10
                PostCode = i["PostCode"]      #{:<9}    '-'*9
                VaccStatus = i["VaccStatus"]  #{:<11}   '-'*11
                print ("{:<11} {:<10} {:<9} {:<11}".format(Ic, Name, PostCode, VaccStatus))
            print("\n------------------------------------------------------------")
            print("Press Enter To Continue.")
            print("------------------------------------------------------------\n")
            EnterInput = input("")
            PostCodeFlag = False
            print( "\n" *35 )
        else:
            print( "\n" *35 )
            print("Invalid Input")
            print("\n")

# -----TESTING-----
# sort_user_postcode()


# Function sorts users by ASSIGNED USERS and NOT ASSIGNED USERS
def sort_user_status():
    print( "\n" *35 )
    database = UserData()
    info = user()
    userStatus = sorted(info, key = lambda k: k["VaccStatus"], reverse= True)
    userStatus = userStatus[:]
    print("Vaccination Status - Vaccinated > Assigned > Not Assigned \n")
    print ("{:<11} {:<10} {:<11}".format('Ic', 'Name', 'Vacc Status'))
    print ("{:<11} {:<10} {:<11}".format('-'*11, '-'*10, '-'*11))
    for i in userStatus:
        Ic = i["Ic"]                  #{:<11}   '-'*11
        Name = i["Name"]              #{:<10}   '-'*10
        VaccStatus = i["VaccStatus"]  #{:<11}   '-'*11
        print ("{:<11} {:<10} {:<11}".format(Ic, Name, VaccStatus))
    print("\n------------------------------------------------------------")
    print("Press Enter To Continue.")
    print("------------------------------------------------------------\n")
    EnterInput = input("")
    print( "\n" *35 )

# -----TESTING-----
# sort_user_status()


# Function to sort users who agree on date of appointment or not
def sort_user_rsvp():
    print( "\n" *35 )
    database = UserData 
    info = user()
    userRsvp = sorted(info, key = lambda k: k["Rsvp"], reverse= True)
    userRsvp = userRsvp[:]
    print("RSVP : Yes | No\n")
    print ("{:<11} {:<10} {:<6}".format('Ic', 'Name', 'Rsvp'))
    print ("{:<11} {:<10} {:<6}".format('-'*11, '-'*10, '-'*9, '-'*11))
    for i in userRsvp:
        Ic = i["Ic"]                  #{:<11}   '-'*11
        Name = i["Name"]              #{:<10}   '-'*10
        Rsvp = i["Rsvp"]              #{:<6}    '-'*6
        VaccStatus = i["VaccStatus"]  #{:<11}   '-'*11
        print ("{:<11} {:<10} {:<6}".format(Ic, Name, Rsvp))
    print("\n------------------------------------------------------------")
    print("Press Enter To Continue.")
    print("------------------------------------------------------------\n")
    EnterInput = input("")
    print( "\n" *35 )

# -----TESTING-----
# sort_user_rsvp()


# To make sure the window can loop
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()


