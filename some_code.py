#!/usr/bin/env python3
r = 14
t1 = "THIS IS A VIRUS"
t2 = "SEND ME BITCOIN"
print("")
for i in range(-r//2,r//2+1):
    print(7*" ",end="")
    if i == -1:
        print("x",(r-10)*" ",t1,(r-10)*" ","x")
    
    elif i == +1:
        print("x",(r-10)*" ",t2,(r-10)*" ","x")
    else:
        for j in range(-r,r+1):    
            print("x",end="") if (2*i)**2 + j**2 >= r**2 else print(" ",end="")
        print("")
print("")