Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = 42
if x%2 == 0:
    print("even")

    
even
if x < 10:
    print("one digit number")
elif x < 100:
    print ("two digit number")
else:
    print ("more than two digit")

    
two digit number
x = ["hello", "world"]
x = [1,3,"hello","world",["another","list"]]
x = [3,5,6]
len(x)
3
x[1]
5
x[4]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    x[4]
IndexError: list index out of range
x[0]
3
import time
time.asctime()
'Fri Jun 30 15:50:59 2023'
#module
import sys
print(sys.argv.append[1])
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(sys.argv.append[1])
TypeError: 'builtin_function_or_method' object is not subscriptable
