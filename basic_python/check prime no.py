# Program to check if a number is prime or not

import os
def clear():
    os.system( 'cls' )

clear()

num=int(input("enter a number  "))
if num >1:
    for i in range(2,num//2):  #// means if 5//2 so the answer wil be 2 
                               #it will always give int in return        

         if ( num % i)==0 :
            print(i,"times",num//i,"is",num,"so it is not prime")
            break

    else:
        print(num,"is a prime number")

else:
    print("Invalid input")

input()