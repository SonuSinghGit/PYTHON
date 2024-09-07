f=open("first.txt","r")
f2=open("second.txt","w")
s=f.readlines()

for i in s:
    f2.write(i)
f.close()
f2.close()