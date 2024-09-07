#program for print the string one by one

s="welcome"
l=len(s)
print(l)#17
for a in range(l):#17
    print(s[a])

#for reverse
print(" ")
for a in range(l-1,-1,-1):
    print(s[a])
#shortcut meathod
s="sonu"
for a in s:
    print(a)