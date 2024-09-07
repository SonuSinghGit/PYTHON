l=[]
for a in range(1,100):
    print(a)
    l.append(a)
print(l)

#list comprehension
n=[m for m in range(1,100) if m%2==0]
print(n)

a="hello"
b=[c for c in a]
print(b)