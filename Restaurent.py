from tkinter import *
import random
import time;
win=Tk()
win.geometry('1600x800+0+0')
win.title('Restaurant Managment System')

#here is text_input and some commond
text_input=StringVar()
operator=""

def Btnclick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)
def Eqral():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=''
def clear():
    global operator
    operator=''
    text_input.set(operator)
    



#Frame work
Tops=Frame(win,width=1600,bg='Powder blue',relief=SUNKEN)
Tops.pack(side=TOP)
f1=Frame(win,width=800,height=700,relief=RAISED)
f1.pack(side=LEFT)
f2=Frame(win,width=800,height=700,relief=RAISED)
f2.pack(side=RIGHT)

#there is time function
Local_Time=time.asctime(time.localtime(time.time()))

#Info work as time
Info=Label(Tops,font=('arial',50,'bold'),text='Restaurant Managment System' ,fg='Red',bd=10,anchor=W)
Info.grid(row=0,column=0)
Info=Label(Tops,font=('arial',20,'bold'),text=Local_Time ,fg='Green',bd=10,anchor=W)
Info.grid(row=1,column=0)

#time to built calculater in f2

txtDisplay=Entry(f2,font=('arial',20,'bold'),textvariable=text_input,bd=30,insertwidth=4,bg='Powder Blue',justify='right')
txtDisplay.grid(columnspan=4)

# Now creation of button
B7=Button (f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='7',bg='Powder Blue',command=lambda:Btnclick(7)).grid(row=2,column=0)
B8=Button (f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='8',bg='Powder Blue',command=lambda:Btnclick(8)).grid(row=2,column=1)
B9=Button (f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='9',bg='Powder Blue',command=lambda:Btnclick(9)).grid(row=2,column=2)
#for addition 
Addition=Button (f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='+',bg='Powder Blue',command=lambda:Btnclick('+')).grid(row=2,column=3)

B4=Button (f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='4',bg='Powder Blue',command=lambda:Btnclick(4)).grid(row=3,column=0)
B5=Button (f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='5',bg='Powder Blue',command=lambda:Btnclick(5)).grid(row=3,column=1)
B6=Button (f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='6',bg='Powder Blue',command=lambda:Btnclick(6)).grid(row=3,column=2)
#for substraction 
substraction=Button (f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='-',bg='Powder Blue',command=lambda:Btnclick('-')).grid(row=3,column=3)

B1=Button (f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='1',bg='Powder Blue',command=lambda:Btnclick(1)).grid(row=4,column=0)
B2=Button (f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='2',bg='Powder Blue',command=lambda:Btnclick(2)).grid(row=4,column=1)
B3=Button (f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='3',bg='Powder Blue',command=lambda:Btnclick(3)).grid(row=4,column=2)
#for Division 
Division=Button (f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='/',bg='Powder Blue',command=lambda:Btnclick('/')).grid(row=4,column=3)

zero=Button (f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='0',bg='Powder Blue',command=lambda:Btnclick(0)).grid(row=5,column=0)

mult=Button (f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='*',bg='Powder Blue',command=lambda:Btnclick('*')).grid(row=5,column=1)

equal=Button (f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='=',bg='Powder Blue',command=Eqral).grid(row=5,column=2)

clr=Button (f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='C',bg='Powder Blue',command=clear).grid(row=5,column=3)

#Now second forms creation

#method for second form
rand=StringVar()

fric=StringVar()
fric.set('0')
Burg=StringVar()
Burg.set('0')
Filet=StringVar()
Filet.set('0')
service_chrage=StringVar()
service_chrage.set('100')
Drinks=StringVar()
Drinks.set('0')
Tax=StringVar()
Tax.set('90')
Cost=StringVar()
chiken_burger=StringVar()
chiken_burger.set('0')
cheese_burger=StringVar()
cheese_burger.set('0')
Dos=StringVar()
Dos.set('0')


refrence1=Label(f1,font=('arial',16,'bold'),text='Reference',bd=16,anchor='w')
refrence1.grid(row=0,column=0)
txtrefrence=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=16,insertwidth=4,bg='powder blue',justify='right')
txtrefrence.grid(row=0,column=1)

frice=Label(f1,font=('arial',16,'bold'),text='LargeFrice',bd=16,anchor='w')
frice.grid(row=1,column=0)
frice1=Entry(f1,font=('arial',16,'bold'),textvariable=fric,bd=16,insertwidth=4,bg='powder blue',justify='right')
frice1.grid(row=1,column=1)

