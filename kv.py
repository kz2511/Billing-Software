"""
Created on Wed Apr 22 10:22:00 2020

@author: KUNAL ZAVERI
"""

from tkinter import*
import random
import time,csv
import pymysql

root = Tk()
root.geometry("890x580+0+0")
root.title("KV CAFE ")

Tops = Frame(root,bg="blue",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
#------------------TIME--------------

localtime=time.asctime(time.localtime(time.time()))

#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'aria' ,30, 'italic' ),text=" KV CAFE & FOOD ",fg="red",bd=6,anchor='w')
lblinfo.grid(row=0,column=0)

lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="steel blue",anchor='w')
lblinfo.grid(row=2,column=0)

lblinfo = Label(Tops, font=( 'aria' ,30, 'italic' ),text=" 18012021094 & KUNAL ZAVERI  ",fg="green",bd=6,anchor='w')
lblinfo.grid(row=3,column=0)


def err_screen_for_subject():
    def ec_delete():
        ec.destroy()

    global ec
    ec = Tk()
    ec.geometry('300x100')
    ec.title('Warning!!')
    Label(ec, text='Please enter all Quantity!!!', fg='red', font=('times', 16, ' bold ')).pack()
    Button(ec, text='OK', command=ec_delete, fg="black", bg="lawn green", width=9, height=1, activebackground="Red",
           font=('times', 15, ' bold ')).place(x=90, y=50)

def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)
    try:
 #       global cof,colfries,cob,cofi,cochee,codr
        cof =float(Fries.get())
        colfries= float(Largefries.get())
        cob= float(Burger.get())
        cofi= float(Filet.get())
        cochee= float(Cheese_burger.get())
        codr= float(Drinks.get())

        costoffries = cof * 25
        costoflargefries = colfries * 40
        costofburger = cob * 35
        costoffilet = cofi * 50
        costofcheeseburger = cochee * 30
        costofdrinks = codr * 35

        cofm2 = costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks
        costofmeal = "Rs.", str(
            '%.2f' % (costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
        PayTax = ((
                              costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks) * 0.33)
        Totalcost = (costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)
        Ser_Charge = ((
                                  costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks) / 99)
        Service = "Rs.", str('%.2f' % Ser_Charge)
        ovalc2 = PayTax + Totalcost + Ser_Charge
        OverAllCost = "Rs.", str(PayTax + Totalcost + Ser_Charge)
        PaidTax = "Rs.", str('%.2f' % PayTax)

        Service_Charge.set(Service)
        cost.set(costofmeal)
        Tax.set(PaidTax)
        Subtotal.set(costofmeal)
        Total.set(OverAllCost)


        con = pymysql.connect("localhost","root","",database="Py_Project")
        cursor = con.cursor()
        query = "Insert into billing_details values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(str(x), str(codr), str(cof), str(colfries), str(cob), str(cofi), str(cochee), str(cofm2), str(ovalc2))
        cursor.execute(query)
        con.commit()
        
        
        # row = [Enrollment, Name, Date, Time]
        # with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
        #     writer = csv.writer(csvFile, delimiter=',')
        #     writer.writerow(row)
        #     csvFile.close()

        with open('OrderDetails.csv', 'a+') as csvFile:
            rows = [costofmeal,PayTax,Totalcost,Ser_Charge,Service,OverAllCost,PaidTax]
            writer = csv.writer(csvFile, delimiter=',')
            writer.writerow(rows)
            csvFile.close()
    except Exception as e:
        print(e)
        #rand.set("")
        #err_screen_for_subject()

def qexit():
    root.destroy()

def reset():
    rand.set("")
    Fries.set("")
    Largefries.set("")
    Burger.set("")
    Filet.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Cheese_burger.set("")


#---------------------------------------------------------------------------------------
rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = StringVar()


lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="brown",bd=20,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1,font=('ariel' ,16,'bold'), state=DISABLED,textvariable=rand , bd=6,insertwidth=6,bg="blue" ,justify='right')
txtreference.grid(row=0,column=1)

lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text=" French Fries ",fg="blue",bd=10,anchor='w')
lblfries.grid(row=2,column=0)
txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="yellow" ,justify='right')
txtfries.grid(row=2,column=1)

lblLargefries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Lunch ",fg="blue",bd=10,anchor='w')
lblLargefries.grid(row=3,column=0)
txtLargefries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Largefries , bd=6,insertwidth=4,bg="green" ,justify='right')
txtLargefries.grid(row=3,column=1)


lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Burger ",fg="blue",bd=10,anchor='w')
lblburger.grid(row=4,column=0)
txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Burger , bd=6,insertwidth=4,bg="red" ,justify='right')
txtburger.grid(row=4,column=1)

lblFilet = Label(f1, font=( 'aria' ,16, 'bold' ),text="Pizza ",fg="blue",bd=10,anchor='w')
lblFilet.grid(row=5,column=0)
txtFilet = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Filet , bd=6,insertwidth=4,bg="pink" ,justify='right')
txtFilet.grid(row=5,column=1)

lblCheese_burger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cheese burger",fg="blue",bd=10,anchor='w')
lblCheese_burger.grid(row=6,column=0)
txtCheese_burger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Cheese_burger , bd=6,insertwidth=4,bg="green" ,justify='right')
txtCheese_burger.grid(row=6,column=1)

#--------------------------------------------------------------------------------------
lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="blue",bd=10,anchor='w')
lblDrinks.grid(row=1,column=0)
txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="blue" ,justify='right')
txtDrinks.grid(row=1,column=1)

lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cost",fg="black",bd=10,anchor='w')
lblcost.grid(row=2,column=2)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), state=DISABLED,textvariable=cost , bd=6,insertwidth=4,bg="white" ,justify='right')
txtcost.grid(row=2,column=3)

lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="black",bd=10,anchor='w')
lblService_Charge.grid(row=3,column=2)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), state=DISABLED,textvariable=Service_Charge , bd=6,insertwidth=4,bg="white" ,justify='right')
txtService_Charge.grid(row=3,column=3)

lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="black",bd=10,anchor='w')
lblTax.grid(row=4,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'),state=DISABLED, textvariable=Tax , bd=6,insertwidth=4,bg="white" ,justify='right')
txtTax.grid(row=4,column=3)

lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="black",bd=10,anchor='w')
lblSubtotal.grid(row=5,column=2)
txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), state=DISABLED,textvariable=Subtotal , bd=6,insertwidth=4,bg="white" ,justify='right')
txtSubtotal.grid(row=5,column=3)

lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="green",bd=10,anchor='w')
lblTotal.grid(row=6,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'),state=DISABLED, textvariable=Total , bd=6,insertwidth=4,bg="grey" ,justify='right')
txtTotal.grid(row=6,column=3)

#-----------------------------------------buttons------------------------------------------
lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=7,columnspan=3)

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="red",command=Ref)
btnTotal.grid(row=8, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="red",command=reset)
btnreset.grid(row=8, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="red",command=qexit)
btnexit.grid(row=8, column=3)

def price():
    roo = Tk()
    roo.geometry("800x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="French Fries", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lunch ", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger ", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza ", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)
    

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="red",command=price)
btnprice.grid(row=8, column=0)

root.mainloop()