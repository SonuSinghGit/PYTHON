f= open("abc.txt","r")
g=open("xyz.txt","w")
s=f.readlines()

for i in s:
    if i[0].isupper():
        g.write(i)

print("lined copy")
f.close()
g.close()