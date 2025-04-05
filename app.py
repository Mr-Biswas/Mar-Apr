
import tkinter as tk
from tkinter import StringVar, Label, Entry, Button, Toplevel
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from tkinter import messagebox
import tkinter


class MultiWindowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VBFT Project")
        self.root.geometry("400x400")
# window size

        # Set the background color of the main window to red
        self.root.config(bg="yellow")

        # Add buttons to open new windows
        open_window_button1 = Button(
            self.root, text="Registration Form", bg="green", fg="white", font=(
                "Comic Sans MS", 11, "bold"), command=self.open_window_1)
        open_window_button1.pack(pady=70)

        open_window_button2 = Button(
            self.root, text="Performance Tab", bg="green", fg="white", font=(
                "Comic Sans MS", 11, "bold"), command=self.open_window_2)
        open_window_button2.pack(pady=1)

        close_window_button = Button(
            self.root, text="Close Window", bg="#FF6347", fg="white", font=("Comic Sans MS", 11, "bold"), command=self.close_window)
        close_window_button.pack(pady=50)

    def close_window(self):
        # Close the main window when the button is pressed
        self.root.iconify()

    def open_window_1(self):
        """Open a new window (Window 1)"""
        window1 = Toplevel(self.root)
        window1.title("Window 1")
        window1.geometry("1350x720+0+0")

        # Set the background color of Window 1
        window1.config(bg="lightblue")


# VARIABLEs FOR DATABASE:
        self.first_name_var = StringVar()
        self.middle_name_var = StringVar()
        self.last_name_var = StringVar()
        self.gender_var = StringVar()
        self.birth_date_var = StringVar()
        self.father_name_var = StringVar()
        self.mother_name_var = StringVar()
        self.phone_var = StringVar()
        self.whatsapp_var = StringVar()
        self.email_var = StringVar()
        self.adm_date_var = StringVar()
        self.address_var = StringVar()
        self.city_var = StringVar()
        self.state_var = StringVar()
        self.pin_var = StringVar()

        lbltitle = Label(window1, text="Registration Form", bg="yellow", fg="#06038d",
                         bd=5, relief=SUNKEN, font=("Comic Sans MS", 30, "bold"), padx=2, pady=5)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(window1, bd=5, relief=RIDGE, padx=10, bg="#d3d3d3")
        frame.place(x=0, y=70, width=1345, height=300)

