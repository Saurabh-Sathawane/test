from tkinter import *
from tkinter import messagebox
import random
import time

root=Tk()
root.geometry("1600x800+0+0")
root.title("Restaurent Management System")

text_Input= StringVar()
operator=""


Tops=Frame(root, width= 1600,height=50,bg="red",relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root, width= 800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)


f2=Frame(root, width= 300,height=700,bg="red",relief=SUNKEN)
f2.pack(side=RIGHT)
#=============TIME========#
localtime=time.asctime(time.localtime(time.time()))
#=========Info=====#


lblInfo=Label(Tops,font=('arial',50,'bold'),text="Restaurent Management System",fg="red",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="red",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
#=======calculator=====#
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnequalInput():
    global operator
    sumup=str(eval(operator))
    operator=""
    text_Input.set(sumup)
def Ref():
    x=random.randint(10908,50897)
    randomRef = str(x)
    rand.set(randomRef)

    coF=float(Large_Fries.get())
    coB=float(Burger.get())
    coD=float(drinks.get())
    cofilet=float(Filet.get())
    coChee_bur=float(Cheese_Burger.get())
    coChi_bur=float(Chicken_Burger.get())

    cos_of_fries=coF*20
    co_of_Burger=coB*25
    co_of_filet=coF*75
    co_of_drinks=coD*15
    cchib= coChi_bur*80
    ccheb=coChee_bur*50

    
    
    cost_of_meal="Rs.",str( "%.2f" % ( cos_of_fries+co_of_Burger+co_of_filet+co_of_drinks
    +cchib+ccheb))
    paytax=((cos_of_fries+co_of_Burger+co_of_filet+co_of_drinks+cchib+ccheb)*0.2)
    totaltax=(cos_of_fries+co_of_Burger+co_of_filet+co_of_drinks+cchib+ccheb)
    ser_chr=(( cos_of_fries+co_of_Burger+co_of_filet+co_of_drinks+cchib+ccheb)/99)
    ser="Rs.",str("%.2f" %ser_chr)
    overall="Rs.",str("%.2f" % (paytax+totaltax+ser_chr))
    paidtax="Rs.",str("%.2f" % paytax)

    service.set(ser)
    Cost.set(cost_of_meal)
    Tax.set(paidtax)
    Subtotal.set(cost_of_meal)
    total.set( overall)

def qexit():
    root.destroy()

def reset():
     rand.set("")
     Large_Fries.set("")
     Burger.set("")
     Filet.set("")
     Subtotal.set("")
     total.set("")
     service.set("")
     drinks.set("")
     Tax.set("")
     Cost.set("")
     Chicken_Burger.set("")
     Cheese_Burger.set("")
    

    
    
txtDisplay=Entry(f2,font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,
                 bg="red",justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="7",bg="red",command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="8",bg="red",command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="9",bg="red",command=lambda:btnClick(9)).grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="+",bg="red",command=lambda:btnClick("+")).grid(row=2,column=3)
#======
btn4=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="4",bg="red",command=lambda:btnClick(4)).grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="5",bg="red",command=lambda:btnClick(5)).grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="6",bg="red",command=lambda:btnClick(6)).grid(row=3,column=2)

Subtraction=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="-",bg="red",command=lambda:btnClick("-")).grid(row=3,column=3)

#============

btn1=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="1",bg="red",command=lambda:btnClick(1)).grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="2",bg="red",command=lambda:btnClick(2)).grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="3",bg="red",command=lambda:btnClick(3)).grid(row=4,column=2)

Multply=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="*",bg="red",command=lambda:btnClick("*")).grid(row=4,column=3)
#==========

btn0=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="0",bg="red",command=lambda:btnClick(0)).grid(row=5,column=0)

btnclear=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="C",bg="red",command=btnClearDisplay).grid(row=5,column=1)


btnEquals =Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="=",bg="red",command=btnequalInput).grid(row=5,column=2)

btnDiv=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="/",bg="red",command=lambda:btnClick("/")).grid(row=5,column=3)

#==============Restaurent info==========
rand=StringVar()
Large_Fries=StringVar()
Burger=StringVar()
Filet=StringVar()
Subtotal=StringVar()
total=StringVar()
service=StringVar()
drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Chicken_Burger=StringVar()
Cheese_Burger=StringVar()

