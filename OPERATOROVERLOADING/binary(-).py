class A:
    
    def __init__(self,a,b):
        self.a= a
        self.b= b
        
        
    def __sub__(self,other):
        return self.a-other.x , self.b- other.y
        
        
class B:
    def __init__(self,x,y):
        self.x=x
        self.y=y
              
obj1=A(12, 23)
obj2=B(5, 3)
print(obj1-obj2)