class A:
    a=int(input("enter your salary:"))
    b=int(input("enter your year:"))
    
    if(b>=5):
        c=a+(a*0.20)
        print("updated salary:",c)
    else:
        print("original salary",a)
        
obj=A()