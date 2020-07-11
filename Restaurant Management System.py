from tkinter import *
import random
import time
import tkinter.messagebox

win=Tk()
win.geometry('1350x750+0+0')
win.title('Advance Restaurant Mangement System')
win.configure(bg='Cadet Blue')

######Frame work#######
tops=Frame(win,bg='Cadet Blue',bd=20,pady=5,relief=RIDGE)
tops.pack(side=TOP)
L1=Label(tops,bg='Cadet Blue',text='Reastaurant Managment System',font=('arial',60,'bold'),fg='Red',justify=CENTER).grid(row=0,column=0)

menu_frame=Frame(win,bg='Cadet Blue',bd=10,relief=RIDGE)
menu_frame.pack(side=LEFT)

main_reciept_frame=Frame(win,bg='Powder Blue',bd=10,relief=RIDGE)
main_reciept_frame.pack(side=RIGHT)

button_frame=Frame(main_reciept_frame,bg='Powder Blue',bd=2,relief=RIDGE)
button_frame.pack(side=BOTTOM)

#####now work in recipt frame
calculator_frame=Frame(main_reciept_frame,bg='White',bd=6,relief=RIDGE)
calculator_frame.pack(side=TOP)

reciept_frame=Frame(main_reciept_frame,bg='Powder Blue',bd=4,relief=RIDGE)
reciept_frame.pack(side=BOTTOM)

#####now work in Menu frame
Cost_frame=Frame(menu_frame,bg='Powder Blue',bd=4,relief=RIDGE)
Cost_frame.pack(side=BOTTOM)

drinks_frame=Frame(menu_frame,bg='Powder Blue',bd=10,relief=RIDGE)
drinks_frame.pack(side=LEFT)

cake_frame=Frame(menu_frame,bg='Powder Blue',bd=10,relief=RIDGE)
cake_frame.pack(side=RIGHT)

#*****************************variable
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=StringVar()
var18=StringVar()
var19=StringVar()
var20=StringVar()
var21=StringVar()
var22=StringVar()
var23=StringVar()
var24=StringVar()
var25=StringVar()
var26=StringVar()
var27=StringVar()
var28=StringVar()
var29=StringVar()
var30=StringVar()
var31=StringVar()
var32=StringVar()
var33=StringVar()
var34=StringVar()
var35=StringVar()
var36=StringVar()
var37=StringVar()
var38=StringVar()
var35.set('80')
var36.set('180')

var17.set('0')
var18.set('0')
var19.set('0')
var20.set('0')
var21.set('0')
var22.set('0')
var23.set('0')
var24.set('0')
var25.set('0')
var26.set('0')
var27.set('0')
var28.set('0')
var29.set('0')
var30.set('0')
var31.set('0')
var32.set('0')



text_input=StringVar()
operator=''

recieptref=StringVar()

Dateoforder=StringVar()
Dateoforder.set(time.strftime("%d/%m/%y"))

######Now link to check button to Entry box ********************************************

def chk1():
    if(var1.get()==1):
        E1.configure(state=NORMAL)
        E1.focus()
        E1.delete('0',END)
        var17.set('0')
    elif(var1.get()==0):
        E1.configure(state=DISABLED)
        var17.set('0')
def chk2():
    if(var2.get()==1):
        E2.configure(state=NORMAL)
        E2.focus()
        E2.delete('0',END)
        var18.set('0')
    elif(var2.get()==0):
        E2.configure(state=DISABLED)
        var18.set('0')
def chk3():
    if(var3.get()==1):
        E3.configure(state=NORMAL)
        E3.focus()
        E3.delete('0',END)
        var19.set('0')
    elif(var3.get()==0):
        E3.configure(state=DISABLED)
        var19.set('0')
def chk4():
    if(var4.get()==1):
        E4.configure(state=NORMAL)
        E4.focus()
        E4.delete('0',END)
        var20.set('0')
    elif(var4.get()==0):
        E4.configure(state=DISABLED)
        var20.set('0')
def chk5():
    if(var5.get()==1):
        E5.configure(state=NORMAL)
        E5.focus()
        E5.delete('0',END)
        var21.set('0')
    elif(var5.get()==0):
        E5.configure(state=DISABLED)
        var21.set('0')
