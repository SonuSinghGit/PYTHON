f=open("hello.txt",'r')
data=f.readline(5)
print(data)
f.close()


f=open("hello.txt",'r')
data=f.readlines()
print(data)
f.close()

f=open("hello.txt",'r')
data=f.readlines()
for line in data:
   print(line)
f.close()