from tkinter import *
import tkinter.messagebox
import sqlite3
import time
import datetime
import random

conn= sqlite3.connect("account.db")
c= conn.cursor()
###################################################################################################################
def newAcc() :

    window = Toplevel(master)
    window.title("New Account")
    window.geometry('400x200')

    label0 = Label(window,text="NEW ACCOUNT",bg="lightgreen",fg="white")
    label0.config(font=("ariel",12))
    label0.grid(row=0,column=1)

    #label to enter name
    label1 = Label(window,text="Name :")
    label1.config(font=("ariel",12))
    label1.grid(row=1,column=0,sticky=W)

    #label to enter password
    label2 = Label(window,text="Phone Number : (+91)")
    label2.config(font=("ariel",12))
    label2.grid(row=2,column=0,sticky=W)

    # third label to enter amount
    label3 = Label(window,text="Address :")
    label3.config(font=("ariel",12))
    label3.grid(row=3,column=0,sticky=W)

    label4 = Label(window,text="User Name :")
    label4.config(font=("ariel",12))
    label4.grid(row=4,column=0,sticky=W)

    label5 = Label(window,text="Set Password :")
    label5.config(font=("ariel",12))
    label5.grid(row=5,column=0,sticky=W)



    E1= Entry(window)
    E1.grid(row=1,column=1)


    E2= Entry(window)
    E2.grid(row=2,column=1)


    E3= Entry(window)
    E3.grid(row=3,column=1)

    E4= Entry(window)
    E4.grid(row=4,column=1)


    E5= Entry(window)
    E5.grid(row=5,column=1)

    def quit_window() :
         window.destroy()

    quit= Button(window,text="Cancel",fg='red',bg='white',command=quit_window)
    quit.grid(row=6,column=2)


    # SQLite

    def create_table():
      c.execute('CREATE TABLE IF NOT EXISTS newAccount(name TEXT, phone TEXT,address text,userName TEXT, password TEXT)')

    #create_table()

    def data_entry():

        name=str(E1.get())
        phone=str(E2.get())
        address=str(E3.get())
        userName=E4.get()
        password= E5.get()

        c.execute("Select userName FROM newAccount Where userName=(?)",(userName,))
        names=c.fetchone()

        if names==None:
           c.execute("INSERT INTO newAccount (name,phone,address,userName,password) VALUES (?, ?, ?, ?, ?)", (name, phone, address, userName, password))
           conn.commit()
           mbox=tkinter.messagebox.showinfo("Success!", "Your account has been successfully created !!")
           quit_window()

        else:
            names=str(names[0])
            if names==userName :
              mbox=tkinter.messagebox.showwarning("Invalid Username", "This Username already exists!!")
              quit_window()
              newAcc()

    b1= Button(window,text="Enter",command=data_entry)
    b1.grid(row=6,column=1)
    #data_entry()

    create_table()
####################################################################################################################

