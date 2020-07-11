from tkinter import Tk,StringVar,ttk,messagebox
from tkinter import *
import time,datetime
root=Tk()
root.title('Attendence Sheet')
root.geometry('1350x650+0+0')
root.configure(background='black')

#************************Frame dividation *************************************
first_frame=Frame(root,width='1350',height='650',bd=8,relief='raise')
first_frame.pack(side=LEFT)
Second_frame=Frame(root,width='1350',height='650',bd=8,relief='raise')
Second_frame.pack(side=RIGHT)

#**************************divide of first frame **********************
frame1=Frame(first_frame,width='1000',height='100',bd=8,relief='raise')
frame1.pack(side=TOP)
frame2=Frame(first_frame,width='1000',height='550',bd=8,relief='raise')
frame2.pack(side=TOP)

#*********************************second_frame ***********************
frame3=Frame(Second_frame,width=350,height=215,relief='raise',bd=8)
frame3.pack(side=TOP)
frame4=Frame(Second_frame,width=350,height=415,relief='raise',bd=8)
frame4.pack(side=TOP)

#*********************variable ***************************
Dateoforder=StringVar()
value0=StringVar()
value1=StringVar()
value2=StringVar()
value3=StringVar()
value4=StringVar()
value5=StringVar()
value6=StringVar()
value7=StringVar()
value8=StringVar()
value9=StringVar()
value10=StringVar()
value11=StringVar()
value12=StringVar()

#***************************componet*********************************

Dateoforder.set(time.strftime('%d/%m/%Y'))

#8=*****************************command********************************
def qexit():
    a=messagebox.askyesno("Exit From System","Do You Want To Exit?")
    if a>0:
        root.destroy()
    return

def Rset():
    value0.set('')
    value1.set('')
    value2.set('')
    value3.set('')
    value4.set('')
    value5.set('')
    value6.set('')
    value7.set('')
    value8.set('')
    value9.set('')
    value10.set('')
    value11.set('')
    value12.set('')

def fil():
    if(value0.get()==' '):
        value1.set(' ')
        value2.set(' ')
        value3.set(' ')
        value4.set(' ')
        value5.set(' ')
        value6.set(' ')
        value7.set(' ')
        value8.set(' ')
        value9.set(' ')
        value10.set(' ')
        value11.set(' ')
        value12.set(' ')
    elif (value0.get()=='L'):
        value1.set('L')
        value2.set('L')
        value3.set('L')
        value4.set('L')
        value5.set('L')
        value6.set('L')
        value7.set('L')
        value8.set('L')
        value9.set('L')
        value10.set('L')
        value11.set('L')
        value12.set('L')
    elif (value0.get()=='/'):
        value1.set('/')
        value2.set('/')
        value3.set('/')
        value4.set('/')
        value5.set('/')
        value6.set('/')
        value7.set('/')
        value8.set('/')
        value9.set('/')
        value10.set('/')
        value11.set('/')
        value12.set('/')

    elif (value0.get()=='A'):
        value1.set('A')
        value2.set('A')
        value3.set('A')
        value4.set('A')
        value5.set('A')
        value6.set('A')
        value7.set('A')
        value8.set('A')
        value9.set('A')
        value10.set('A')
        value11.set('A')
        value12.set('A')
    elif (value0.get()=='O'):
        value1.set('O')
        value2.set('O')
        value3.set('O')
        value4.set('O')
        value5.set('O')
        value6.set('O')
        value7.set('O')
        value8.set('O')
        value9.set('O')
        value10.set('O')
        value11.set('O')
        value12.set('O')
    elif (value0.get()=='S'):
        value1.set('S')
        value2.set('S')
        value3.set('S')
        value4.set('S')
        value5.set('S')
        value6.set('S')
        value7.set('S')
        value8.set('S')
        value9.set('S')
        value10.set('S')
        value11.set('S')
        value12.set('S')
        
#********************************************************Images********************************************************

