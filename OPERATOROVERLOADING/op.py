class A:
    def __init__(self,a):
        self.a=a
        
    def __add__(self, other):
        return self.a + other.x
        
        
class B:
    def __init__(self,x):
        self.x=x
obj1=A(23)
obj2=B(45)
print(obj1+obj2)

    