####################################################################################################################
def loginAcc():
    window = Toplevel(master)
    window.title("Login")
    window.geometry('400x200')
    label0 = Label(window,text="LOGIN ACCOUNT")
    label0.config(font=("ariel",12))
    label0.grid(row=0,column=1)

    #label to enter username
    label1 = Label(window,text="UserName :")
    label1.config(font=("ariel",12))
    label1.grid(row=1,column=0,sticky=W)

    #label to enter password
    label2 = Label(window,text="Password :")
    label2.config(font=("ariel",12))
    label2.grid(row=2,column=0,sticky=W)

    E1= Entry(window)
    E1.grid(row=1,column=1)

    E2= Entry(window,show="*")
    E2.grid(row=2,column=1)

    userName_E=E1.get()

    def account_info() :
        window2 = Toplevel(window)
        window2.title("Account Information")
        window2.geometry('400x400')

        labelin = Label(window2,text="ACCOUNT INFO :")
        labelin.config(font=("ariel",12))
        labelin.grid(row=0,column=0)

        c.execute("CREATE TABLE IF NOT EXISTS account (id integer primary key autoincrement, userName TEXT,"
                  " balance INTEGER, dateStamp TEXT)")
        c.execute("INSERT INTO account (userName) SELECT (userName) FROM newAccount")

        #name displayed
        usern=E1.get()
        c.execute("SELECT name FROM newAccount WHERE userName = (?)",(usern,))
        temp=c.fetchone()
        lname = Label(window2,text="WELCOME : " + temp[0])
        lname.grid(row=3,column=0)
        lname.config(font=("ariel",12))
        # account number displayed
        c.execute("SELECT id FROM account WHERE userName=(?)",(usern,))
        accnum=c.fetchone()
        accnum=str(accnum[0])
        name=Label(window2,text="Your Account Number is :  " + accnum).grid(row=4,column=0)

        #balance display
        c.execute("SELECT balance FROM account WHERE userName=(?)",(usern,))
        bal=c.fetchone()
        bal=str(bal[0])
        li=Label(window2,text="Your Account Balance is : " + bal).grid(row=6,column=0)

        #time stamp
        unix=time.time()
        date =str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        print (date)
        def locker():
            windowl=Toplevel(window2)
            windowl.title("Lockers")
            windowl.geometry('400x200')

            labelaccnum = Label(windowl,text="Avail Locker for : " + accnum)
            labelaccnum.config(font=("ariel",14))
            labelaccnum.grid(row=1,column=0)

            label2o = Label(windowl,text="Select type :")
            label2o.config(font=("ariel",14))
            label2o.grid(row=2,column=0,sticky=W)

            var1=IntVar()
            Checkbutton(windowl, text="Size=200x200", variable=var1).grid(row=3, sticky=W)
            var2=IntVar()
            Checkbutton(windowl, text="Size=500x500", variable=var2).grid(row=4, sticky=W)

            def lock():
                lbl= Label(windowl,text="your locker number is : "+ accnum)
                lbl.grid(row=6)
                a=random.randint(10000,999999)
                a=str(a)
                b=random.randint(0,9)
                b=str(b)
                lbl2= Label(windowl,text="your locker password is : "+a+"b"+b).grid(row=7)

            b1= Button(windowl,text="Get Locker",command=lock).grid(row=5,column=2)


        def depWith2() :
           window3 = Toplevel(window2)
           window3.title("Deposit and Withdraw money")
           window3.geometry('400x200')

           #label to displayaccount number
           labelaccnum = Label(window3,text="Transaction on account : " + accnum)
           labelaccnum.config(font=("ariel",14))
           labelaccnum.grid(row=1,column=0)

           #label to enter amount
           label2o = Label(window3,text="Enter Amount :")
           label2o.config(font=("ariel",14))
           label2o.grid(row=2,column=0,sticky=W)

           # amount entry
           amt= Entry(window3)
           amt.grid(row=2,column=1)

           # deposit ka logic #

           def exit() :
               window3.destroy()


           def deposit() :

             amtE=amt.get()
             amtE=int(amtE)
             c.execute("SELECT balance FROM account WHERE id=(?)",(accnum,))
             balanceamt = c.fetchall()
             balance=balanceamt[0]
             balance=balance[0]
             if balance==None:
                 balance=0
             balance=int(balance)
             print(balance)
             #print(balance,depamt)
             newBalance= balance + amtE
             newBalance=int(newBalance)
             c.execute("UPDATE account SET balance = (?) WHERE id=(?)",(newBalance,accnum,))
             conn.commit()
             mbox=tkinter.messagebox.showinfo("Success!", "Deposit successful!")
             exit()

           b1= Button(window3,text="EnterAmount",command=deposit)
           b1.grid(row=4,column=1)

           quit= Button(window3,text="Cancel",fg='red',bg='white',command=exit)
           quit.grid(row=4,column=2)


         # withdraw ki window
        def withdraw() :
            window3 = Toplevel(window2)
            window3.title("Deposit and Withdraw money")
            window3.geometry('400x200')

            #label to displayaccount number
            labelaccnum = Label(window3,text="Transaction on account : " + accnum)
            labelaccnum.config(font=("ariel",14))
            labelaccnum.grid(row=1,column=0)

            #label to enter amount
            label2o = Label(window3,text="Enter Amount :")
            label2o.config(font=("ariel",14))
            label2o.grid(row=2,column=0,sticky=W)

            # amount entry
            amt= Entry(window3)
            amt.grid(row=2,column=1)

           # withdraw ka logic

            def exit() :
                window3.destroy()

            def withd() :
                amtE=amt.get()
                amtE=int(amtE)
                c.execute("SELECT balance FROM account WHERE id=(?)",(accnum,))
                balanceamt = c.fetchall()
                balance=balanceamt[0]
                balance=balance[0]
                if balance==None:
                  balance=0
                balance=int(balance)
                print(balance)
                #print(balance,depamt)
                if(balance-amtE>0):
                  newBalance= balance - amtE
                  newBalance=int(newBalance)
                  c.execute("UPDATE account SET balance = (?) WHERE id=(?)",(newBalance,accnum,))
                  conn.commit()
                  mbox=tkinter.messagebox.showinfo("Success!", "withdraw successful!")
                  exit()
                else:
                    mbox=tkinter.messagebox.showwarning("Invalid Request", "withdraw Unsuccessful,Check Amount")
                    exit()


            b1= Button(window3,text="EnterAmount",command=withd)
            b1.grid(row=4,column=1)

            quit= Button(window3,text="Cancel",fg='red',bg='white',command=exit)
            quit.grid(row=4,column=2)

        def quit_window() :
            window2.destroy()

        def refresh():
            quit_window()
            window.destroy()
            loginAcc()


        depbtn=Button(window2,text="Deposit",command=depWith2).grid(row=7,column=0)
        withbtn=Button(window2,text="WITHDRAW",command=withdraw).grid(row=7,column=1)
        logout=Button(window2,text="LOGOUT",command=quit_window).grid(row=8,column=0)
        refresh=Button(window2,text="refresh",command=refresh,bg="lightgreen").grid(row=8,column=1)
        locker=Button(window2,text="Locker",command=locker,bg="lightblue").grid(row=9,column=0)
