a=int(input("enter  the first number: "))
b=int(input("enter the second number: "))
try:
    res=a/b
    print("result= ",res)
    c=a+"hello"
except:
    print("exception handler")

print(c)
print("end of the code")