def chk6():
    if(var6.get()==1):
        E6.configure(state=NORMAL)
        E6.focus()
        E6.delete('0',END)
        var22.set('0')
    elif(var6.get()==0):
        E6.configure(state=DISABLED)
        var22.set('0')

def chk7():
    if(var7.get()==1):
        E7.configure(state=NORMAL)
        E7.focus()
        E7.delete('0',END)
        var23.set('0')
    elif(var7.get()==0):
        E7.configure(state=DISABLED)
        var23.set('0')
def chk8():
    if(var8.get()==1):
        E8.configure(state=NORMAL)
        E8.focus()
        E8.delete('0',END)
        var24.set('0')
    elif(var8.get()==0):
        E8.configure(state=DISABLED)
        var24.set('0')
def chk9():
    if(var9.get()==1):
        E9.configure(state=NORMAL)
        E9.focus()
        E9.delete('0',END)
        var25.set('0')
    elif(var9.get()==0):
        E9.configure(state=DISABLED)
        var25.set('0')
def chk10():
    if(var10.get()==1):
        E10.configure(state=NORMAL)
        E10.focus()
        E10.delete('0',END)
        var26.set('0')
    elif(var10.get()==0):
        E10.configure(state=DISABLED)
        var26.set('0')
def chk11():
    if(var11.get()==1):
        E11.configure(state=NORMAL)
        E11.focus()
        E11.delete('0',END)
        var27.set('0')
    elif(var11.get()==0):
        E11.configure(state=DISABLED)
        var27.set('0')

def chk12():
    if(var12.get()==1):
        E12.configure(state=NORMAL)
        E12.focus()
        E12.delete('0',END)
        var28.set('0')
    elif(var12.get()==0):
        E12.configure(state=DISABLED)
        var28.set('0')
def chk13():
    if(var13.get()==1):
        E13.configure(state=NORMAL)
        E13.focus()
        E13.delete('0',END)
        var29.set('0')
    elif(var13.get()==0):
        E13.configure(state=DISABLED)
        var29.set('0')
def chk14():
    if(var14.get()==1):
        E14.configure(state=NORMAL)
        E14.focus()
        E14.delete('0',END)
        var30.set('0')
    elif(var14.get()==0):
        E14.configure(state=DISABLED)
        var30.set('0')
def chk15():
    if(var15.get()==1):
        E15.configure(state=NORMAL)
        E15.focus()
        E15.delete('0',END)
        var31.set('0')
    elif(var15.get()==0):
        E15.configure(state=DISABLED)
        var31.set('0')
def chk16():
   if(var16.get()==1):
        E16.configure(state=NORMAL)
        E16.focus()
        E16.delete('0',END)
        var32.set('0')
   elif(var16.get()==0):
        E16.configure(state=DISABLED)
        var32.set('0')







        
#####################This is for drink checkbuttonks frame (now working on menuframe as drinks and cake)

        
d1=Checkbutton(drinks_frame,text='COLD COFFEE',variable=var1,onvalue=1,offvalue=0,
               font=('arial',18,'bold'),bg='Powder Blue',command=chk1).grid(row=0,sticky=W)
d2=Checkbutton(drinks_frame,text='HOT COFFEE',variable=var2,onvalue=1,offvalue=0,
               font=('arial',18,'bold'),bg='Powder Blue',command=chk2).grid(row=1,sticky=W)
d3=Checkbutton(drinks_frame,text='CHOCHLATE COFFEE',variable=var3,onvalue=1,offvalue=0,
               font=('arial',18,'bold'),bg='Powder Blue',command=chk3).grid(row=2,sticky=W)
d4=Checkbutton(drinks_frame,text='TEA',variable=var4,onvalue=1,offvalue=0,
               font=('arial',18,'bold'),bg='Powder Blue',command=chk4).grid(row=3,sticky=W)
d5=Checkbutton(drinks_frame,text='GINGER TEA',variable=var5,onvalue=1,offvalue=0,
               font=('arial',18,'bold'),bg='Powder Blue',command=chk5).grid(row=4,sticky=W)
