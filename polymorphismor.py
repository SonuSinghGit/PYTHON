class A:
    def function1(self):
        print("this is class A ")
    
class B(A):
    def function1(self):
        super().function1()
        print("this is class B ")
        
obj=B()
obj.function1()