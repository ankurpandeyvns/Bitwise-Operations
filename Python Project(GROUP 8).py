from Tkinter import*
import Tkinter as tk
root=Tk()
root.wm_title("Main Frame")
def callback(number):
    global opr,n2
    if(number==1):
        opr="AND"
        entry_2.configure(state="normal")
        entry_2.update()
    elif(number==2):
        opr="OR"
        entry_2.configure(state="normal")
        entry_2.update()
    elif(number==3):
        opr="NOT"
        entry_2.insert(0,00)
        entry_2.configure(state="disabled")
        entry_2.update()
    elif(number==4):
        opr="XOR"
        entry_2.configure(state="normal")
        entry_2.update()
opr="AND" #DEFAULT VALUE IS AND..[DEFAULT VALUE SO THAT PROGRAM DOESN'T CRASH WHEN NO OPTION IS SELECTED.]
####################################################################################################################
#################              CALCULATION SECTION(MADE BY SWETANK AND DIVIT)              #########################
####################################################################################################################
from string import*
def dec2bin(n):
    lst=[]
    if n==1:
        lst.append(1)
    elif n==0:
        lst.append(0)
    else:
        while n > 1:
            rem = n%2
            quo = n/2
            if quo == 1:
                lst.append(rem)
                lst.append(quo)
            elif quo > 1:
                lst.append(rem)
            n = quo
    lst.append(0)
    return lst

def lenCmp(m1,m2):
    if len(m1) > len(m2):
        x = len(m1) - len(m2)
        while x > 0:
            m2.append(0)
            x -= 1
    elif len(m1) < len(m2):
        x = len(m2) - len(m1)
        while x > 0:
            m1.append(0)
            x -= 1
    m1.reverse()
    m2.reverse()

def andOp(b1,b2):
    i = 0
    andlst=[]
    while i < len(m2):
        if m1[i] == 0 and m2[i] == 0:
            andlst.append(0)
        elif m1[i] is not m2[i]:
            andlst.append(0)
        else:
            andlst.append(1)
        i = i+1
    t1 = andlst
    #t1 = map(str,andlst)
    return t1

def orOp(b1,b2):
    i = 0
    orlst=[]
    while i < len(m2):
        if m1[i] == 0 and m2[i] == 0:
            orlst.append(0)
        elif m1[i] is not m2[i]:
            orlst.append(1)
        else:
            orlst.append(1)
        i = i+1
    t2 = orlst
    #t2 = map(str,orlst)
    return t2

def xorOp(b1,b2):
    i = 0
    xorlst=[]
    while i < len(m2):
        if m1[i] == m2[i]:
            xorlst.append(0)
        else:
            xorlst.append(1)
        i = i+1
    t3 = xorlst
    #t3 = map(str,xorlst)
    return t3

def notOp(b1):
    i = 0
    notlst=[]
    while i < len(m1):
        if m1[i] == 0:
            notlst.append(1)
        elif m1[i] == 1:
            notlst.append(0)
        i = i+1
    t4 = notlst
    #t4 = map(str,notlst)
    return t4

def bin2dec(n):
    n.reverse()
    d = 0
    x = 0
    while x < (len(n)-1):
        d = d + (n[x] * (2**x))
        x = x + 1
    n.reverse()
    return d

def conv2str(z1):
    z2 = map(str,z1)
    return z2