d6=Checkbutton(drinks_frame,text='MASALA TEA',variable=var6,onvalue=1,offvalue=0,
               font=('arial',18,'bold'),bg='Powder Blue',command=chk6).grid(row=5,sticky=W)
d7=Checkbutton(drinks_frame,text='COLD DRINKS',variable=var7,onvalue=1,offvalue=0,
               font=('arial',18,'bold'),bg='Powder Blue',command=chk7).grid(row=6,sticky=W)
d8=Checkbutton(drinks_frame,text='JUICE',variable=var8,onvalue=1,offvalue=0,
               font=('arial',18,'bold'),bg='Powder Blue',command=chk8).grid(row=7,sticky=W)

#####This is for cAKE frame

c1=Checkbutton(cake_frame,text='Birthday Cake',variable=var9,onvalue=1,offvalue=0,
               font=('arial',18,'bold'),bg='Powder Blue',command=chk9).grid(row=0,sticky=W)
c2=Checkbutton(cake_frame,text='Marriage Cake',variable=var10,onvalue=1,offvalue=0,
               font=('arial',18,'bold'),bg='Powder Blue',command=chk10).grid(row=1,sticky=W)
c3=Checkbutton(cake_frame,text='Friednship Cake',variable=var11,onvalue=1,offvalue=0,
               font=('arial',18,'bold'),bg='Powder Blue',command=chk11).grid(row=2,sticky=W)
c4=Checkbutton(cake_frame,text='Anversery Cake',variable=var12,onvalue=1,offvalue=0,
               font=('arial',18,'bold'),bg='Powder Blue',command=chk12).grid(row=3,sticky=W)
c5=Checkbutton(cake_frame,text='School Cake',variable=var13,onvalue=1,offvalue=0,
               font=('arial',18,'bold'),bg='Powder Blue',command=chk13).grid(row=4,sticky=W)
c6=Checkbutton(cake_frame,text='Opening Cake',variable=var14,onvalue=1,offvalue=0,
               font=('arial',18,'bold'),bg='Powder Blue',command=chk14).grid(row=5,sticky=W)
c7=Checkbutton(cake_frame,text='Cristmas Cake',variable=var15,onvalue=1,offvalue=0,
               font=('arial',18,'bold'),bg='Powder Blue',command=chk15).grid(row=6,sticky=W)
c8=Checkbutton(cake_frame,text='Death Cake',variable=var16,onvalue=1,offvalue=0,
               font=('arial',18,'bold'),bg='Powder Blue',command=chk16).grid(row=7,sticky=W)

#####Entry box for drinks

E1=Entry(drinks_frame,font=('arial',18,'bold'),bd=8,width=6,justify=LEFT,textvariable=var17,state=DISABLED)
E1.grid(row=0,column=1)
E2=Entry(drinks_frame,font=('arial',18,'bold'),bd=8,width=6,justify=LEFT,textvariable=var18,state=DISABLED)
E2.grid(row=1,column=1)
E3=Entry(drinks_frame,font=('arial',18,'bold'),bd=8,width=6,justify=LEFT,textvariable=var19,state=DISABLED)
E3.grid(row=2,column=1)
E4=Entry(drinks_frame,font=('arial',18,'bold'),bd=8,width=6,justify=LEFT,textvariable=var20,state=DISABLED)
E4.grid(row=3,column=1)
E5=Entry(drinks_frame,font=('arial',18,'bold'),bd=8,width=6,justify=LEFT,textvariable=var21,state=DISABLED)
E5.grid(row=4,column=1)
E6=Entry(drinks_frame,font=('arial',18,'bold'),bd=8,width=6,justify=LEFT,textvariable=var22,state=DISABLED)
E6.grid(row=5,column=1)
E7=Entry(drinks_frame,font=('arial',18,'bold'),bd=8,width=6,justify=LEFT,textvariable=var23,state=DISABLED)
E7.grid(row=6,column=1)
E8=Entry(drinks_frame,font=('arial',18,'bold'),bd=8,width=6,justify=LEFT,textvariable=var24,state=DISABLED)
E8.grid(row=7,column=1)

#######Entry box for Cakes

