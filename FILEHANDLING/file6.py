f=open("agc2.txt",'r')
s=f.readline().split()
print(s)

even=0
odd=0

for i in s:
    if int(i)%2==0:
        even+=1
    else:
        odd+=1
        
print("even",even)
print("odd",odd)

f.close()