#######################################################################################################################################################
    def login():
        try :
          password_E=str(E2.get())
          user=str(E1.get())
          c.execute("SELECT password FROM newAccount WHERE userName=(?)",(user,))
          password=c.fetchone()
          password=(str(password[0]))
          #print(password_E)
        #print(password)
          if password_E==password :
              mbox=tkinter.messagebox.showinfo("Success!", "You have successfully logged into account")
              account_info()
          else :
              mbox=tkinter.messagebox.showwarning("Warning!", "Incorrect username or password ! TRY AGAIN!!")

        except TypeError :
            mbox=tkinter.messagebox.showwarning("Warning!", "Incorrect username or password ! TRY AGAIN!!")
            window.destroy()
            loginAcc()

########################################################################################################################
    def admin():
      try:
        adm=Toplevel(window)
        adm.title("ADMIN LOGIN")
        adm.geometry('300x200')

        lbl=Label(adm,text="username : ").grid(row=1)
        ent=Entry(adm)
        ent.grid(row=1,column=1)


        lbl2=Label(adm,text="password : ").grid(row=2)
        ent2=Entry(adm,show="*")
        ent2.grid(row=2,column=1)

        a=ent
        p=ent2

        def but():
            en=ent.get()
            en2=ent2.get()
            print(en+" "+en2)
            if (en=="admin"):
                if(en2=="admin"):
                    mbox=tkinter.messagebox.showinfo("Success!", "You have successfully logged into account")
                    ad()
            else :
                mbox=tkinter.messagebox.showinfo("Try Again!", "Invalid Username or Password")
                adm.destroy()
                admin()


        # admin profile
        def ad():
            adm1=Toplevel(adm)
            adm1.title("ADMIN Control")
            adm1.geometry('300x200')

            #print account list
            def al():
                adm2=Toplevel(adm1)
                adm2.geometry('500x400')
                c.execute("SELECT name,phone,address FROM newAccount")
                t=c.fetchall()
                l=len(t)
                row=1
                for i in range(0,l):
                 q=len(t[i])-1
                 r=t[i]
                 for j in range(0,3):
                  if j==0:
                    labl=Label(adm2,text="NAME: "+r[j]).grid(row=row,sticky=W)
                    row+=row
                  elif j==1 :
                    Label(adm2,text="PHONE NUMBER:"+r[j]).grid(row=row,sticky=W)
                    row=row+1
                  if j==2 :
                    Label(adm2,text="ADDRESS:"+r[j]).grid(row=row,sticky=W)
                    row=row+1

            def delacc():
                 adm3=Toplevel(adm1)
                 adm3.title("Delete account")
                 adm3.geometry('500x400')

                 Label(adm3,text="Enter name:").grid(row=1,column=0)
                 Ent=Entry(adm3)
                 Ent.grid(row=1,column=1)


                 Label(adm3,text="Enter account number:").grid(row=2,column=0)
                 Ent2=Entry(adm3)
                 Ent2.grid(row=2,column=1)


                 def dele():
                   name=Ent.get()
                   name=str(name)
                   acnum=Ent2.get()
                   acnum=int(acnum)
                   c.execute("DELETE FROM newAccount WHERE name=(?)",(name,))
                   c.execute("DELETE FROM account WHERE id=(?)",(acnum,))
                   conn.commit()
                   mbox=tkinter.messagebox.showinfo("Success!", "You have successfully deleted account")
                   adm3.destroy()

                 Bt=Button(adm3,text="delete",command=dele).grid(row=3,column=0)

            bt1=Button(adm1,text="account list",command=al,bg="lightgreen").grid(row=1,column=0,sticky=W)
            bt2=Button(adm1,text="delete account",bg="lightblue",command=delacc).grid(row=2,column=0,sticky=E)
            def quits():
                adm.destroy()
            bt3=Button(adm1,text="Quit",bg="red",command=quits).grid(row=3,column=1,sticky=E)

        but1 = Button(adm,text="enter",command=but).grid(row=3)
      except TypeError :
        mbox=tkinter.messagebox.showwarning("Warning!", "Incorrect username or password ! TRY AGAIN!!")
        adm.destroy()
        admin()
