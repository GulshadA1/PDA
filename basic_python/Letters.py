
import os
def clear():
    os.system( 'cls' )

clear()

letter=''' Dear Mr.xyz:
                    Let me begin by thanking you for your 
 past contributions  to our Little League baseball team.
 Your sponsorship aided in the purchase of ten full
  uniforms and several pieces of baseball equipment f
  or last year's season.

Next month, our company is planning an employee appreciation 
pancake breakfast honoring retired employees for their past 
years of service and present employees for their loyalty and 
dedication in spite of the current difficult economic conditions.

We would like to place an order with your company for 25
 pounds of pancake mix and five gallons of maple syrup. We hope you 
will be able to provide these products in the bulk quantities we require.

As you are a committed corporate sponsor and long-time associate,
 we hope that you will be able to join us for breakfast on abc
Respectfully yours.

Mr.john

'''

name=input("enter name here\n ")
date =input("enter date here\n ")
 
letter =letter.replace('xyz',name)
letter =letter.replace('abc',date)
print(letter)