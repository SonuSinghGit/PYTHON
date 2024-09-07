try:
   n=int(input("enter a positive number:"))
   if n<=0:
    raise ValueError("not a positive number:")
except ValueError as ve:
        print(Ve)
print("you entered:",n)