a=Canvas(frame4,width=350,height=415,bg='black')
a.grid(row=0,column=0)
b=PhotoImage(file='school.png')
a.create_image(200,200,image=b)

f=Canvas(frame3,width=300,height=215)
f.grid(row=0,column=0)
d=PhotoImage(file='Pic1.png')
e=f.create_image(150,150,image=d)

x=PhotoImage(file='pic3.png')

def pic1():
    e=f.create_image(150,150,image=x)

g=PhotoImage(file='pic2.png')
def pic2():
    e=f.create_image(150,150,image=g)

h=PhotoImage(file='pic3.png')
def pic3():
    e=f.create_image(150,150,image=h)
i=PhotoImage(file='pic4.png')
def pic4():
    e=f.create_image(150,150,image=i)
j=PhotoImage(file='pic5.png')
def pic5():
    e=f.create_image(150,152,image=j)
k=PhotoImage(file='pic7.png')
def pic6():
    e=f.create_image(150,150,image=k)
    
l=PhotoImage(file='pic6.png')
def pic7():
    e=f.create_image(150,150,image=l)
    
m=PhotoImage(file='pic8.png')
def pic8():
    e=f.create_image(150,150,image=m)
    
n=PhotoImage(file='pic9.png')
def pic9():
    e=f.create_image(150,150,image=n)




        
#***************************first frmae (freame1)*********************************
L1=Label(frame1,font=('arial',10,'bold'),text='No.',bd=16)
L1.grid(row=0,column=0,sticky=W)
L2=Label(frame1,font=('arial',10,'bold'),text='Student No.' , bd=16,width=18)
L2.grid(row=0,column=1,sticky=W)
L3=Label(frame1,font=('arial',10,'bold'),text='Student Name' , bd=16,width=18)
L3.grid(row=0,column=2,sticky=W)
L4=Label(frame1,font=('arial',10,'bold'),text='Course Code' , bd=16,width=18,)
L4.grid(row=0,column=3,sticky=W)

box=ttk.Combobox(frame1,textvariable=value0,state='readonly')
box['value']=(' ','L','/','O','A','S')
box.current(0)
box.grid(row=0,column=4)

B1=Button(frame1,text='Fill',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1,command=fil).grid(row=0,column=5)
B2=Button(frame1,text='Reset',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1,command=Rset).grid(row=0,column=6)
B3=Button(frame1,text='Exit',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1,command=qexit).grid(row=0,column=7)

L5=Label(frame1,font=('arial',10,'bold'),textvariable=Dateoforder,bd=16)
L5.grid(row=0,column=8,sticky=W)

#***************************first frmae (freame2) row1*********************************
L6=Label(frame2,font=('arail',10,'bold'),text='1',bd=16)
L6.grid(row=0,column=0,sticky=W)

L7=Label(frame2,font=('arail',10,'bold'),text='1232',padx=2,pady=2,width=18,fg='black',bd=16)
L7.grid(row=0,column=1,sticky=W)
L8=Label(frame2,font=('arail',10,'bold'),text='Fehmi Wales',padx=2,pady=2,width=18,fg='black',bd=16)
L8.grid(row=0,column=2,sticky=W)
L9=Label(frame2,font=('arail',10,'bold'),text='10005',padx=2,pady=2,width=18,fg='black',bd=16)
L9.grid(row=0,column=3,sticky=W)

box=ttk.Combobox(frame2,textvariable=value1,state='readonly')
box['value']=(' ','L','/','O','A','S')
box.current(0)
box.grid(row=0,column=4)

B4=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1 ,command=pic1).grid(row=0,column=5)
B5=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=0,column=6)
B6=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=0,column=7)
B7=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=0,column=8)

#***************************first frmae (freame2) row2*********************************
L10=Label(frame2,font=('arail',10,'bold'),text='3',bd=16)
L10.grid(row=1,column=0,sticky=W)