E9=Entry(cake_frame,font=('arial',18,'bold'),bd=8,width=6,justify=LEFT,textvariable=var25,state=DISABLED)
E9.grid(row=0,column=1)
E10=Entry(cake_frame,font=('arial',18,'bold'),bd=8,width=6,justify=LEFT,textvariable=var26,state=DISABLED)
E10.grid(row=1,column=1)
E11=Entry(cake_frame,font=('arial',18,'bold'),bd=8,width=6,justify=LEFT,textvariable=var27,state=DISABLED)
E11.grid(row=2,column=1)
E12=Entry(cake_frame,font=('arial',18,'bold'),bd=8,width=6,justify=LEFT,textvariable=var28,state=DISABLED)
E12.grid(row=3,column=1)
E13=Entry(cake_frame,font=('arial',18,'bold'),bd=8,width=6,justify=LEFT,textvariable=var29,state=DISABLED)
E13.grid(row=4,column=1)
E14=Entry(cake_frame,font=('arial',18,'bold'),bd=8,width=6,justify=LEFT,textvariable=var30,state=DISABLED)
E14.grid(row=5,column=1)
E15=Entry(cake_frame,font=('arial',18,'bold'),bd=8,width=6,justify=LEFT,textvariable=var31,state=DISABLED)
E15.grid(row=6,column=1)
E16=Entry(cake_frame,font=('arial',18,'bold'),bd=8,width=6,justify=LEFT,textvariable=var32,state=DISABLED)
E16.grid(row=7,column=1)


##########Now use of cost frame#########
L3=Label(Cost_frame,font=('arial',14,'bold'),text='Cost Of Drinks',bg='Powder Blue',fg='Black').grid(row=0,column=0,sticky=W)
E17=Entry(Cost_frame,font=('arial',14,'bold'),bg='White',insertwidth=2,justify=RIGHT,textvariable=var33)
E17.grid(row=0,column=1)

L4=Label(Cost_frame,font=('arial',14,'bold'),text='Cost Of Cakes',bg='Powder Blue',fg='Black').grid(row=1,column=0,sticky=W)
E18=Entry(Cost_frame,font=('arial',14,'bold'),bg='White',insertwidth=2,justify=RIGHT,textvariable=var34)
E18.grid(row=1,column=1)

L4=Label(Cost_frame,font=('arial',14,'bold'),text='Service Charges',bg='Powder Blue',fg='Black').grid(row=2,column=0,sticky=W)
E19=Entry(Cost_frame,font=('arial',14,'bold'),bg='White',insertwidth=2,justify=RIGHT,textvariable=var35)
E19.grid(row=2,column=1)

L5=Label(Cost_frame,font=('arial',14,'bold'),text='Paid Tax',bg='Powder Blue',fg='Black').grid(row=0,column=2)
E20=Entry(Cost_frame,font=('arial',14,'bold'),bg='White',insertwidth=2,justify=RIGHT,textvariable=var36)
E20.grid(row=0,column=3)

L6=Label(Cost_frame,font=('arial',14,'bold'),text='Sub Total',bg='Powder Blue',fg='Black').grid(row=1,column=2)
E21=Entry(Cost_frame,font=('arial',14,'bold'),bg='White',insertwidth=2,justify=RIGHT,textvariable=var37)
E21.grid(row=1,column=3)

L7=Label(Cost_frame,font=('arial',14,'bold'),text='Total Cost',bg='Powder Blue',fg='Black').grid(row=2,column=2)
E22=Entry(Cost_frame,font=('arial',14,'bold'),bg='White',insertwidth=2,justify=RIGHT,textvariable=var38)
E22.grid(row=2,column=3)




#####Creation of text box under calculator for reciept_frame**************

txt_reciept=Text(reciept_frame,width=46,height=12,bg='White',bd=4,font=('arial',12,'bold'))

txt_reciept.grid(row=0,column=0)


##########============================fuction to give command to button************

def Exit():
    Exit=tkinter.messagebox.askyesnocancel('Exit From System','Confirm if you want Exit')
    if Exit>0:
        win.destroy()
        return

