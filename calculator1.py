from tkinter import *

enus = Tk()
enus.title('All In One Calculator')
enus.geometry('518x500')
enus.resizable(0,0)
enus.configure(background='#f2e30a')

exp = ''
vali=StringVar()

def  press(num):
    global exp
    exp = exp + str(num)
    equation.set(exp)

def equalpress():
    try:
        global exp
        total=str(eval(exp))
        equation.set(total)
        exp = ''
    except:
        equation.set('Give Correct Values')
        exp = ''

def clear():
    global exp
    exp = ''
    equation.set('')

equation = StringVar()

l=Label(enus,text='Enus This is your Calculator',font='chalkduster 25',bg='#f2e30a',fg='#07a2f5').grid(row=0,columnspan=4,padx=3,pady=30)
e=Entry(enus,width=30,textvariable=equation,font='chalkboard 28',justify=RIGHT,bg='light grey').grid(row=1,column=0,columnspan=4,padx=3,pady=20)

b0=Button(enus,text='0',padx=40,pady=15,font='chalkduster 10',fg='#d10d0d',command=lambda: press('0')).grid(row=6,column=0,padx=3,pady=3)
bdot=Button(enus,text='.',padx=40,pady=15,font='chalkduster 10',fg='#d10d0d',command=lambda: press('.')).grid(row=6,column=1,padx=3,pady=3)
bequal=Button(enus,text='=',padx=105,pady=15,font='chalkduster 10',fg='#d10d0d',command= equalpress).grid(row=6,column=2,columnspan=2,padx=3,pady=3)

b1=Button(enus,text='1',padx=40,pady=15,font='chalkduster 10',fg='#d10d0d',command=lambda: press('1')).grid(row=5,column=0,padx=3,pady=3)
b2=Button(enus,text='2',padx=40,pady=15,font='chalkduster 10',fg='#d10d0d',command=lambda: press('2')).grid(row=5,column=1,padx=3,pady=3)
b3=Button(enus,text='3',padx=40,pady=15,font='chalkduster 10',fg='#d10d0d',command=lambda: press('3')).grid(row=5,column=2,padx=3,pady=3)
badd=Button(enus,text='+',padx=40,pady=15,font='chalkduster 10',fg='#d10d0d',command=lambda: press('+')).grid(row=5,column=3,padx=3,pady=3)

b4=Button(enus,text='4',padx=40,pady=15,font='chalkduster 10',fg='#d10d0d',command=lambda: press('4')).grid(row=4,column=0,padx=3,pady=3)
b5=Button(enus,text='5',padx=40,pady=15,font='chalkduster 10',fg='#d10d0d',command=lambda: press('5')).grid(row=4,column=1,padx=3,pady=3)
b6=Button(enus,text='6',padx=40,pady=15,font='chalkduster 10',fg='#d10d0d',command=lambda: press('6')).grid(row=4,column=2,padx=3,pady=3)
bsub=Button(enus,text='-',padx=40,pady=15,font='chalkduster 10',fg='#d10d0d',command=lambda: press('-')).grid(row=4,column=3,padx=3,pady=3)

b7=Button(enus,text='7',padx=40,pady=15,font='chalkduster 10',fg='#d10d0d',command=lambda: press('7')).grid(row=3,column=0,padx=3,pady=3)
b8=Button(enus,text='8',padx=40,pady=15,font='chalkduster 10',fg='#d10d0d',command=lambda: press('8')).grid(row=3,column=1,padx=3,pady=3)
b9=Button(enus,text='9',padx=40,pady=15,font='chalkduster 10',fg='#d10d0d',command=lambda: press('9')).grid(row=3,column=2,padx=3,pady=3)
bmul=Button(enus,text='x',padx=40,pady=15,font='chalkduster 10',fg='#d10d0d',command=lambda: press('*')).grid(row=3,column=3,padx=3,pady=3)

bc=Button(enus,text='C',padx=40,pady=15,font='chalkduster 10',fg='#d10d0d',command= clear).grid(row=2,column=0,padx=3,pady=3)
bb=Button(enus,text='B',padx=40,pady=15,font='chalkduster 10',fg='#d10d0d',command=lambda: press('B')).grid(row=2,column=1,padx=3,pady=3)
bd=Button(enus,text='%',padx=40,pady=15,font='chalkduster 10',fg='#d10d0d',command=lambda: press('%')).grid(row=2,column=2,padx=3,pady=3)
bdiv=Button(enus,text='/',padx=40,pady=15,font='chalkduster 10',fg='#d10d0d',command=lambda: press('/')).grid(row=2,column=3,padx=3,pady=3)

enus.mainloop()