L1=Label(f1,font=('arial',16,'bold'),text='Burger',bd=16,anchor='w')
L1.grid(row=2,column=0)
E1=Entry(f1,font=('arial',16,'bold'),textvariable=Burg,bd=16,insertwidth=4,bg='powder blue',justify='right')
E1.grid(row=2,column=1)

L2=Label(f1,font=('arial',16,'bold'),text='Filler',bd=16,anchor='w')
L2.grid(row=3,column=0)
E2=Entry(f1,font=('arial',16,'bold'),textvariable=Filet,bd=16,insertwidth=4,bg='powder blue',justify='right')
E2.grid(row=3,column=1)

L3=Label(f1,font=('arial',16,'bold'),text='Drinks',bd=16,anchor='w')
L3.grid(row=4,column=0)
E3=Entry(f1,font=('arial',16,'bold'),textvariable=Drinks,bd=16,insertwidth=4,bg='powder blue',justify='right')
E3.grid(row=4,column=1)


L4=Label(f1,font=('arial',16,'bold'),text='Chiken Burger',bd=16,anchor='w')
L4.grid(row=5,column=0)
E4=Entry(f1,font=('arial',16,'bold'),textvariable=chiken_burger,bd=16,insertwidth=4,bg='powder blue',justify='right')
E4.grid(row=5,column=1)

L5=Label(f1,font=('arial',16,'bold'),text='Cheese Burger',bd=16,anchor='w')
L5.grid(row=6,column=0)
E5=Entry(f1,font=('arial',16,'bold'),textvariable=cheese_burger,bd=16,insertwidth=4,bg='powder blue',justify='right')
E5.grid(row=6,column=1)

L0=Label(f1,font=('arial',16,'bold'),text='Dosha',bd=16,anchor='w')
L0.grid(row=0,column=3)
E0=Entry(f1,font=('arial',16,'bold'),textvariable=Dos,bd=16,insertwidth=4,bg='powder blue',justify='right')
E0.grid(row=0,column=4)

L6=Label(f1,font=('arial',16,'bold'),text='State Tax',bd=16,anchor='w')
L6.grid(row=1,column=3)
E6=Entry(f1,font=('arial',16,'bold'),textvariable=Tax,bd=16,insertwidth=4,bg='powder blue',justify='right')
E6.grid(row=1,column=4)

L7=Label(f1,font=('arial',16,'bold'),text='Service Charge',bd=16,anchor='w')
L7.grid(row=2,column=3)
E7=Entry(f1,font=('arial',16,'bold'),textvariable=service_chrage,bd=16,insertwidth=4,bg='powder blue',justify='right')
E7.grid(row=2,column=4)

L8=Label(f1,font=('arial',16,'bold'),text='Total Cost',bd=16,anchor='w')
L8.grid(row=3,column=3)
E8=Entry(f1,font=('arial',16,'bold'),textvariable=Cost,bd=16,insertwidth=4,bg='powder blue',justify='right')
E8.grid(row=3,column=4)

#Button for commond
def Rand():
    x=random.randint(2000,100099)
    rando=str(x)
    rand.set(rando)

def add():
    k=int(E6.get())+int(E7.get())+ int(E0.get())+int(E5.get())+int(E4.get())+int(E3.get())+int(E2.get())+int(E1.get())+int(frice1.get())
    Cost.set(str(k))
def Exit():
    win.destroy()
def Clear():
    rand.set('')
    fric.set('0')
    Burg.set('0')
    Filet.set('0')
    Drinks.set('0')
    Cost.set('')
    chiken_burger.set('0')
    cheese_burger.set('0')
    Dos.set('0')
    
    


#Button

B1=Button(f1,padx=16,pady=8,bd=20,fg='Black',text='Total',bg='Powder Blue',command=add).grid(row=4,column=3)
B2=Button(f1,padx=16,pady=8,bd=20,fg='Black',text='Reference Number',bg='Powder Blue',command=Rand).grid(row=4,column=4)
B3=Button(f1,padx=16,pady=8,bd=20,fg='Black',text='Clear',bg='Powder Blue',command=Clear).grid(row=6,column=3)
B4=Button(f1,padx=16,pady=8,bd=20,fg='Black',text='Exit',bg='Powder Blue',command=Exit).grid(row=6,column=4)








win.mainloop()
