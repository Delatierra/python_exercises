#Uebung 1

def mult():
    a= float(input("1: "))
    b= float(input("2: "))

    c=a*b
    return c

print (mult())

#Uebung 2

def gleichung(a,b):
    if a>0 and b>0:
        result= f"{a}x +{b}=0"
    return result
print (gleichung(2,5))

#Uebung 3

def gleichung_drei(a,b,c):
    if a>0 and b>0 and c>0:
        result= f"{a}x**2+{b}x+{c}"
    else:
        print("no 0 allowed")
    return result
print (gleichung_drei(2,5,4))

#Uebung 4

def fakt(n):
    summe=0
    for i in range(1, n+1):
        summe += (i**2)
    return (summe)
print (fakt(4))

#N Faktorial

def fakt_n(n):
    summe=1
    for i in range (1, n+1):
        summe*=i
    return summe
print (fakt_n(3))