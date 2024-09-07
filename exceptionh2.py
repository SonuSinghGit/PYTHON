a=9
b=int(input("enter b:"))
try:
    c=a/b
    d=c+"a"
except  ZeroDivisionError:
    print("division by zero not allowed") 

print(a) 
print(b)
print(c)
print(d)