####################################################################################################################
#################                       GUI SECTION(MADE BY ANKUR)                 #################################
####################################################################################################################
def printVal():
    global n1,n2,m1,m2,t1,t2,t3,t1str,t2str,t3str,t4str,res,dec
    n1=int(entry_1.get())
    n2=int(entry_2.get())
    m1 = dec2bin(n1)
    m2 = dec2bin(n2)
    lenCmp(m1,m2)
    t1 = andOp(m1,m2)
    t2 = orOp(m1,m2)
    t3 = xorOp(m1,m2)
    t4 = notOp(m1)
    m1d = bin2dec(m1)
    m2d = bin2dec(m2)
    t1d = bin2dec(t1)
    t2d = bin2dec(t2)
    t3d = bin2dec(t3)
    t4d = bin2dec(t4)
    t1str = conv2str(t1)
    t2str = conv2str(t2)
    t3str = conv2str(t3)
    t4str = conv2str(t4)
    m1 = map(str,m1)
    m2 = map(str,m2)
    m1 = join(m1,"")
    m2 = join(m2,"")
    if(opr=="AND"):
        res=join(t1str, "")
        dec=t1d
    elif(opr=="OR"):
        res=join(t2str, "")
        dec=t2d
    elif(opr=="XOR"):
        res=join(t3str, "")
        dec=t3d
    elif(opr=="NOT"):
        res=join(t4str, "")
        dec=t4d
    entry_3.delete(0,END)
    entry_3.insert(0,res)


def explanation():
    printVal()
    ex = Toplevel(root)
    ex.wm_title("Explanation")
    Label(ex, text="Number 1").grid(row=0,column=0)
    Label(ex, text="Number 2").grid(row=1,column=0)
    Label(ex, text="Binary NUM1").grid(row=0,column=2)
    Label(ex, text="Binary NUM2").grid(row=1,column=2)
    Label(ex, text=opr).grid(row=3,column=2)
    Label(ex, text="Decimal Result").grid(row=4,column=1)
    entry_3 = Entry(ex)
    entry_10 = Entry(ex)
    entry_5 = Entry(ex)
    entry_6 = Entry(ex)
    entry_7 = Entry(ex)
    entry_8 = Entry(ex)
    entry_3.grid(row=0,column=1)
    entry_10.grid(row=1,column=1)
    entry_5.grid(row=0,column=3)
    entry_6.grid(row=1,column=3)
    entry_7.grid(row=3,column=3)
    entry_8.grid(row=4,column=2)
    entry_3.insert(0,n1)
    entry_10.insert(0,n2)
    if(opr=="AND"):
        entry_10.configure(state="normal")
        entry_10.update()
    elif(opr=="OR"):
        entry_10.configure(state="normal")
        entry_10.update()
    elif(opr=="NOT"):
        entry_6.insert(0,00)
        entry_6.configure(state="disabled")
        entry_6.update()
        entry_10.configure(state="disabled")
        entry_10.update()
    elif(opr=="XOR"):
        entry_10.configure(state="normal")
        entry_10.update()
    entry_5.insert(0,m1)
    entry_6.insert(0,m2)
    entry_7.insert(0,res)
    entry_8.insert(0,dec)

#LABELS
Label(root, text="Number 1").grid(row=0,column=0)
Label(root, text="Number 2").grid(row=0,column=2)
Label(root, text="Result is").grid(row=4,column=0)
#TEXT INPUT
entry_1 = Entry(root)
entry_2 = Entry(root)
entry_3 = Entry(root)
#RADIO BUTTONS
Radiobutton(root,text="AND",value=1,command=lambda: callback(1)).grid(row=1,column=0)
Radiobutton(root,text="OR",value=2,command=lambda: callback(2)).grid(row=1,column=1)
Radiobutton(root,text="NOT",value=3,command=lambda: callback(3)).grid(row=2,column=0)
Radiobutton(root,text="XOR",value=4,command=lambda: callback(4)).grid(row=2,column=1)
#BUTTONS
button_5=Button(root,text="Result",command=printVal).grid(row=3,column=0)
button_6=Button(root,text="Explanation",command=explanation).grid(row=3,column=1)
#GRID GEOMETRY MANAGER
entry_1.grid(row=0,column=1)
entry_2.grid(row=0,column=3)
entry_3.grid(row=4,column=1)

root.mainloop()
####################################################################################################################
#################                       END OF PROGRAM                             #################################
####################################################################################################################