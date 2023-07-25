
import os
def clear():
    os.system( 'cls' )

clear()

letter=''' Greetings name
you are selected 
You can join on date'''

name=input("enter name here\n ")
date =input("enter date here\n ")
 
letter =letter.replace('name',name)
letter =letter.replace('date',date)
print(letter)