########################################################################################################################
    b2=Button(window,text="Admin",command=admin).grid(row=5)
    b1= Button(window,text="enter",command=login)
    b1.grid(row=3,column=1)
########################################################################################################################
def loan() :
  try:
    window = Toplevel(master)
    window.title("EMI Calculator")
    window.geometry('400x200')

    #label to displayaccount number
    label1 = Label(window,text="Select the type of loan you want :")
    label1.config(font=("ariel",14))
    label1.grid(row=1,column=0)

    var1 = IntVar()
    Checkbutton(window, text="Home Loan", variable=var1).grid(row=2, sticky=W)
    var2 = IntVar()
    Checkbutton(window, text="Car Loan", variable=var2).grid(row=3, sticky=W)

    #label to enter password
    label2 = Label(window,text="Enter Amount :")
    label2.config(font=("ariel",12))
    label2.grid(row=4,column=0,sticky=W)

    E1= Entry(window)
    E1.grid(row=4,column=1,columnspan=2)


    label3 = Label(window,text="Enter Time in months :")
    label3.config(font=("ariel",12))
    label3.grid(row=5,column=0,sticky=W)

    E2= Entry(window)
    E2.grid(row=5,column=1,columnspan=2)

    def calc():
        #win=Toplevel(window)
        #win.title("EMI")
        #win.geometry(100*100)
        amt=int(E1.get())
        tim=int(E2.get())
        emi=str((1.3*amt)/tim)
        emi=emi.zfill(8)
        Label(window,text="Your emi will be : " + emi ).grid(row=6,column=0)


    b1= Button(window,text="Calculate EMI",command=calc)
    b1.grid(row=7,column=0)
    def cancel() :
        window.destroy()
    quit= Button(window,text="Cancel",fg='red',bg='white',command=cancel)
    quit.grid(row=7,column=1)

  except ValueError :
      tkinter.messagebox.showwarning("NOTE", "invalid response try again!")
####################################################################################################################
# MAIN FRAME ie MASTER

master = Tk()
master.title("Bank Management System")
master.geometry('360x300')
label = Label(master, text="Bank Management System")

photo = PhotoImage(file="bank.png")
photo_label=Label(master,image=photo)
photo_label.place(x=1,y=2)

e1 = Entry(master,bg="LIGHTGREEN")
e1.grid(row=5, column=0)

listbox = Listbox(master)
listbox.grid(row=2,column=0)
listbox.insert(END, "Enter an option :")
for item in [" ","1 for New Account","","2 for login"," ","3 for EMI CALCULATOR"," ","4 for Lockers"]:
    listbox.insert(END, item)
    listbox.config(font=("ariel",12))
def button_press():
  try:
    a=e1.get()
    b=int(a)
    print("You have selected %s " % (b))
    if b==1 :
        ans = tkinter.messagebox.askquestion("NOTE", "you want to open a new account ?")
        if ans=='yes':
          newAcc()

    if b==2 :
        ans = tkinter.messagebox.askquestion("NOTE", "You Want to LOGIN to your account?")
        if ans=='yes':
            loginAcc()

    if b==3 :
       loan()

    if b==4 :
        ans = tkinter.messagebox.askquestion("NOTE", "Apply for locker ? ")
        if ans=='yes':
            loginAcc()

    if b>4 :
        ans = tkinter.messagebox.showwarning("NOTE", "invalid response try again!")

  except ValueError :
      tkinter.messagebox.showwarning("NOTE", "invalid response try again!")
#####################################################################################################################

b1 = Button(master, text='Enter', command=button_press,bg="green",fg="white").grid(row =5, column=4)
b2 = Button(master, text='Quit', command=master.quit,bg="red",fg="white").grid(row =5, column=6)

mainloop()
