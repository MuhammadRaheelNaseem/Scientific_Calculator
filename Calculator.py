
from math import sin,asin,cos,acos,tan,atan,log,sqrt,log10
from tkinter import * 
import tkinter

equation=' '

def enter(num):
    global equation
    equation = equation + str(num)
    input_var.set(equation)

def equal():
    try:
        global equation
        if equation == 'sin({})':
            equation=sin()
        elif equation == 'asin()':
            equation=asin()
        elif equation == 'cos()':
            equation=cos()
        elif equation == 'acos()':
            equation=acos()
        elif equation == 'tan()':
            equation=tan()
        elif equation == 'atan()':
            equation=atan()
        elif equation == 'sqrt(':
            equatuin= sqrt()
        elif equation == 'log10(':
            equation = log10()
        elif equation == 'log(':
            equation = log()
        else:
            answer=eval(str(equation))
        input_var.set(answer)
        equation=' '
    except:
        input_var.set('Error')
        equation=''
    
#def scientofic_equal:
    
    
def clear():
    global equation
    equation=''
    input_var.set('')





gui=Tk()

input_var=StringVar()

gui.title('Scientific Calculator')
gui.geometry('583x526')
gui.configure(bg='#F4D03F')
gui.minsize(543,526)
gui.maxsize(543,526)

ent1=Entry(gui,font=('Times 33'),justify='right',textvariable=input_var,bg='#ABEBC6')
ent1.place(x=0,y=8,width=539,height=100)

# x------------x-------------x------------x-------------x------------x-------------x

btnClear=Button(gui,text='CE',font=('Arial 18'),width=5,height=2,command=clear,bg='#F4D03F',relief=RIDGE)
btnroot=Button(gui,text='√',font=('Arial 18'),width=5,height=2,command=lambda:enter('sqrt('),bg='#F4D03F',relief=RIDGE)
btnmul=Button(gui,text='x',font=('Arial 18'),width=5,height=2,command=lambda:enter('*'),bg='#F4D03F',relief=RIDGE)
btndiv=Button(gui,text='÷',font=('Arial 18'),width=5,height=2,command=lambda:enter('/'),bg='#F4D03F',relief=RIDGE)
btnlog=Button(gui,text='log',font=('Arial 18'),width=5,height=2,command=lambda:enter('log10('),bg='#F4D03F',relief=RIDGE)
btnln=Button(gui,text='ln',font=('Arial 18'),width=5,height=2,command=lambda:enter('log('),bg='#F4D03F',relief=RIDGE)
btnClear.place(x=7,y=125)
btnroot.place(x=95,y=125)
btnmul.place(x=188,y=125)
btndiv.place(x=280,y=125)
btnlog.place(x=370,y=125)
btnln.place(x=460,y=125)

# x------------x-------------x------------x-------------x------------x-------------x

btn7=Button(gui,text='7',font=('Arial 18'),width=5,height=2,command=lambda:enter(7),bg='#F4D03F',relief=RIDGE)
btn8=Button(gui,text='8',font=('Arial 18'),width=5,height=2,command=lambda:enter(8),bg='#F4D03F',relief=RIDGE)
btn9=Button(gui,text='9',font=('Arial 18'),width=5,height=2,command=lambda:enter(9),bg='#F4D03F',relief=RIDGE)
btnadd=Button(gui,text='+',font=('Arial 18'),width=5,height=2,command=lambda:enter('+'),bg='#F4D03F',relief=RIDGE)
btnsin=Button(gui,text='sin',font=('Arial 18'),width=5,height=2,command=lambda:enter('sin'),bg='#F4D03F',relief=RIDGE)
btnsin_inv=Button(gui,text='sin-1',font=('Arial 18'),width=5,height=2,comman=lambda:enter('asin'),bg='#F4D03F',relief=RIDGE)
btn7.place(x=7,y=205)
btn8.place(x=95,y=205)
btn9.place(x=188,y=205)
btnadd.place(x=280,y=205)
btnsin.place(x=370,y=205)
btnsin_inv.place(x=460,y=205)

# x------------x-------------x------------x-------------x------------x-------------x

btn4=Button(gui,text='4',font=('Arial 18'),width=5,height=2,command=lambda:enter(4),bg='#F4D03F',relief=RIDGE)
btn5=Button(gui,text='5',font=('Arial 18'),width=5,height=2,command=lambda:enter(5),bg='#F4D03F',relief=RIDGE)
btn6=Button(gui,text='6',font=('Arial 18'),width=5,height=2,command=lambda:enter(6),bg='#F4D03F',relief=RIDGE)
btnsub=Button(gui,text='-',font=('Arial 18'),width=5,height=2,command=lambda:enter('-'),bg='#F4D03F',relief=RIDGE)
btncos=Button(gui,text='cos',font=('Arial 18'),width=5,height=2,command=lambda:enter('cos('),bg='#F4D03F',relief=RIDGE)
btncos_inv=Button(gui,text='cos-1',font=('Arial 18'),width=5,height=2,command=lambda:enter('acos('),bg='#F4D03F',relief=RIDGE)
btn4.place(x=7,y=280+5)
btn5.place(x=95,y=280+5)
btn6.place(x=189,y=280+5)
btnsub.place(x=280,y=280+5)
btncos.place(x=370,y=280+5)
btncos_inv.place(x=460,y=280+5)


# x------------x-------------x------------x-------------x------------x-------------x

btn1=Button(gui,text='1',font=('Arial 18'),width=5,height=2,command=lambda:enter(1),bg='#F4D03F',relief=RIDGE)
btn2=Button(gui,text='2',font=('Arial 18'),width=5,height=2,command=lambda:enter(2),bg='#F4D03F',relief=RIDGE)
btn3=Button(gui,text='3',font=('Arial 18'),width=5,height=2,command=lambda:enter(3),bg='#F4D03F',relief=RIDGE)
btnEqual=Button(gui,text='=',font=('Arial 18'),width=5,height=5,command=equal,bg='#F4D03F',relief=RIDGE)
btntan=Button(gui,text='tan',font=('Arial 18'),width=5,height=2,command=lambda:enter('tan('),bg='#F4D03F',relief=RIDGE)
btntan_inv=Button(gui,text='tan-1',font=('Arial 18'),width=5,height=2,command=lambda:enter('atan('),bg='#F4D03F',relief=RIDGE)
btn1.place(x=7,y=243+123)
btn2.place(x=95,y=243+123)
btn3.place(x=189,y=243+123)
btnEqual.place(x=280,y=243+123)
btntan.place(x=370,y=243+123)
btntan_inv.place(x=460,y=243+123)

# x------------x-------------x------------x-------------x------------x-------------x

btn0=Button(gui,text='0',font=('Arial 18'),width=11,height=2,command=lambda:enter(0),bg='#F4D03F',relief=RIDGE)
btndot=Button(gui,text='.',font=('Arial 18'),width=5,height=2,command=lambda:enter('.'),bg='#F4D03F',relief=RIDGE)
btnA=Button(gui,text='(',font=('Arial 18'),width=5,height=2,command=lambda:enter('('),bg='#F4D03F',relief=RIDGE)
btnB=Button(gui,text=')',font=('Arial 18'),width=5,height=2,command=lambda:enter(')'),bg='#F4D03F',relief=RIDGE)
btn0.place(x=9,y=448)
btndot.place(x=190,y=448)
btnA.place(x=370,y=448)
btnB.place(x=456,y=448)




gui.mainloop()
