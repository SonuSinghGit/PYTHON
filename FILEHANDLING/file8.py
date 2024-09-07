from random import randint

f=open("rand.txt",'w')

for i in range(1,16):
    
    x=randint(500,1000)
    f.write(str(x) + " ")
    
print("number generated..")
f.close()