def reset():
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var33.set('')
    var34.set('')
    var37.set('')
    var38.set('')
    txt_reciept.delete('1.0',END)
    var17.set('0')
    var18.set('0')
    var19.set('0')
    var20.set('0')
    var21.set('0')
    var22.set('0')
    var23.set('0')
    var24.set('0')
    var25.set('0')
    var26.set('0')
    var27.set('0')
    var28.set('0')
    var29.set('0')
    var30.set('0')
    var31.set('0')
    var32.set('0')
    E1.configure(state=DISABLED)
    E2.configure(state=DISABLED)
    E3.configure(state=DISABLED)
    E4.configure(state=DISABLED)
    E5.configure(state=DISABLED)
    E6.configure(state=DISABLED)
    E7.configure(state=DISABLED)
    E8.configure(state=DISABLED)
    E9.configure(state=DISABLED)
    E10.configure(state=DISABLED)
    E11.configure(state=DISABLED)
    E12.configure(state=DISABLED)
    E13.configure(state=DISABLED)
    E14.configure(state=DISABLED)
    E15.configure(state=DISABLED)
    E16.configure(state=DISABLED)

def total():
    k=(int(E1.get())+ int(E2.get())+int(E3.get())+int(E4.get())+int(E5.get())+int(E6.get())+int(E7.get())+int(E8.get()))
    L=(int(E9.get())+ int(E10.get())+int(E11.get())+int(E12.get())+int(E13.get())+int(E14.get())+int(E15.get())+int(E16.get()))
    var33.set(k)
    var34.set(L)
    j=int(E17.get())+int(E18.get())
    var37.set(j)
    i=int(E20.get())+int(E21.get())+int(E19.get())
    var38.set(i)

def reciept():
    txt_reciept.delete('1.0',END)
    x=random.randint(5000,22222)
    randomref=str(x)
    recieptref.set('Bill'+randomref)
    txt_reciept.insert(END,'Reciept Ref :\t\t\t'+recieptref.get()+'\t'+Dateoforder.get()+'\n')
    txt_reciept.insert(END,'Item :\t\t\t'+'Item List\n')
    txt_reciept.insert(END,'COLD COFFEE :\t\t\t'+E1.get()+'\n')
    txt_reciept.insert(END,'HOT COFFEE :\t\t\t'+E2.get()+'\n')
    txt_reciept.insert(END,'CHOCHLATE COFFEE :\t\t\t'+E3.get()+'\n')
    txt_reciept.insert(END,'TEA :\t\t\t'+E4.get()+'\n')
    txt_reciept.insert(END,'GINGER TEA :\t\t\t'+E5.get()+'\n')
    txt_reciept.insert(END,'MASALA TEA :\t\t\t'+E6.get()+'\n')
    txt_reciept.insert(END,'Cold Drinks :\t\t\t'+E7.get()+'\n')
    txt_reciept.insert(END,'JUICE :\t\t\t'+E8.get()+'\n')
    txt_reciept.insert(END,'Birthday Cake :\t\t\t'+E9.get()+'\n')
    txt_reciept.insert(END,'Marriage Cake:\t\t\t'+E10.get()+'\n')
    txt_reciept.insert(END,'Friednship Cake :\t\t\t'+E11.get()+'\n')
    txt_reciept.insert(END,'Anversery Cake :\t\t\t'+E12.get()+'\n')
    txt_reciept.insert(END,'School Cake :\t\t\t'+E13.get()+'\n')
    txt_reciept.insert(END,'Opening Cake :\t\t\t'+E14.get()+'\n')
    txt_reciept.insert(END,'Cristmas Cake :\t\t\t'+E15.get()+'\n')
    txt_reciept.insert(END,'Death Cake :\t\t\t'+E16.get()+'\n')
    txt_reciept.insert(END,'Cost of Drinks :\t\t\t'+E17.get()+'\n')
    txt_reciept.insert(END,'Cost of Cakes :\t\t\t'+E18.get()+'\n')
    txt_reciept.insert(END,'Sub Total :\t\t\t'+E21.get()+'\n')
    txt_reciept.insert(END,'Total Cost :\t\t\t'+E22.get()+'\n')



        

############Button in buttonframe***********************************

b1=Button(button_frame,padx=16,pady=1,bd=5,fg='Green',font=('arial',16,'bold'),
          width=4,text='Total',bg='Powder Blue',command=total).grid(row=0,column=0)
