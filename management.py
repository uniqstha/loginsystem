from tkinter import *
from PIL import Image,ImageTk
import os
import sqlite3
from tkinter import messagebox

from tkinter import ttk




root=Tk()
root.geometry("1366x768+60+10")
root.title("Contact")
root.resizable(0, 0)
# root.iconbitmap('./images/3.ico')



# # # creating database
# conn = sqlite3.connect("info.db")
# c = conn.cursor()
# '''
# c.execute("""CREATE TABLE information(
#         First_Name text,
#         Age integer,
#         Address text,
#         Gender integer,
#         Email text,
#         Password text
#  )""")
# '''

# function
# ------------------------------------------
def save():
    global main

    conn = sqlite3.connect('info.db')
    c = conn.cursor()
    record_id=employeeID.get()
    c.execute("""UPDATE information SET
         'Full_name': fullname,
          'Age': age,
            'Address': address,
            'Gender': gender,
            'Email': email,
            'Password': password
         WHERE oid =:oid""",
         {
         'full_name': fullname.get(),
            'age': age.get(),
            'address': address.get(),
            'gender': var.get(),
            'email': email.get(),
            'password': password.get()
         })
    conn.commit()
    conn.close()
    employeeID.delete(0,END)
    main.destroy()
    os.system("admin.py")



def clear():
    first_name.delete(0,END)
    last_name.delete(0,END)
    gender.delete(0,END)
    age.delete(0,END)
    address.delete(0,END)
    contact.delete(0, END)

def update():
    root.withdraw()
    if (employeeID.get()==""):
        messagebox.showinfo("Error","Please select employee")
    else:
        global my_img
        global root1
        root1 = Toplevel()
        root1.geometry("1366x768+60+10")
        root1.title("Login")
        root1.resizable(0, 0)

        conn = sqlite3.connect('info.db')
        c = conn.cursor()
        record_id = employeeID.get()
        c.execute("SELECT*from information WHERE oid = " + record_id)
        records = c.fetchall()
        global fullname
        global address
        global age
        global gender
        global email
        global Password

        my_img = ImageTk.PhotoImage(Image.open('signup.png'))
        my_label=Label(root1,image=my_img).pack()
        fullname_lbl = Label(root1, text="Full Name", font=('Consolas', 15), bg="white")
        fullname_lbl.place(x=180, y=200)
        age_lbl = Label(root1, text="Age", font=('Consolas', 15), bg="white")
        age_lbl.place(x=720, y=200)
        address_lbl = Label(root1, text="Address", font=('Consolas', 15), bg="white")
        address_lbl.place(x=180, y=290)
        gender_lbl = Label(root1, text="Gender", font=('Consolas', 15), bg="white")
        gender_lbl.place(x=720, y=290)
        email_lbl = Label(root1, text="Email", font=('Consolas', 15), bg="white")
        email_lbl.place(x=180, y=380)
        password_lbl = Label(root1, text="Password", font=('Consolas', 15), bg="white")
        password_lbl.place(x=720, y=380)

        fullname = Entry(root1, width=40, border=0, font=('Consolas', 15))
        fullname.place(x=180, y=230)
        age = Entry(root1, width=40, border=0, font=('Consolas', 15))
        age.place(x=720, y=230)
        gender = Entry(root1, width=40, border=0, font=('Consolas', 15))
        gender.place(x=720, y=320)
        address = Entry(root1, width=40, border=0, font=('Consolas', 15))
        address.place(x=180, y=320)

        email = Entry(root1, width=40, border=0, font=('Consolas', 15))
        email.place(x=180, y=410)
        password = Entry(root1, width=40, border=0, font=('Consolas', 15))
        password.place(x=720, y=410)



        check = IntVar()
        checkbtn = Checkbutton(root1, text="Terms and Conditions", font=('Consolas', 20), bg="white",
                               activebackground="white", variable=check, onvalue=1, offvalue=0)
        checkbtn.deselect()
        checkbtn.place(x=525, y=540)

        for record in records:
            fullname.insert(0, record[0])
            age.insert(0, record[1])
            address.insert(0, record[2])
            gender.insert(0, record[3])
            email.insert(0, record[4])
            password.insert(0, record[5])
        submit_btn = Button(root1, text="SUBMIT", font=('Consolas', 15), cursor='hand2',
                            bg="#834dd6", border=0, activebackground="#834dd6", padx=22, pady=10,
                            command=confirm)
        submit_btn.place(x=544, y=630)
        exit_btn = Button(root1, text="EXIT", font=('Consolas', 15), cursor='hand2',
                          bg="#834dd6", border=0, activebackground="#834dd6", padx=25, pady=10, )
        exit_btn.place(x=715, y=630)

