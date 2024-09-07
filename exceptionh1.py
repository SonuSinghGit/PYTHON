a=10
b=int(input("enter b:"))
try:
    c=a/b
except ZeroDivisionError:
    print("number division by zero not allowed :") 

print(c)
print(b)