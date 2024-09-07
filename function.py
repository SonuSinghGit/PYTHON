                 #FUNCTIONS
'''1. IN- BUILT FUNCTION
2. MODULE FUNCTIONS
3. USER-DEFINED FUNCTIONS

1.in- built function:-
int(),str(),bool() they all are in built fuction

2. module function:-
math '''

#lets see the math module function
import math
print(dir(math))

from math import sqrt# here we pick sqrt of math function
print(sqrt(6))#output(2.4494....)
print(sqrt(16))#output(4.0)

#if we take all module function of math then we have to write *(select all) after import. 
#And now we ready to use all module fuction of math. let's see

from math import *
print(sqrt(25))#output(5.0)

# 3.USER-DEFINED FUNCTION
#user make own function itself 
'''  SYNTAX OF USER-DEFINED FUNCTION
           def function_name(parameters):
       // do something  '''
# sum of two number using function

def sum(first,second):
    print(first+second)
sum(5,7)# function call output(12)

#another example
def sum(first, second=6):#second already decleared 
    print(first+second)
sum(9)# only one arguments pass only for first
