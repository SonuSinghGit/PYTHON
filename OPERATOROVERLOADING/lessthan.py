class A():
    def __init__(self,x):
        self.x=x
    
    def __lt__(self,other):
        if(self.x < other.x):
            return True
        
        else:
            return False
        
obj1=A(5)
obj2=A(9)
if(obj1<obj2):
    print("object1 is less than object 2")
else:
    print("obj1 is grater than object")