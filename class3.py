class demo:
    def fun(self):
        print("this is normal functon")
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(a+b)
        
    def __del__(self):
        print("destructor called")
        
obj=demo(12,12)
print(obj.fun())
del obj