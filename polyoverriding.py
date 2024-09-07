class A:
    def showdata(self):
        print("this is function 1")

class B(A):
    def showdata(self):
        print("this is B class")
        
obj=B()
obj.showdata()
