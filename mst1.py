import random
class A:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    for i in range(1,5):
        x=random.randint(a, b)
        print(x)
    n=tuple(map(x.split(', ')))
    s=max(n)
    print(s)


    