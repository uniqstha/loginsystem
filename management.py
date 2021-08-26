from tkinter import *
from PIL import Image,ImageTk
import os
import sqlite3
from tkinter import messagebox

from tkinter import ttk




root=Tk()
root.geometry("1150x768+185+10")
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
        global main
        main = Toplevel()
        main.geometry("1366x768+60+10")
        main.title("Login")
        main.resizable(0, 0)

        conn = sqlite3.connect('ContactInfo.db')
        c = conn.cursor()
        record_id = employeeID.get()
        c.execute("SELECT*from addresses WHERE oid = " + record_id)
        records = c.fetchall()
        global first_name
        global last_name
        global gender
        global age
        global address
        global contact

        # my_img = ImageTk.PhotoImage(Image.open('images/update.png'))
        # my_label=Label(main,image=my_img).pack()
        first_name_lbl = Label(main, text="First Name", font=('Consolas', 15), bg="white")
        first_name_lbl.place(x=180, y=200)
        last_name_lbl = Label(main, text="Last_name", font=('Consolas', 15), bg="white")
        last_name_lbl.place(x=720, y=200)
        gender_lbl = Label(main, text="Gender", font=('Consolas', 15), bg="white")
        gender_lbl.place(x=180, y=290)
        age_lbl = Label(main, text="Age", font=('Consolas', 15), bg="white")
        age_lbl.place(x=720, y=290)
        address_lbl = Label(main, text="Address", font=('Consolas', 15), bg="white")
        address_lbl.place(x=180, y=380)
        contact_lbl = Label(main, text="Contact", font=('Consolas', 15), bg="white")
        contact_lbl.place(x=720, y=380)

        first_name = Entry(main, width=40, border=0, font=('Consolas', 15))
        first_name.place(x=180, y=230)
        last_name = Entry(main, width=40, border=0, font=('Consolas', 15))
        last_name.place(x=720, y=230)
        gender = Entry(main, width=40, border=0, font=('Consolas', 15))
        gender.place(x=180, y=320)
        age = Entry(main, width=40, border=0, font=('Consolas', 15))
        age.place(x=720, y=320)
        address = Entry(main, width=40, border=0, font=('Consolas', 15))
        address.place(x=180, y=410)
        contact = Entry(main, width=40, border=0, font=('Consolas', 15))
        contact.place(x=720, y=410)
        for record in records:
            first_name.insert(0, record[0])
            last_name.insert(0, record[1])
            gender.insert(0, record[2])
            age.insert(0, record[3])
            address.insert(0, record[4])
            contact.insert(0, record[5])
        update_btn = Button(main, text="UPDATE", font=('Consolas', 15), cursor='hand2',
                         bg="#00bff3", border=0, activebackground="#00bff3", padx=20, pady=10,command=save)
        update_btn.place(x=550, y=630)
        clear_btn = Button(main, text="CLEAR", font=('Consolas', 15), cursor='hand2',
                           bg="#00bff3", border=0, activebackground="#00bff3", padx=25, pady=10,command=clear)
        clear_btn.place(x=715, y=630)

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
    global main1

    conn = sqlite3.connect('info.db')
    c = conn.cursor()
    c.execute('DELETE from information WHERE oid= ' + employeeID.get())
    print("Deleted successfully")

    conn.commit()
    conn.close()
    employeeID.delete(0, END)
    main1.destroy()
    os.system("contact.py")




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
# myimage=ImageTk.PhotoImage(Image.open('./images/adminmanagement1.png'))
# Label(image=myimage).pack()

# label
id_lbl=Label(root,text="Search Name-",font=('Consolas',13),bg="white")
id_lbl.place(x=330,y=118)


# entry
employeeID=Entry(root,width=25,border=0,font=('Consolas',13))
employeeID.place(x=450,y=120)
# entryID = employeeID.get()



# buttons

searchBTN=Button(root,text="Search",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3",command = search)
searchBTN.place(x=710,y=115)

addEmpBTN=Button(root,text="ADD CONTACT",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3",padx=50,)
addEmpBTN.place(x=160,y=670)

updateBTN=Button(root,text="UPDATE CONTACT",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3",padx=50, command = update)
updateBTN.place(x=455,y=670)
deleteBTN=Button(root,text="DELETE CONTACT",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3",padx=50, command = delete)
deleteBTN.place(x=768,y=670)


refreshBTN=Button(root,text="Refresh",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3", command = refresh)
refreshBTN.place(x=925,y=115)






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

my_tree.place(relx=0.1389, rely=0.203, width=840, height=500)




count=0
for record in records:
    my_tree.insert(parent='',index='end',iid=count,text="Parent",values=(record[6],record[0],record[1],record[2],record[3],record[4],record[5]))
    count+=1
conn.commit()
conn.close()
root.mainloop()