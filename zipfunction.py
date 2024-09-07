l=[32,34,23,56]
l2=[76,75,44,34]
#using zip function
for a,b in zip(l,l2):
    print(a,b)
print(" ")
#another method
t=len(l)
for  h in range(t):
    print(l[h],l2[h])