import os
def clear():
    os.system('cls')

clear()

a=float(input("enter a number :"))

if a > 0 :
    print("num is positive ",a)

elif a < 0 :
    print ("num is negative ",a)

else  :
    print("num is zero ",a)
 
input()