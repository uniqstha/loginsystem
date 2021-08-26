from tkinter import *
from tkinter import messagebox
import sqlite3

from PIL import Image, ImageTk

root = Tk()
root.lift()
root.geometry("1366x768+60+10")
root.title("Employee Management System")
root.resizable(0, 0)


# root.iconbitmap('./images/1.ico')


def Exit():
    sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=root)
    if sure == True:
        root.destroy()


root.protocol("WM_DELETE_WINDOW", Exit)


def login():
    global myimage
    global root1

    def login_database():
        conn = sqlite3.connect("info.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM information WHERE Email=? AND Password=?", (e1.get(), e2.get()))
        row = cur.fetchall()
        conn.close()
        print(row)
        if row != []:
            e_mail = row[0][5]
            # Label(root1,text="user name found with name: " + user_name).place(x=100,y=100)
            messagebox.showinfo("LOGIN SUCESS", "User Found With Email: " + e_mail)
        else:
            messagebox.showinfo("LOGIN FAILED", "User Not Found ")

    root1 = Toplevel()
    root1.geometry("1366x768+60+10")
    myimage = ImageTk.PhotoImage(Image.open('login.png'))
    Label(root1, image=myimage).pack()
    username_lbl = Label(root1, text='UserName', font=('Consolas', 15), bg='white')
    username_lbl.place(x=484, y=225)
    password_lbl = Label(root1, text='Password', font=('Consolas', 15), bg='white')
    password_lbl.place(x=484, y=325)
    # e1 entry for username entry
    e1 = Entry(root1, width=40, border=0, font=('Consolas', 13))
    e1.place(x=510, y=258)

    # e2 entry for password entry
    e2 = Entry(root1, width=40, border=0, show='*', font=('Consolas', 13))
    e2.place(x=510, y=362)

    Button(root1, text='LOGIN', font=('Consolas', 20), padx=150, pady=8, cursor='hand2', border=0, bg="#834dd6",
           activebackground="#834dd6", command=login_database).place(x=485, y=532)
    root1.mainloop()


def signup():
    global root2
    global myimg


    def signup_database():
        conn = sqlite3.connect("info.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS information(
		        Full_Name text,
		        Age integer,
		        Address text,
		        Gender integer,
		        Email text,
		        Password text
		 )""")

        c.execute("INSERT INTO information VALUES (:Full_name, :Age, :Address, :Gender, :Email, :Password)", {

            'Full_name': fullname.get(),
            'Age': age.get(),
            'Address': address.get(),
            'Gender': var.get(),
            'Email': email.get(),
            'Password': password.get()

        })
        messagebox.showinfo("Prompt", "Account Created Successfully: ")
        conn.commit()
        conn.close()


    root2 = Toplevel()
    # root.iconbitmap('ico.ico')
    root2.geometry("1366x768+60+10")
    root2.resizable(0, 0)
    root2.title("Login")

    myimg = ImageTk.PhotoImage(Image.open('signup.png'))
    Label(root2, image=myimg).pack()

    fullname_lbl = Label(root2, text="Full Name", font=('Consolas', 15), bg="white")
    fullname_lbl.place(x=180, y=200)
    age_lbl = Label(root2, text="Age", font=('Consolas', 15), bg="white")
    age_lbl.place(x=720, y=200)
    address_lbl = Label(root2, text="Address", font=('Consolas', 15), bg="white")
    address_lbl.place(x=180, y=290)
    gender_lbl = Label(root2, text="Gender", font=('Consolas', 15), bg="white")
    gender_lbl.place(x=720, y=290)
    email_lbl = Label(root2, text="Email", font=('Consolas', 15), bg="white")
    email_lbl.place(x=180, y=380)
    password_lbl = Label(root2, text="Password", font=('Consolas', 15), bg="white")
    password_lbl.place(x=720, y=380)

    fullname = Entry(root2, width=40, border=0, font=('Consolas', 15))
    fullname.place(x=180, y=230)
    age = Entry(root2, width=40, border=0, font=('Consolas', 15))
    age.place(x=720, y=230)
    address = Entry(root2, width=40, border=0, font=('Consolas', 15))
    address.place(x=180, y=320)

    email = Entry(root2, width=40, border=0, font=('Consolas', 15))
    email.place(x=180, y=410)
    password = Entry(root2, width=40, border=0, font=('Consolas', 15))
    password.place(x=720, y=410)
    submit_btn = Button(root2, text="SUBMIT", font=('Consolas', 15), cursor='hand2',
                        bg="#834dd6", border=0, activebackground="#834dd6", padx=22, pady=10, )
    var = StringVar()
    r1 = Radiobutton(root2, text="Male", bg='white', activebackground='white', font=('Consolas', 15), value='Male',
                     variable=var)
    r1.deselect()
    r1.place(x=720, y=320)
    r2 = Radiobutton(root2, text="Female", bg='white', activebackground='white', font=('Consolas', 15), value='Female',
                     variable=var)
    r2.place(x=820, y=320)
    r3 = Radiobutton(root2, text="other", bg='white', activebackground='white', font=('Consolas', 15), value="Others",
                     variable=var)
    r3.place(x=920, y=320)

    check = IntVar()
    checkbtn = Checkbutton(root2, text="Terms and Conditions", font=('Consolas', 20), bg="white",
                           activebackground="white", variable=check, onvalue=1, offvalue=0)
    checkbtn.deselect()
    checkbtn.place(x=525, y=540)
    submit_btn = Button(root2, text="SUBMIT", font=('Consolas', 15), cursor='hand2',
                        bg="#834dd6", border=0, activebackground="#834dd6", padx=22, pady=10, command=signup_database)
    submit_btn.place(x=544, y=630)
    exit_btn = Button(root2, text="EXIT", font=('Consolas', 15), cursor='hand2',
                      bg="#834dd6", border=0, activebackground="#834dd6", padx=25, pady=10, )
    exit_btn.place(x=715, y=630)


def exit():
    root.destroy()


label1 = Label(root)
label1.place(x=0, y=0, width=1366, height=768)
img = PhotoImage(file="./loginas.png")
label1.configure(image=img)

button1 = Button(root, bg='white', fg='white', activebackground="white", relief="flat", overrelief="flat",
                 borderwidth="0",
                 cursor='hand2', command=login)
button1.place(x=435, y=330, width=146, height=90)
img2 = PhotoImage(file="existing.png")
button1.configure(image=img2)
Label(root, text='Existing User', bg='white', font=('Consolas', 15)).place(x=429, y=410)

button2 = Button(root, bg='white', fg='white', activebackground="white", relief="flat", overrelief="flat",
                 borderwidth="0",
                 cursor='hand2', command=signup)
button2.place(x=779, y=330, width=146, height=90)
img3 = PhotoImage(file="new.png")
button2.configure(image=img3)
Label(root, text='New User', bg='white', font=('Consolas', 14)).place(x=810, y=410)

Button(root, text='EXIT', font=('Consolas', 25), padx=40, cursor='hand2', border=0, bg="#834dd6",
       activebackground="#834dd6", command=exit).place(x=590, y=600)

root.mainloop()