L11=Label(frame2,font=('arail',10,'bold'),text='1234',padx=2,pady=2,width=18,fg='black',bd=16)
L11.grid(row=1,column=1,sticky=W)
L12=Label(frame2,font=('arail',10,'bold'),text='Andy Wales',padx=2,pady=2,width=18,fg='black',bd=16)
L12.grid(row=1,column=2,sticky=W)
L13=Label(frame2,font=('arail',10,'bold'),text='10007',padx=2,pady=2,width=18,fg='black',bd=16)
L13.grid(row=1,column=3,sticky=W)

box=ttk.Combobox(frame2,textvariable=value2,state='readonly')
box['value']=(' ','L','/','O','A','S')
box.current(0)
box.grid(row=1,column=4)

B8=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1,command=pic2).grid(row=1,column=5)
B9=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=1,column=6)
B10=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=1,column=7)
B11=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=1,column=8)

#***************************first frmae (freame2) row3*********************************
L10=Label(frame2,font=('arail',10,'bold'),text='4',bd=16)
L10.grid(row=2,column=0,sticky=W)

L11=Label(frame2,font=('arail',10,'bold'),text='1235',padx=2,pady=2,width=18,fg='black',bd=16)
L11.grid(row=2,column=1,sticky=W)
L12=Label(frame2,font=('arail',10,'bold'),text='Sheldon Wales',padx=2,pady=2,width=18,fg='black',bd=16)
L12.grid(row=2,column=2,sticky=W)
L13=Label(frame2,font=('arail',10,'bold'),text='10007',padx=2,pady=2,width=18,fg='black',bd=16)
L13.grid(row=2,column=3,sticky=W)

box=ttk.Combobox(frame2,textvariable=value3,state='readonly')
box['value']=(' ','L','/','O','A','S')
box.current(0)
box.grid(row=2,column=4)

B8=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1,command=pic3).grid(row=2,column=5)
B9=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=2,column=6)
B10=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=2,column=7)
B11=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=2,column=8)
#***************************first frmae (freame2) row4*********************************
L10=Label(frame2,font=('arail',10,'bold'),text='5',bd=16)
L10.grid(row=3,column=0,sticky=W)

L11=Label(frame2,font=('arail',10,'bold'),text='1235',padx=2,pady=2,width=18,fg='black',bd=16)
L11.grid(row=3,column=1,sticky=W)
L12=Label(frame2,font=('arail',10,'bold'),text='Deenu Wales',padx=2,pady=2,width=18,fg='black',bd=16)
L12.grid(row=3,column=2,sticky=W)
L13=Label(frame2,font=('arail',10,'bold'),text='10006',padx=2,pady=2,width=18,fg='black',bd=16)
L13.grid(row=3,column=3,sticky=W)

box=ttk.Combobox(frame2,textvariable=value4,state='readonly')
box['value']=(' ','L','/','O','A','S')
box.current(0)
box.grid(row=3,column=4)

B8=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1,command=pic4).grid(row=3,column=5)
B9=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=3,column=6)
B10=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=3,column=7)
B11=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=3,column=8)
#***************************first frmae (freame2) row5*********************************
L10=Label(frame2,font=('arail',10,'bold'),text='6',bd=16)
L10.grid(row=4,column=0,sticky=W)

L11=Label(frame2,font=('arail',10,'bold'),text='1236',padx=2,pady=2,width=18,fg='black',bd=16)
L11.grid(row=4,column=1,sticky=W)
L12=Label(frame2,font=('arail',10,'bold'),text='Mike ',padx=2,pady=2,width=18,fg='black',bd=16)
L12.grid(row=4,column=2,sticky=W)
L13=Label(frame2,font=('arail',10,'bold'),text='10006',padx=2,pady=2,width=18,fg='black',bd=16)
L13.grid(row=4,column=3,sticky=W)

box=ttk.Combobox(frame2,textvariable=value5,state='readonly')
box['value']=(' ','L','/''O','A','S')
box.current(0)
box.grid(row=4,column=4)

