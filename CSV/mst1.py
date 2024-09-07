import random
class hello:
    def out(self):
        l=[]
        n=int(input("Enter The Number :"))
        sat=int(input("Enter The Starting Point :"))
        end=int(input("Enter The End Point :"))
        for i in range(n):
            a=random.randint(sat,end)
            l.append(a)
        
        
        print(l)    
        max=l[0]
        min=0
        for i in range(len(l)):
            if max>l[i]:
                max=l[i]
            elif min<l[i]:
                min=l[i] 
        
        
        print("maximum: ",max , "minimum: " ,min)  

obj=hello()
obj.out()