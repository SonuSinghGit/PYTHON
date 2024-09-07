num=int(input("enter any number:"))
fact=1
a=1
while (a<=num):
    fact=fact*a
    a=a+1
print("factorial of the number is:",fact)   

#another method
a=int(input("enter any number:"))
fact=1
while(a>0):
    fact=fact*a
    a=a-1
print("factorial of the number:",fact)

#using for loop
n=int(input("enter any number:"))
fact=1
for i in range(n,0,-1):
    fact=fact*i
print("factorial of the number is:",fact)