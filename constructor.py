class demo:
    a=10
    def __init__(self):
        print("this is constructor")#constructor
    
    def showvalue(self):
        self.c=self.a*self.a
        print(self.c)

    def showvalue1(self,a,b):
        print(a+b)
obj=demo()
obj.showvalue()
obj.showvalue1(34,345)    
