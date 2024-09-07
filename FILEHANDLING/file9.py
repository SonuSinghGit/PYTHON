f=open("rand.txt",'r')

even=0
s=f.readline().split()

for i in s:
    if int(i)%2==0:
        even+=1
        print(i)
print("the even numbers are",even)

f.close()