B8=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1,command=pic5).grid(row=4,column=5)
B9=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=4,column=6)
B10=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=4,column=7)
B11=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=4,column=8)
#***************************first frmae (freame2) row6*********************************
L10=Label(frame2,font=('arail',10,'bold'),text='7',bd=16)
L10.grid(row=5,column=0,sticky=W)

L11=Label(frame2,font=('arail',10,'bold'),text='1237',padx=2,pady=2,width=18,fg='black',bd=16)
L11.grid(row=5,column=1,sticky=W)
L12=Label(frame2,font=('arail',10,'bold'),text='Kiron Wales',padx=2,pady=2,width=18,fg='black',bd=16)
L12.grid(row=5,column=2,sticky=W)
L13=Label(frame2,font=('arail',10,'bold'),text='10006',padx=2,pady=2,width=18,fg='black',bd=16)
L13.grid(row=5,column=3,sticky=W)

box=ttk.Combobox(frame2,textvariable=value6,state='readonly')
box['value']=(' ','L','/''O','A','S')
box.current(0)
box.grid(row=5,column=4)

B8=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1,command=pic6).grid(row=5,column=5)
B9=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=5,column=6)
B10=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=5,column=7)
B11=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=5,column=8)
#***************************first frmae (freame2) row7*********************************
L10=Label(frame2,font=('arail',10,'bold'),text='8',bd=16)
L10.grid(row=6,column=0,sticky=W)

L11=Label(frame2,font=('arail',10,'bold'),text='1238',padx=2,pady=2,width=18,fg='black',bd=16)
L11.grid(row=6,column=1,sticky=W)
L12=Label(frame2,font=('arail',10,'bold'),text='Josheph Wales',padx=2,pady=2,width=18,fg='black',bd=16)
L12.grid(row=6,column=2,sticky=W)
L13=Label(frame2,font=('arail',10,'bold'),text='10006',padx=2,pady=2,width=18,fg='black',bd=16)
L13.grid(row=6,column=3,sticky=W)

box=ttk.Combobox(frame2,textvariable=value7,state='readonly')
box['value']=(' ','L','/''O','A','S')
box.current(0)
box.grid(row=6,column=4)

B8=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1,command=pic7).grid(row=6,column=5)
B9=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=6,column=6)
B10=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=6,column=7)
B11=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=6,column=8)
#***************************first frmae (freame2) row8*********************************
L10=Label(frame2,font=('arail',10,'bold'),text='9',bd=16)
L10.grid(row=7,column=0,sticky=W)

L11=Label(frame2,font=('arail',10,'bold'),text='1239',padx=2,pady=2,width=18,fg='black',bd=16)
L11.grid(row=7,column=1,sticky=W)
L12=Label(frame2,font=('arail',10,'bold'),text='Deen Wales',padx=2,pady=2,width=18,fg='black',bd=16)
L12.grid(row=7,column=2,sticky=W)
L13=Label(frame2,font=('arail',10,'bold'),text='10006',padx=2,pady=2,width=18,fg='black',bd=16)
L13.grid(row=7,column=3,sticky=W)

box=ttk.Combobox(frame2,textvariable=value8,state='readonly')
box['value']=(' ','/','O','A','S')
box.current(0)
box.grid(row=7,column=4)

B8=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1,command=pic8).grid(row=7,column=5)
B9=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=7,column=6)
B10=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=7,column=7)
B11=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=7,column=8)
#***************************first frmae (freame2) row9*********************************
L10=Label(frame2,font=('arail',10,'bold'),text='10',bd=16)
L10.grid(row=8,column=0,sticky=W)

L11=Label(frame2,font=('arail',10,'bold'),text='1240',padx=2,pady=2,width=18,fg='black',bd=16)
L11.grid(row=8,column=1,sticky=W)
L12=Label(frame2,font=('arail',10,'bold'),text='Kim Wales',padx=2,pady=2,width=18,fg='black',bd=16)
L12.grid(row=8,column=2,sticky=W)
L13=Label(frame2,font=('arail',10,'bold'),text='10006',padx=2,pady=2,width=18,fg='black',bd=16)
L13.grid(row=8,column=3,sticky=W)