lblref = Label(f1,font=('arial',16,'bold'),text="Reference",bd=16,anchor='w')
lblref.grid(row=0,column=0)
txtref=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,
             bg="red",justify='right')
txtref.grid(row=0,column=1)


lblfries = Label(f1,font=('arial',16,'bold'),text="Large Fries",bd=16,anchor='w')
lblfries.grid(row=1,column=0)
txtfries=Entry(f1,font=('arial',16,'bold'),textvariable=Large_Fries,bd=10,insertwidth=4,
             bg="red",justify='right')
txtfries.grid(row=1,column=1)

lblburger = Label(f1,font=('arial',16,'bold'),text="Burger Meal",bd=16,anchor='w')
lblburger.grid(row=2,column=0)
txtburger=Entry(f1,font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4,
             bg="red",justify='right')
txtburger.grid(row=2,column=1)

lblfilet = Label(f1,font=('arial',16,'bold'),text="Filet_o_Meal",bd=16,anchor='w')
lblfilet.grid(row=3,column=0)
txtfilet=Entry(f1,font=('arial',16,'bold'),textvariable=Filet,bd=10,insertwidth=4,
             bg="red",justify='right')
txtfilet.grid(row=3,column=1)

lblchicken= Label(f1,font=('arial',16,'bold'),text="Chicken Meal",bd=16,anchor='w')
lblchicken.grid(row=4,column=0)
txtchicken=Entry(f1,font=('arial',16,'bold'),textvariable=Chicken_Burger,bd=10,insertwidth=4,
             bg="red",justify='right')
txtchicken.grid(row=4,column=1)

lblcheese = Label(f1,font=('arial',16,'bold'),text="cheese meal",bd=16,anchor='w')
lblcheese.grid(row=5,column=0)
txtcheese=Entry(f1,font=('arial',16,'bold'),textvariable=Cheese_Burger,bd=10,insertwidth=4,
             bg="red",justify='right')
txtcheese.grid(row=5,column=1)


#======Resto.. info 2..=====
lbldrinks = Label(f1,font=('arial',16,'bold'),text="Drinks",bd=16,anchor='w')
lbldrinks.grid(row=0,column=2)
txtdrinks=Entry(f1,font=('arial',16,'bold'),textvariable=drinks,bd=10,insertwidth=4,
             bg="red",justify='right')
txtdrinks.grid(row=0,column=3)


lblcost = Label(f1,font=('arial',16,'bold'),text="cost",bd=16,anchor='w')
lblcost.grid(row=1,column=2)
txtcost=Entry(f1,font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,
             bg="red",justify='right')
txtcost.grid(row=1,column=3)

lblservice = Label(f1,font=('arial',16,'bold'),text="service",bd=16,anchor='w')
lblservice.grid(row=2,column=2)
txtservice=Entry(f1,font=('arial',16,'bold'),textvariable=service,bd=10,insertwidth=4,
             bg="red",justify='right')
txtservice.grid(row=2,column=3)

lbltax = Label(f1,font=('arial',16,'bold'),text="Tax",bd=16,anchor='w')
lbltax.grid(row=3,column=2)
txttax=Entry(f1,font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,
             bg="red",justify='right')
txttax.grid(row=3,column=3)

lblsub= Label(f1,font=('arial',16,'bold'),text="Subtotal",bd=16,anchor='w')
lblsub.grid(row=4,column=2)

txtsub=Entry(f1,font=('arial',16,'bold'),textvariable=Subtotal,bd=10,insertwidth=4,
             bg="red",justify='right')
txtsub.grid(row=4,column=3)

lbltot = Label(f1,font=('arial',16,'bold'),text="Total",bd=16,anchor='w')
lbltot.grid(row=5,column=2)
txttot=Entry(f1,font=('arial',16,'bold'),textvariable=total,bd=10,insertwidth=4,
             bg="red",justify='right')
txttot.grid(row=5,column=3)


#========buttons======
btnref=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,
                text='Ref no.',bg="red",command=Ref).grid(row=7,column=1)
btnreset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,
                text='Reset',bg="red",command=reset).grid(row=7,column=2)
btnexit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,
                text='Exit',bg="red",command=qexit).grid(row=7,column=3)


root.mainloop()

