a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if(a>b and b>c):
    print(a,"is big")
if(b>a and a>c):
    print(b,"is greater")
else:
    print(c, "is big")        

