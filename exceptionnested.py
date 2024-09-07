try:
    num=int(input("enter the numerator: "))
    den=int(input("enter the denominator: "))
    try:
        result=num/den
        print("result: ",result)
    except:
        print("divide by zero error")
        
except:
    print("invalid input")
print("end of the program")