box=ttk.Combobox(frame2,textvariable=value9,state='readonly')
box['value']=(' ','L','/''O','A','S')
box.current(0)
box.grid(row=8,column=4)

B8=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1,command=pic9).grid(row=8,column=5)
B9=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=8,column=6)
B10=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=8,column=7)
B11=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=8,column=8)
#***************************first frmae (freame2) row10*********************************
L10=Label(frame2,font=('arail',10,'bold'),text='11',bd=16)
L10.grid(row=9,column=0,sticky=W)

L11=Label(frame2,font=('arail',10,'bold'),text='1241',padx=2,pady=2,width=18,fg='black',bd=16)
L11.grid(row=9,column=1,sticky=W)
L12=Label(frame2,font=('arail',10,'bold'),text='Jack Wales',padx=2,pady=2,width=18,fg='black',bd=16)
L12.grid(row=9,column=2,sticky=W)
L13=Label(frame2,font=('arail',10,'bold'),text='10006',padx=2,pady=2,width=18,fg='black',bd=16)
L13.grid(row=9,column=3,sticky=W)

box=ttk.Combobox(frame2,textvariable=value10,state='readonly')
box['value']=(' ','L','/''O','A','S')
box.current(0)
box.grid(row=9,column=4)

B8=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=9,column=5)
B9=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=9,column=6)
B10=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=9,column=7)
B11=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=9,column=8)
#***************************first frmae (freame2) row11*********************************
L10=Label(frame2,font=('arail',10,'bold'),text='12',bd=16)
L10.grid(row=10,column=0,sticky=W)

L11=Label(frame2,font=('arail',10,'bold'),text='1242',padx=2,pady=2,width=18,fg='black',bd=16)
L11.grid(row=10,column=1,sticky=W)
L12=Label(frame2,font=('arail',10,'bold'),text='Sam Wales',padx=2,pady=2,width=18,fg='black',bd=16)
L12.grid(row=10,column=2,sticky=W)
L13=Label(frame2,font=('arail',10,'bold'),text='10006',padx=2,pady=2,width=18,fg='black',bd=16)
L13.grid(row=10,column=3,sticky=W)

box=ttk.Combobox(frame2,textvariable=value11,state='readonly')
box['value']=(' ','L','/''O','A','S')
box.current(0)
box.grid(row=10,column=4)

B8=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=10,column=5)
B9=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=10,column=6)
B10=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=10,column=7)
B11=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=10,column=8)
#***************************first frmae (freame2) row12*********************************
L10=Label(frame2,font=('arail',10,'bold'),text='13',bd=16)
L10.grid(row=11,column=0,sticky=W)

L11=Label(frame2,font=('arail',10,'bold'),text='1244',padx=2,pady=2,width=18,fg='black',bd=16)
L11.grid(row=11,column=1,sticky=W)
L12=Label(frame2,font=('arail',10,'bold'),text='Wox Wales',padx=2,pady=2,width=18,fg='black',bd=16)
L12.grid(row=11,column=2,sticky=W)
L13=Label(frame2,font=('arail',10,'bold'),text='10006',padx=2,pady=2,width=18,fg='black',bd=16)
L13.grid(row=11,column=3,sticky=W)

box=ttk.Combobox(frame2,textvariable=value12,state='readonly')
box['value']=(' ','L','/''O','A','S')
box.current(0)
box.grid(row=11,column=4)

B8=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=11,column=5)
B9=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=11,column=6)
B10=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=11,column=7)
B11=Button(frame2,text=' ',padx=2,pady=2,bd=2,fg='Black',font=('arial',10,'bold'),width=12,height=1).grid(row=11,column=8)

#************************************************************************************************************************






root.mainloop()
