f=open("hello.txt",'r')
print(f.readable())
print(f.writable())
f.close()

f=open("hello.txt",'r+')
print(f.readable())
print(f.writable())
f.close()