num=int(input("enter the number:"))
if num==1:
    print("it is not prime number:")
    
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("it is not a prime number: ")
            break
        else:
            print("it is prime number")
            break