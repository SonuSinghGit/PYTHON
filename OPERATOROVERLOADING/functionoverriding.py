class A:
    def result(self,a,b):
        print("addition of a and b is:", a+b)
        
class B(A):
    def result(self,x,y):
        super().result(10,5)
        print("multiplication of a and b :",x*y)       
obj1=B()
obj1.result(2,5)