def delete():
    if (employeeID.get()==""):
        messagebox.showinfo("Error","Please select employee")
    else:
        root.withdraw()
        conn = sqlite3.connect('info.db')
        c = conn.cursor()
        c.execute('DELETE from information WHERE oid= ' + employeeID.get())
        print("Deleted successfully")

        conn.commit()
        conn.close()
        employeeID.delete(0, END)

        os.system("management.py")

def confirm():
    global root1

    conn = sqlite3.connect('info.db')
    c = conn.cursor()
    c.execute('DELETE from information WHERE oid= ' + employeeID.get())
    print("Deleted successfully")

    conn.commit()
    conn.close()
    employeeID.delete(0, END)
    root1.destroy()
    os.system("management.py")




def search():
    record_id = employeeID.get()
    for record in my_tree.get_children():
        my_tree.delete(record)

    conn = sqlite3.connect("info.db")
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM information WHERE FullName = ?", (record_id,))
    records = c.fetchall()

    for record in records:
        my_tree.insert('', 'end', values=(record))

    conn.commit()
    conn.close()








def refresh():
    root.destroy()
    os.system('management.py')





def Exit():
    sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=root)
    if sure == True:
        root.destroy()




# desgin
# -------------------------------------

# image
myimage=ImageTk.PhotoImage(Image.open('management.png'))
Label(image=myimage).pack()




# entry
employeeID=Entry(root,width=55,border=0,font=('Consolas',18))
employeeID.place(x=180,y=595)
# entryID = employeeID.get()



# buttons

searchBTN=Button(root,text="Search",font=('Consolas',15),cursor='hand2',padx=35,pady=7,
                  bg="#cc469d",border=0,activebackground="#cc469d",command = search)
searchBTN.place(x=1025,y=585)

updateBTN=Button(root,text="UPDATE ",font=('Consolas',22),cursor='hand2',padx=20,pady=1,
                  bg="#6b30a6",border=0,activebackground="#6b30a6",command=update)
updateBTN.place(x=220,y=650)

deleteBTN=Button(root,text="DELETE ",font=('Consolas',22),cursor='hand2',
                  bg="#9d3ca2",border=0,activebackground="#9d3ca2",padx=20,pady=1, command = delete)
deleteBTN.place(x=600,y=650)
refreshBTN=Button(root,text="REFRESH ",font=('Consolas',22),cursor='hand2',
                  bg="#cc469d",border=0,activebackground="#cc469d",padx=20,pady=1, command = refresh)
refreshBTN.place(x=980,y=650)


logoutBTN=Button(root,text="EXIT",font=('Consolas',18),cursor='hand2',padx=20,pady=1,
                  bg="#cc469d",border=0,activebackground="#cc469d", command = exit)
logoutBTN.place(x=1122,y=38)






# tree
conn=sqlite3.connect('info.db')
c=conn.cursor()
c.execute('SELECT * ,oid from information')
records = c.fetchall()
my_tree = ttk.Treeview(root)
my_tree['columns'] = ("Sno.","First Name", "Last Name", "Gender","Age", "Address","Contact")

my_tree.column("#0", width =0, stretch=NO)
my_tree.column("Sno.", anchor=CENTER,width=30)
my_tree.column("First Name", anchor=CENTER,width=150)
my_tree.column("Last Name", anchor=CENTER,width=120)
my_tree.column("Gender", anchor=CENTER,width=40)
my_tree.column("Age", anchor=CENTER,width=90)
my_tree.column("Address", anchor=CENTER,width=100)
my_tree.column("Contact", anchor=CENTER,width=100)

my_tree.heading("#0", text = "", anchor = CENTER)
my_tree.heading("Sno.", text = "Sno", anchor = CENTER)
my_tree.heading("First Name", text = "First Name", anchor = CENTER)
my_tree.heading("Last Name", text = "Last Name", anchor = CENTER)
my_tree.heading("Gender", text = "Gender", anchor = CENTER)
my_tree.heading("Age", text = "Age", anchor = CENTER)
my_tree.heading("Address", text = "Address", anchor = CENTER)
my_tree.heading("Contact",text = "Contact", anchor = CENTER)

my_tree.place(x=110,y=90, width=1150, height=420)




count=0
for record in records:
    my_tree.insert(parent='',index='end',iid=count,text="Parent",values=(record[6],record[0],record[1],record[2],record[3],record[4],record[5]))
    count+=1
conn.commit()
conn.close()
root.mainloop()