b2=Button(button_frame,padx=16,pady=1,bd=5,fg='Green',font=('arial',16,'bold'),
          width=4,text='Reset',bg='Powder Blue',command=reset).grid(row=0,column=1)
b3=Button(button_frame,padx=16,pady=1,bd=5,fg='Green',font=('arial',16,'bold'),
          width=4,text='Exit',bg='Powder Blue',command=Exit).grid(row=0,column=2)

b4=Button(button_frame,padx=16,pady=1,bd=5,fg='Green',font=('arial',16,'bold'),
          width=4,text='Recipt',bg='Powder Blue',command=reciept).grid(row=0,column=3)

#***************************calculator working********************************************

def btnclick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)
    
def clear():
    global operator
    oprtator=''
    text_input.set(operator)
    
def eql():
    global operator
    sump=str(eval(operator))
    text_input.set(sump)
    operator=''
    
    



######calculator display##################################################

cdisplay=Entry(calculator_frame,width=45,bg='White',font=('arial',12,'bold'),justify=RIGHT,textvariable=text_input)
cdisplay.grid(row=0,column=0,columnspan=4,pady=1)
cdisplay.insert(0,"0")

######calculator Buttons#######################################################
B1=Button(calculator_frame,padx=16,pady=7,fg='Black',font=('arial',16,'bold'),width=4,text='7',command=lambda:btnclick(7)).grid(row=2,column=0)

B2=Button(calculator_frame,padx=16,pady=7,fg='Black',font=('arial',16,'bold'),width=4,text='8',command=lambda:btnclick(8)).grid(row=2,column=1)

B3=Button(calculator_frame,padx=16,pady=7,fg='Black',font=('arial',16,'bold'),width=4,text='9',command=lambda:btnclick(9)).grid(row=2,column=2)

B4=Button(calculator_frame,padx=16,pady=7,fg='Black',font=('arial',16,'bold'),width=4,text='+',command=lambda:btnclick('+')).grid(row=2,column=3)

B5=Button(calculator_frame,padx=16,pady=7,fg='Black',font=('arial',16,'bold'),width=4,text='4',command=lambda:btnclick(4)).grid(row=3,column=0)

B6=Button(calculator_frame,padx=16,pady=7,fg='Black',font=('arial',16,'bold'),width=4,text='5',command=lambda:btnclick(5)).grid(row=3,column=1)

B7=Button(calculator_frame,padx=16,pady=7,fg='Black',font=('arial',16,'bold'),width=4,text='6',command=lambda:btnclick(6)).grid(row=3,column=2)

B8=Button(calculator_frame,padx=16,pady=7,fg='Black',font=('arial',16,'bold'),width=4,text='-',command=lambda:btnclick('-')).grid(row=3,column=3)

B9=Button(calculator_frame,padx=16,pady=7,fg='Black',font=('arial',16,'bold'),width=4,text='3',command=lambda:btnclick(3)).grid(row=4,column=0)

B10=Button(calculator_frame,padx=16,pady=7,fg='Black',font=('arial',16,'bold'),width=4,text='2',command=lambda:btnclick(2)).grid(row=4,column=1)

B11=Button(calculator_frame,padx=16,pady=7,fg='Black',font=('arial',16,'bold'),width=4,text='1',command=lambda:btnclick(1)).grid(row=4,column=2)

B12=Button(calculator_frame,padx=16,pady=7,fg='Black',font=('arial',16,'bold'),width=4,text='/',command=lambda:btnclick('/')).grid(row=4,column=3)

B13=Button(calculator_frame,padx=16,pady=7,fg='Black',font=('arial',16,'bold'),width=4,text='0',command=lambda:btnclick(0)).grid(row=5,column=0)

B14=Button(calculator_frame,padx=16,pady=7,fg='Black',font=('arial',16,'bold'),width=4,text='*',command=lambda:btnclick('*')).grid(row=5,column=1)

B15=Button(calculator_frame,padx=16,pady=7,fg='Black',font=('arial',16,'bold'),width=4,text='=',command=eql).grid(row=5,column=2)

B16=Button(calculator_frame,padx=16,pady=7,fg='Black',font=('arial',16,'bold'),width=4,text='C',command=clear).grid(row=5,column=3)


win.mainloop()
                                                                    