# Created the Left DataFrame
        DataFrameLeft = LabelFrame(frame, text="Candidate Profile", bg="#d3d3d3",
                                   fg="#06038d", bd=5, relief=RIDGE, font=("Comic Sans MS", 20, "bold"))
        DataFrameLeft.place(x=1, y=5, width=1010, height=250)

        lblfirst_name = Label(DataFrameLeft, text="First Name:", bg="#d3d3d3",
                              fg="#940003", font=("Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblfirst_name.grid(row=0, column=0, sticky=W)
        txtfirst_name = Entry(DataFrameLeft, font=(
            "Comic Sans MS", 11, "italic"), width=24, textvariable=self.first_name_var)
        txtfirst_name.grid(row=0, column=1)

        lblmiddle_name = Label(DataFrameLeft, text="Middle Name:", bg="#d3d3d3",
                               fg="#ff0000", font=("Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblmiddle_name.grid(row=1, column=0, sticky=W)
        txtmiddle_name = Entry(DataFrameLeft, font=(
            "Comic Sans MS", 11, "italic"), width=24, textvariable=self.middle_name_var)
        txtmiddle_name.grid(row=1, column=1)

        lbllast_name = Label(DataFrameLeft, text="Last Name:", bg="#d3d3d3",
                             fg="#ff1493", font=("Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lbllast_name.grid(row=2, column=0, sticky=W)
        txtlast_name = Entry(DataFrameLeft, font=(
            "Comic Sans MS", 11, "italic"), width=24, textvariable=self.last_name_var)
        txtlast_name.grid(row=2, column=1)

        lblgender = Label(DataFrameLeft, text="Gender:", bg="#d3d3d3", fg="#ff4500", font=(
            "Comic Sans MS", 12, "underline"), padx=5, pady=6)
        lblgender.grid(row=3, column=0, sticky=W)
        comgender = ttk.Combobox(DataFrameLeft, font=(
            "Comic Sans MS", 11, "italic"), width=22, textvariable=self.gender_var)
        comgender["value"] = ("Male", "Female", "Others")
        comgender.current(0)
        comgender.grid(row=3, column=1)

        lblbirth_date = Label(DataFrameLeft, text="Birth Date:", bg="#d3d3d3",
                              fg="#008000", font=("Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblbirth_date.grid(row=4, column=0, sticky=W)
        txtbirth_date = Entry(DataFrameLeft, font=(
            "Comic Sans MS", 11, "italic"), width=24, textvariable=self.birth_date_var)
        txtbirth_date.grid(row=4, column=1)
        txtbirth_date.insert(0, "YYYY-MM-DD")

        lblfathers_name = Label(DataFrameLeft, text="Father's Name:", bg="#d3d3d3",
                                fg="#0000ff", font=("Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblfathers_name.grid(row=0, column=2, sticky=W)
        txtfathers_name = Entry(DataFrameLeft, font=(
            "Comic Sans MS", 11, "italic"), width=24, textvariable=self.father_name_var)
        txtfathers_name.grid(row=0, column=3)

        lblmothers_name = Label(DataFrameLeft, text="Mother's Name:", bg="#d3d3d3",
                                fg="#4b0082", font=("Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblmothers_name.grid(row=1, column=2, sticky=W)
        txtmothers_name = Entry(DataFrameLeft, font=(
            "Comic Sans MS", 11, "italic"), width=24, textvariable=self.mother_name_var)
        txtmothers_name.grid(row=1, column=3)

        lblphone = Label(DataFrameLeft, text="Phone:", bg="#d3d3d3", fg="#8a2be2", font=(
            "Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblphone.grid(row=2, column=2, sticky=W)
        txtphone = Entry(DataFrameLeft, font=(
            "Comic Sans MS", 11, "italic"), width=24, textvariable=self.phone_var)
        txtphone.grid(row=2, column=3)

        lblwhatsapp = Label(DataFrameLeft, text="WhatsApp:", bg="#d3d3d3", fg="#03ac13", font=(
            "Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblwhatsapp.grid(row=3, column=2, sticky=W)
        txtwhatsapp = Entry(DataFrameLeft, font=(
            "Comic Sans MS", 11, "italic"), width=24, textvariable=self.whatsapp_var)
        txtwhatsapp.grid(row=3, column=3)

        lblemail_id = Label(DataFrameLeft, text="0ccupation:", bg="#d3d3d3", fg="#b22222", font=(
            "Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblemail_id.grid(row=4, column=2, sticky=W)
        txtemail_id = Entry(DataFrameLeft, font=(
            "Comic Sans MS", 11, "italic"), width=24, textvariable=self.email_var)
        txtemail_id.grid(row=4, column=3)

        lbladmission_date = Label(DataFrameLeft, text="Adm_Date:", bg="#d3d3d3",
                                  fg="#9932cc", font=("Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lbladmission_date.grid(row=0, column=4, sticky=W)
        txtadmission_date = Entry(DataFrameLeft, font=(
            "Comic Sans MS", 11, "italic"), width=24, textvariable=self.adm_date_var)
        txtadmission_date.grid(row=0, column=5)
        txtadmission_date.insert(0, "YYYY-MM-DD")

        lbladdress = Label(DataFrameLeft, text="Address:", bg="#d3d3d3", fg="#0000ff", font=(
            "Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lbladdress.grid(row=1, column=4, sticky=W)
        txtaddress = Entry(DataFrameLeft, font=("Comic Sans MS", 11,
                                                "italic"), width=24, textvariable=self.address_var)
        txtaddress.grid(row=1, column=5)

        lblcity = Label(DataFrameLeft, text="City:", bg="#d3d3d3", fg="#ff1493", font=(
            "Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblcity.grid(row=2, column=4, sticky=W)
        txtcity = Entry(DataFrameLeft, font=("Comic Sans MS", 11,
                        "italic"), width=24, textvariable=self.city_var)
        txtcity.grid(row=2, column=5)

        lblstate = Label(DataFrameLeft, text="State:", bg="#d3d3d3", fg="#4b0082", font=(
            "Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblstate.grid(row=3, column=4, sticky=W)
        txtstate = Entry(DataFrameLeft, font=("Comic Sans MS", 11,
                                              "italic"), width=24, textvariable=self.state_var)
        txtstate.grid(row=3, column=5)

        lblpin = Label(DataFrameLeft, text="Pin:", bg="#d3d3d3", fg="#ff1493", font=(
            "Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblpin.grid(row=4, column=4, sticky=W)
        txtpin = Entry(DataFrameLeft, font=("Comic Sans MS", 11,
                                            "italic"), width=24, textvariable=self.pin_var)
        txtpin.grid(row=4, column=5)


# Created the Right DataFrame
        DataFrameRight = LabelFrame(frame, text="View Tab", bg="#d3d3d3",
                                    fg="#06038d", bd=5, relief=SUNKEN, font=("Comic Sans MS", 20, "bold"))
        DataFrameRight.place(x=1015, y=2, width=300, height=250)
# Created txtBox, an attribute of the class using self
        self.txtBox = Text(DataFrameRight, font=(
            "Comic Sans MS", 11, "normal"), width=25, height=10, padx=15, pady=0)
        self.txtBox.grid(row=0, column=0)

        listscrollbar = Scrollbar(
            DataFrameRight, orient=VERTICAL, command=self.txtBox.yview)
        listscrollbar.grid(row=0, column=1, sticky="ns")
        self.txtBox.config(yscrollcommand=listscrollbar.set)

# Function to check if the content needs a scrollbar

        def update_scrollbar(*args):
            if self.txtBox.yview()[1] < 1:
                # Show the scrollbar
                listscrollbar.grid(row=0, column=1, sticky="ns")
            else:
                listscrollbar.grid_forget()  # Hide the scrollbar if content fits

    # Reset scrollbar to 0 (start position) if the text box is empty
            if not self.txtBox.get(1.0, "end-1c"):  # Check if the text box is empty
                self.txtBox.yview_moveto(0)  # Reset the view to the top (0)
        # Bind the text widget to track changes and update scrollbar visibility
        # Trigger when a key is released
        self.txtBox.bind("<KeyRelease>", update_scrollbar)
        # Trigger when the widget is resized
        self.txtBox.bind("<Configure>", update_scrollbar)

        # Testing: You can add some text initially
        # Adds enough text to make the textbox scrollable
        self.txtBox.insert(END, "Student\'s Details\n")


# Buttons to update the textbox content
        buttonframe = Frame(window1, bd=5, relief=RIDGE,
                            padx=20, bg="#ffffff")
        buttonframe.place(x=0, y=370, width=1345, height=70)

        btninsert = Button(buttonframe, cursor="hand2", text="Insert", command=self.addData, font=(
            "Comic Sans MS", 11, "bold"), width=34, bg="#98fb98", fg="#0000ff", bd=5, pady=9)
        btninsert.grid(row=0, column=0)

        btnreset = Button(buttonframe, cursor="watch", text="Read", command=self.showData, font=(
            "Comic Sans MS", 11, "bold"), width=34, bg="#98fb98", fg="#0000ff", bd=5, pady=9)
        btnreset.grid(row=0, column=2)

        btndelete = Button(buttonframe, cursor="hand2", text="Refresh", command=self.reset, font=(
            "Comic Sans MS", 11, "bold"), width=34, bg="#aef359", fg="#0000ff", bd=5, pady=9)
        btndelete.grid(row=0, column=3)

        btnexit = Button(buttonframe, cursor="watch", text="Exit", command=self.iexit, font=(
            "Comic Sans MS", 11, "bold"), width=34, bg="#aef359", fg="#0000ff", bd=5, pady=9)
        btnexit.grid(row=0, column=4)


# INFORMATION Frame
        infoframe = Frame(window1, bd=5, relief=RIDGE,
                          padx=5, bg="#046a38")
        infoframe.place(x=1, y=445, width=1345, height=250)

        Tableframe = Frame(window1, bd=4, relief=RIDGE, bg="#00ff00")
        Tableframe.place(x=1, y=445, width=1335, height=245)

# # I will get the joining letter from Ericsson India Global Service within November. God will help me.

        xscroll = ttk.Scrollbar(Tableframe, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Tableframe, orient=VERTICAL)
# Created a Treeview widget to display the data from MySQL

        self.registrationTable = ttk.Treeview(
            Tableframe,
            columns=("First_Name", "Middle_Name", "Last_Name", "Gender", "Birth_Date", "Father_Name", "Mother_Name", "Phone",
                     "Whatsapp", "Email", "Adm_Date", "Address", "City", "State", "Pin"),
            xscrollcommand=xscroll.set,
            yscrollcommand=yscroll.set
        )


# ScrollBar added to the Treeview
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.registrationTable.xview)
        yscroll.config(command=self.registrationTable.yview)

        self.registrationTable.heading("First_Name", text="First Name")
        self.registrationTable.heading("Middle_Name", text="Middle Name")
        self.registrationTable.heading("Last_Name", text="Last Name")
        self.registrationTable.heading("Gender", text="Gender")
        self.registrationTable.heading("Birth_Date", text="Birth Date")
        self.registrationTable.heading("Father_Name", text="Father's Name")
        self.registrationTable.heading("Mother_Name", text="Mother's Name")
        self.registrationTable.heading("Phone", text="Phone")
        self.registrationTable.heading("Whatsapp", text="Whatsapp")
        self.registrationTable.heading("Email", text="0ccupation")
        self.registrationTable.heading("Adm_Date", text="Admission Date")
        self.registrationTable.heading("Address", text="Address")
        self.registrationTable.heading("City", text="City")
        self.registrationTable.heading("State", text="State")
        self.registrationTable.heading("Pin", text="Pin")
        self.registrationTable["show"] = "headings"
        self.registrationTable.pack(fill=BOTH, expand=1)


# THE WIDTH OF COLUMNS IN TABLE checked
# Setting column widths for the registration table to match field names
        self.registrationTable.column("First_Name", width=100)
        self.registrationTable.column("Middle_Name", width=100)
        self.registrationTable.column("Last_Name", width=100)
        self.registrationTable.column("Gender", width=100)
        self.registrationTable.column("Birth_Date", width=100)
        self.registrationTable.column("Father_Name", width=100)
        self.registrationTable.column("Mother_Name", width=100)
        self.registrationTable.column("Phone", width=100)
        self.registrationTable.column("Whatsapp", width=100)
        self.registrationTable.column("Email", width=100)
        self.registrationTable.column("Adm_Date", width=100)
        self.registrationTable.column("Address", width=100)
        self.registrationTable.column("City", width=100)
        self.registrationTable.column("State", width=100)
        self.registrationTable.column("Pin", width=100)

        self.connect_to_database()
# Fetched the data from MySQL database
        self.fetch_data_from_mysql()
        self.registrationTable.bind("<ButtonRelease-1>",
                                    self.get_cursor)
# Event Binding

    def connect_to_database(self):
        self.my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="library_database")
        self.my_cursor = self.my_db.cursor()
        print("Connected First Time")

    def addData(self):
        if self.my_db is not None:

            query = """
                INSERT INTO registration (first_name, middle_name, last_name, gender, birth_date, father_name, mother_name,
                                    phone, whatsapp, email, adm_date, address, city, state, pin)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""


# Created a tuple of data to insert
            data = (

                self.first_name_var.get().title(),
                self.middle_name_var.get().title(),
                self.last_name_var.get().title(),
                self.gender_var.get(),
                self.birth_date_var.get(),
                self.father_name_var.get().title(),
                self.mother_name_var.get().title(),
                self.phone_var.get(),
                self.whatsapp_var.get(),
                self.email_var.get(),
                self.adm_date_var.get(),
                self.address_var.get().title(),
                self.city_var.get().title(),
                self.state_var.get().title(),
                self.pin_var.get()
            )
# Executed the SQL command
            self.my_cursor.execute(query, data)
            self.my_db.commit()  # Commit the transaction
            self.fetch_data_from_mysql()

            messagebox.showinfo("Success", "Data inserted successfully!")
            print("Data inserted successfully.")

    def fetch_data_from_mysql(self):
        """Fetched data from MySQL database and display it in the Treeview"""
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="library_database")

        if conn.is_connected():
            print("Connected Second Time")

# Created a cursor object to interact with the database
            cursor = conn.cursor()

# Executed the SELECT query
            query = "SELECT * FROM registration"
            cursor.execute(query)

# Fetched all the rows
            rows = cursor.fetchall()

# Inserted rows into the Treeview widget
            if len(rows) != 0:

                self.registrationTable.delete(
                    *self.registrationTable.get_children())
                for row in rows:
                    self.registrationTable.insert("", END, values=row)

# Closed the cursor and connection
            conn.commit()
            cursor.close()
            conn.close()
# Inserted the data into the text box in the desired format

    def showData(self):

        self.txtBox.insert(END, "First_Name\t" +
                           self.first_name_var.get() + "\n")

        self.txtBox.insert(END, "Middle_Name\t" +
                           self.middle_name_var.get() + "\n")
        self.txtBox.insert(END, "Last_Name\t" +
                           self.last_name_var.get() + "\n")
        self.txtBox.insert(END, "Gender\t" +
                           self.gender_var.get() + "\n")
        self.txtBox.insert(END, "Birth_Date\t" +
                           self.birth_date_var.get() + "\n")
        self.txtBox.insert(END, "Father_Name\t" +
                           self.father_name_var.get() + "\n")
        self.txtBox.insert(END, "Mother_Name\t" +
                           self.mother_name_var.get() + "\n")
        self.txtBox.insert(END, "Phone\t" + self.phone_var.get() + "\n")
        self.txtBox.insert(END, "Whatsapp\t" + self.whatsapp_var.get() + "\n")
        self.txtBox.insert(END, "Email\t" + self.email_var.get() + "\n")
        self.txtBox.insert(END, "Adm_Date\t" +
                           self.adm_date_var.get() + "\n")
        self.txtBox.insert(END, "Address\t" +
                           self.address_var.get() + "\n")
        self.txtBox.insert(
            END, "City:\t" + self.city_var.get() + "\n")
        self.txtBox.insert(END, "State\t" +
                           self.state_var.get() + "\n")
        self.txtBox.insert(END, "Pin\t" + self.pin_var.get() + "\n")

    def get_cursor(self, event=""):
        # To get the currently focused row
        cursor_row = self.registrationTable.focus()
        content = self.registrationTable.item(cursor_row)
        rows = content.get("values")

# Checked if the row is valid
        if cursor_row == '':

            print("Selected row is empty")
            return
# Exit the function if the row has no values

# Checked if 'rows' is None or an empty list
        if rows is None or len(rows) == 0:
            print("There is no value")
            return


# Assigned values from the database or other data source to StringVars
# Set the Tkinter variables to corresponding values from the database row (rows)
        self.first_name_var.set(rows[0])    # First Name
        self.middle_name_var.set(rows[1])   # Middle Name
        self.last_name_var.set(rows[2])     # Last Name
        self.gender_var.set(rows[3])        # Gender
        self.birth_date_var.set(rows[4])    # Birth Date
        self.father_name_var.set(rows[5])  # Father's Name
        self.mother_name_var.set(rows[6])  # Mother's Name
        self.phone_var.set(rows[7])         # Phone
        self.whatsapp_var.set(rows[8])      # Whatsapp
        self.email_var.set(rows[9])         # Email
        self.adm_date_var.set(rows[10])  # Admission Date
        self.address_var.set(rows[11])      # Address
        self.city_var.set(rows[12])         # City
        self.state_var.set(rows[13])        # State
        self.pin_var.set(rows[14])          # Pin

    def reset(self):

        # Reset the Tkinter variables to empty strings
        self.first_name_var.set("")  # Reset First Name
        self.middle_name_var.set("")  # Reset Middle Name
        self.last_name_var.set("")   # Reset Last Name
        self.gender_var.set("")      # Reset Gender
        self.birth_date_var.set("")  # Reset Birth Date
        self.father_name_var.set("")  # Reset Father's Name
        self.mother_name_var.set("")  # Reset Mother's Name
        self.phone_var.set("")       # Reset Phone
        self.whatsapp_var.set("")    # Reset Whatsapp
        self.email_var.set("")       # Reset Email
        self.adm_date_var.set("")  # Reset Admission Date
        self.address_var.set("")     # Reset Address
        self.city_var.set("")        # Reset City
        self.state_var.set("")       # Reset State
        self.pin_var.set("")         # Reset Pin

    def iexit(self):
        iexit = tkinter.messagebox.askyesno(
            "Registration Form", "want to ⚠LEAVE⚠ the window?")
        if iexit > 0:
            self.root.destroy()
            return
# 22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222

    def open_window_2(self):
        """Open a new window (Window 2)"""
        window2 = Toplevel(self.root)
        window2.title("Window 2")
        window2.geometry("1350x720+0+0")

# VARIABLEs FOR DATABASE:
        self.class_var = StringVar()
        self.year_var = StringVar()
        self.month_var = StringVar()
        self.payment_mode_var = StringVar()
        self.fee_var = StringVar()
        self.attendance_var = StringVar()
        self.subject1_var = StringVar()
        self.marks1_var = StringVar()
        self.subject2_var = StringVar()
        self.marks2_var = StringVar()
        self.subject3_var = StringVar()
        self.marks3_var = StringVar()
        self.subject4_var = StringVar()
        self.marks4_var = StringVar()
        self.remark_var = StringVar()

        lbltitle1 = Label(window2, text="Monthly Scores", bg="yellow", fg="#06038d",
                          bd=5, relief=SUNKEN, font=("Comic Sans MS", 30, "bold"), padx=2, pady=5)
        lbltitle1.pack(side=TOP, fill=X)

        frame1 = Frame(window2, bd=5, relief=RIDGE, padx=10, bg="#d3d3d3")
        frame1.place(x=0, y=70, width=1345, height=300)

# Created the Left DataFrame
        DataFrameLeft1 = LabelFrame(frame1, text="Score Sheet", bg="#d3d3d3",
                                    fg="#06038d", bd=5, relief=RIDGE, font=("Comic Sans MS", 18, "bold"))
        DataFrameLeft1.place(x=1, y=5, width=1010, height=250)

        lblclass = Label(DataFrameLeft1, text="Class:", bg="#d3d3d3", fg="#ff4500", font=(
            "Comic Sans MS", 12, "underline"), padx=5, pady=6)
        lblclass.grid(row=0, column=0, sticky=W)
        comclass = ttk.Combobox(DataFrameLeft1, font=(
            "Comic Sans MS", 11, "italic"), width=22, textvariable=self.class_var)
        comclass["value"] = ("1", "2", "3", "4")
        comclass.current(0)
        comclass.grid(row=0, column=1)

        lblyear = Label(DataFrameLeft1, text="Date:", bg="#d3d3d3",
                        fg="#ff0000", font=("Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblyear.grid(row=1, column=0, sticky=W)
        txtyear = Entry(DataFrameLeft1, font=(
            "Comic Sans MS", 11, "italic"), width=24, textvariable=self.year_var)
        txtyear.grid(row=1, column=1)
        txtyear.insert(0, "YYYY-MM-DD")

        lblmonth = Label(DataFrameLeft1, text="Name:", bg="#d3d3d3",
                         fg="#0000ff", font=("Comic Sans MS", 11, "underline"), padx=2, pady=6)
        lblmonth.grid(row=2, column=0, sticky=W)
        txtmonth = Entry(DataFrameLeft1, font=(
            "Comic Sans MS", 12, "italic"), width=22, textvariable=self.month_var)
        txtmonth.grid(row=2, column=1)

        lblpayment_mode = Label(DataFrameLeft1, text="Payment Mode:", bg="#d3d3d3", fg="#ff4500", font=(
            "Comic Sans MS", 12, "underline"), padx=5, pady=6)
        lblpayment_mode.grid(row=3, column=0, sticky=W)
        compayment_mode = ttk.Combobox(DataFrameLeft1, font=(
            "Comic Sans MS", 11, "italic"), width=22, textvariable=self.payment_mode_var)
        compayment_mode["value"] = ("Cash", "Online", "Others")
        compayment_mode.current(0)
        compayment_mode.grid(row=3, column=1)

        lblfee = Label(DataFrameLeft1, text="Fee:", bg="#d3d3d3",
                       fg="#008000", font=("Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblfee.grid(row=4, column=0, sticky=W)
        txtfee = Entry(DataFrameLeft1, font=(
            "Comic Sans MS", 11, "italic"), width=24, textvariable=self.fee_var)
        txtfee.grid(row=4, column=1)
        txtfee.insert(0, "700")

        lblattendance = Label(DataFrameLeft1, text="Attendance:", bg="#d3d3d3",
                              fg="#0000ff", font=("Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblattendance.grid(row=0, column=2, sticky=W)
        txtattendance = Entry(DataFrameLeft1, font=(
            "Comic Sans MS", 11, "italic"), width=24, textvariable=self.attendance_var)
        txtattendance.grid(row=0, column=3)
        txtattendance.insert(0, "4")

        lblsubject1 = Label(DataFrameLeft1, text="Subject1:", bg="#d3d3d3",
                            fg="#4b0082", font=("Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblsubject1.grid(row=1, column=2, sticky=W)
        txtsubject1 = Entry(DataFrameLeft1, font=(
            "Comic Sans MS", 11, "italic"), width=24, textvariable=self.subject1_var)
        txtsubject1.grid(row=1, column=3)
        txtsubject1.insert(0, "subject name")

        lblmarks1 = Label(DataFrameLeft1, text="Marks1:", bg="#d3d3d3", fg="#8a2be2", font=(
            "Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblmarks1.grid(row=2, column=2, sticky=W)
        txtmarks1 = Entry(DataFrameLeft1, font=(
            "Comic Sans MS", 11, "italic"), width=24, textvariable=self.marks1_var)
        txtmarks1.grid(row=2, column=3)
        txtmarks1.insert(0, "1")

        lblsubject2 = Label(DataFrameLeft1, text="Subject2:", bg="#d3d3d3", fg="#03ac13", font=(
            "Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblsubject2.grid(row=3, column=2, sticky=W)
        txtsubject2 = Entry(DataFrameLeft1, font=(
            "Comic Sans MS", 11, "italic"), width=24, textvariable=self.subject2_var)
        txtsubject2.grid(row=3, column=3)

        lblmarks2 = Label(DataFrameLeft1, text="Marks2:", bg="#d3d3d3", fg="#b22222", font=(
            "Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblmarks2.grid(row=4, column=2, sticky=W)
        txtmarks2 = Entry(DataFrameLeft1, font=(
            "Comic Sans MS", 11, "italic"), width=24, textvariable=self.marks2_var)
        txtmarks2.grid(row=4, column=3)
        txtmarks2.insert(0, "1")
        lblsubject3 = Label(DataFrameLeft1, text="Subject3:", bg="#d3d3d3",
                            fg="#9932cc", font=("Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblsubject3.grid(row=0, column=4, sticky=W)
        txtsubject3 = Entry(DataFrameLeft1, font=(
            "Comic Sans MS", 11, "italic"), width=24, textvariable=self.subject3_var)
        txtsubject3.grid(row=0, column=5)

        lblmarks3 = Label(DataFrameLeft1, text="Marks3:", bg="#d3d3d3", fg="#0000ff", font=(
            "Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblmarks3.grid(row=1, column=4, sticky=W)
        txtmarks3 = Entry(DataFrameLeft1, font=("Comic Sans MS", 11,
                                                "italic"), width=24, textvariable=self.marks3_var)
        txtmarks3.grid(row=1, column=5)
        txtmarks3.insert(0, "1")
        lblsubject4 = Label(DataFrameLeft1, text="Subject4:", bg="#d3d3d3", fg="#ff1493", font=(
            "Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblsubject4.grid(row=2, column=4, sticky=W)
        txtsubject4 = Entry(DataFrameLeft1, font=("Comic Sans MS", 11,
                                                  "italic"), width=24, textvariable=self.subject4_var)
        txtsubject4.grid(row=2, column=5)

        lblmarks4 = Label(DataFrameLeft1, text="Marks4:", bg="#d3d3d3", fg="#4b0082", font=(
            "Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblmarks4.grid(row=3, column=4, sticky=W)
        txtmarks4 = Entry(DataFrameLeft1, font=("Comic Sans MS", 11,
                                                "italic"), width=24, textvariable=self.marks4_var)
        txtmarks4.grid(row=3, column=5)
        txtmarks4.insert(0, "1")
        lblremark = Label(DataFrameLeft1, text="Remark:", bg="#d3d3d3", fg="#ff1493", font=(
            "Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblremark.grid(row=4, column=4, sticky=W)
        txtremark = Entry(DataFrameLeft1, font=("Comic Sans MS", 11,
                                                "italic"), width=24, textvariable=self.remark_var)
        txtremark.grid(row=4, column=5)


# Created the Right DataFrame
        DataFrameRight1 = LabelFrame(frame1, text="View Tab", bg="#d3d3d3",
                                     fg="#06038d", bd=5, relief=SUNKEN, font=("Comic Sans MS", 20, "bold"))
        DataFrameRight1.place(x=1015, y=2, width=300, height=250)
# Created txtBox, an attribute of the class using self
        self.txtBox1 = Text(DataFrameRight1, font=(
            "Comic Sans MS", 11, "normal"), width=25, height=10, padx=15, pady=0)
        self.txtBox1.grid(row=0, column=0)

        listscrollbar1 = Scrollbar(
            DataFrameRight1, orient=VERTICAL, command=self.txtBox1.yview)
        listscrollbar1.grid(row=0, column=1, sticky="ns")
        self.txtBox1.config(yscrollcommand=listscrollbar1.set)

# Function to check if the content needs a scrollbar

        def update_scrollbar1(*args):
            if self.txtBox1.yview()[1] < 1:
                # Show the scrollbar
                listscrollbar1.grid(row=0, column=1, sticky="ns")
            else:
                listscrollbar1.grid_forget()  # Hide the scrollbar if content fits

    # Reset scrollbar to 0 (start position) if the text box is empty
            # Check if the text box is empty
            if not self.txtBox1.get(1.0, "end-1c"):
                self.txtBox1.yview_moveto(0)  # Reset the view to the top (0)
        # Bind the text widget to track changes and update scrollbar visibility
        # Trigger when a key is released
        self.txtBox1.bind("<KeyRelease>", update_scrollbar1())
        # Trigger when the widget is resized
        self.txtBox1.bind("<Configure>", update_scrollbar1)

        # Testing: You can add some text initially
        # Adds enough text to make the textbox scrollable
        self.txtBox1.insert(END, "Student\'s Details\n")


# Buttons to update the textbox content
        buttonframe1 = Frame(window2, bd=5, relief=RIDGE,
                             padx=20, bg="#ffffff")
        buttonframe1.place(x=0, y=370, width=1345, height=70)

        btninsert1 = Button(buttonframe1, cursor="hand2", text="Insert", command=self.addData1, font=(
            "Comic Sans MS", 11, "bold"), width=34, bg="#98fb98", fg="#0000ff", bd=5, pady=9)
        btninsert1.grid(row=0, column=0)

        btnreset1 = Button(buttonframe1, cursor="watch", text="Read", command=self.showData1, font=(
            "Comic Sans MS", 11, "bold"), width=34, bg="#98fb98", fg="#0000ff", bd=5, pady=9)
        btnreset1.grid(row=0, column=2)

        btndelete1 = Button(buttonframe1, cursor="hand2", text="Refresh", command=self.reset1, font=(
            "Comic Sans MS", 11, "bold"), width=34, bg="#aef359", fg="#0000ff", bd=5, pady=9)
        btndelete1.grid(row=0, column=3)

        btnexit1 = Button(buttonframe1, cursor="watch", text="Exit", command=self.iexit1, font=(
            "Comic Sans MS", 11, "bold"), width=34, bg="#aef359", fg="#0000ff", bd=5, pady=9)
        btnexit1.grid(row=0, column=4)


# INFORMATION Frame
        infoframe1 = Frame(window2, bd=5, relief=RIDGE,
                           padx=5, bg="#046a38")
        infoframe1.place(x=1, y=445, width=1345, height=250)

        Tableframe1 = Frame(window2, bd=4, relief=RIDGE, bg="#00ff00")
        Tableframe1.place(x=1, y=445, width=1335, height=245)

        xscroll1 = ttk.Scrollbar(Tableframe1, orient=HORIZONTAL)
        yscroll1 = ttk.Scrollbar(Tableframe1, orient=VERTICAL)
# Created a Treeview widget to display the data from MySQL

        self.scoreTable = ttk.Treeview(
            Tableframe1,
            columns=("class", "year", "month", "payment_mode", "fee", "attendance", "subject1", "marks1",
                     "subject2", "marks2", "subject3", "marks3", "subject4", "marks4", "remark"),
            xscrollcommand=xscroll1.set,
            yscrollcommand=yscroll1.set
        )


# ScrollBar added to the Treeview
        xscroll1.pack(side=BOTTOM, fill=X)
        yscroll1.pack(side=RIGHT, fill=Y)

        xscroll1.config(command=self.scoreTable.xview)
        yscroll1.config(command=self.scoreTable.yview)

        self.scoreTable.heading("class", text="Class")
        self.scoreTable.heading("year", text="Date")
        self.scoreTable.heading("month", text="Name")
        self.scoreTable.heading("payment_mode", text="Payment Mode")
        self.scoreTable.heading("fee", text="Fee")
        self.scoreTable.heading("attendance", text="Attendance")
        self.scoreTable.heading("subject1", text="Subject1")
        self.scoreTable.heading("marks1", text="Marks1")
        self.scoreTable.heading("subject2", text="Subject2")
        self.scoreTable.heading("marks2", text="Marks2")
        self.scoreTable.heading("subject3", text="Subject3")
        self.scoreTable.heading("marks3", text="Marks3")
        self.scoreTable.heading("subject4", text="Subject4")
        self.scoreTable.heading("marks4", text="Marks4")
        self.scoreTable.heading("remark", text="Remark")
        self.scoreTable["show"] = "headings"
        self.scoreTable.pack(fill=BOTH, expand=1)


# THE WIDTH OF COLUMNS IN TABLE checked
# Setting column widths for the registration table to match field names
        self.scoreTable.column("class", width=100)
        self.scoreTable.column("year", width=100)
        self.scoreTable.column("month", width=100)
        self.scoreTable.column("payment_mode", width=100)
        self.scoreTable.column("fee", width=100)
        self.scoreTable.column("attendance", width=100)
        self.scoreTable.column("subject1", width=100)
        self.scoreTable.column("marks1", width=100)
        self.scoreTable.column("subject2", width=100)
        self.scoreTable.column("marks2", width=100)
        self.scoreTable.column("subject3", width=100)
        self.scoreTable.column("marks3", width=100)
        self.scoreTable.column("subject4", width=100)
        self.scoreTable.column("marks4", width=100)
        self.scoreTable.column("remark", width=100)

        self.connect_to_database1()
# Fetched the data from MySQL database
        self.fetch_data_from_mysql1()
        self.scoreTable.bind("<ButtonRelease-1>",
                             self.get_cursor1())
# Event Binding

    def connect_to_database1(self):
        self.my_db1 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="sbi_bank")
        self.my_cursor1 = self.my_db1.cursor()
        print("Marks App: Database Connected")

    def addData1(self):
        if self.my_db1 is not None:

            query1 = """
                INSERT INTO score (class, year, month, payment_mode, fee, attendance, subject1, 
                                    marks1, subject2, marks2, subject3, marks3, subject4, marks4, remark)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""


# Created a tuple of data to insert
            data1 = (

                self.class_var.get(),
                self.year_var.get(),
                self.month_var.get().title(),
                self.payment_mode_var.get(),
                self.fee_var.get(),
                self.attendance_var.get(),
                self.subject1_var.get().title(),
                self.marks1_var.get(),
                self.subject2_var.get().title(),
                self.marks2_var.get(),
                self.subject3_var.get().title(),
                self.marks3_var.get(),
                self.subject4_var.get().title(),
                self.marks4_var.get(),
                self.remark_var.get()
            )
# Executed the SQL command
            self.my_cursor1.execute(query1, data1)
            self.my_db1.commit()  # Commit the transaction
            self.fetch_data_from_mysql1()

            messagebox.showinfo("Success", "Data inserted successfully!")
            print("Marks App: Second Time")

    def fetch_data_from_mysql1(self):
        """Fetched data from MySQL database and display it in the Treeview"""
        conn1 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="sbi_bank")

        if conn1.is_connected():
            print("Marks For Second")

# Created a cursor object to interact with the database
            cursor1 = conn1.cursor()

# Executed the SELECT query
            query1 = "SELECT * FROM score"
            cursor1.execute(query1)

# Fetched all the rows
            rows1 = cursor1.fetchall()

# Inserted rows into the Treeview widget
            if len(rows1) != 0:

                self.scoreTable.delete(
                    *self.scoreTable.get_children())
                for row1 in rows1:
                    self.scoreTable.insert("", END, values=row1)

# Closed the cursor and connection
            conn1.commit()
            cursor1.close()
            conn1.close()
# Inserted the data into the text box in the desired format

    def showData1(self):

        self.txtBox1.insert(END, "class\t" +
                            self.class_var.get() + "\n")

        self.txtBox1.insert(END, "year\t" +
                            self.year_var.get() + "\n")
        self.txtBox1.insert(END, "month\t" +
                            self.month_var.get() + "\n")
        self.txtBox1.insert(END, "payment_mode\t" +
                            self.payment_mode_var.get() + "\n")
        self.txtBox1.insert(END, "fee\t" +
                            self.fee_var.get() + "\n")
        self.txtBox1.insert(END, "attendance\t" +
                            self.attendance_var.get() + "\n")
        self.txtBox1.insert(END, "subject1\t" +
                            self.subject1_var.get() + "\n")
        self.txtBox1.insert(END, "marks1\t" + self.marks1_var.get() + "\n")
        self.txtBox1.insert(END, "subject2\t" + self.subject2_var.get() + "\n")
        self.txtBox1.insert(END, "marks2\t" + self.marks2_var.get() + "\n")
        self.txtBox1.insert(END, "subject3\t" +
                            self.subject3_var.get() + "\n")
        self.txtBox1.insert(END, "marks3\t" +
                            self.marks3_var.get() + "\n")
        self.txtBox1.insert(
            END, "subject4:\t" + self.subject4_var.get() + "\n")
        self.txtBox1.insert(END, "marks4\t" +
                            self.marks4_var.get() + "\n")
        self.txtBox1.insert(END, "remark\t" + self.remark_var.get() + "\n")

    def get_cursor1(self, event1=""):
        # To get the currently focused row
        cursor_row1 = self.scoreTable.focus()
        content1 = self.scoreTable.item(cursor_row1)
        rows1 = content1.get("values")

# Checked if the row is valid
        if cursor_row1 == '':

            print("Selected row is empty")
            return
# Exit the function if the row has no values

# Checked if 'rows' is None or an empty list
        if rows1 is None or len(rows1) == 0:
            print("There is no value")
            return


# Assigned values from the database or other data source to StringVars
# Set the Tkinter variables to corresponding values from the database row (rows)
        self.class_var.set(rows1[0])
        self.year_var.set(rows1[1])
        self.month_var.set(rows1[2])
        self.payment_mode_var.set(rows1[3])
        self.fee_var.set(rows1[4])
        self.attendance_var.set(rows1[5])
        self.subject1_var.set(rows1[6])
        self.marks1_var.set(rows1[7])
        self.subject2_var.set(rows1[8])
        self.marks2_var.set(rows1[9])
        self.subject3_var.set(rows1[10])
        self.marks3_var.set(rows1[11])
        self.subject4_var.set(rows1[12])
        self.marks4_var.set(rows1[13])
        self.remark_var.set(rows1[14])

    def reset1(self):

        # Reset the Tkinter variables to empty strings
        self.class_var.set("")  # Reset First Name
        self.year_var.set("")  # Reset Middle Name
        self.month_var.set("")   # Reset Last Name
        self.payment_mode_var.set("")      # Reset payment_mode
        self.fee_var.set("")  # Reset Birth Date
        self.attendance_var.set("")  # Reset Father's Name
        self.subject1_var.set("")  # Reset Mother's Name
        self.marks1_var.set("")       # Reset marks1
        self.subject2_var.set("")    # Reset subject2
        self.marks2_var.set("")       # Reset Email
        self.subject3_var.set("")  # Reset Admission Date
        self.marks3_var.set("")     # Reset marks2
        self.subject4_var.set("")        # Reset subject4
        self.marks4_var.set("")       # Reset marks4
        self.remark_var.set("")         # Reset remark

    def iexit1(self):
        iexit1 = tkinter.messagebox.askyesno(
            "Score Sheet", "want to ⚠LEAVE⚠ the window?")
        if iexit1 > 0:
            self.root.destroy()
            return


if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()

    # Create the app instance
    app = MultiWindowApp(root)

    # Start the Tkinter event loop
    root.mainloop()
