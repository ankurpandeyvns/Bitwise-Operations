#only for +ve decimal numbers

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
    t1 = map(str,andlst)
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
    t2 = map(str,orlst)
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
    t3 = map(str,xorlst)
    return t3

n1 = input("Enter the first number in decimal number system: ")
n2 = input("Enter the second number in decimal number system: ")
m1 = dec2bin(n1)
m2 = dec2bin(n2)
lenCmp(m1,m2)
t1 = andOp(m1,m2)
t2 = orOp(m1,m2)
t3 = xorOp(m1,m2)
m1 = map(str,m1)
m2 = map(str,m2)
m1 = join(m1,"")
m2 = join(m2,"")
print "NUM1: ",m1
print "NUM2: ",m2
print "AND : ", join(t1, "")
print "OR  : ", join(t2, "")
print "XOR : ", join(t3, "")

