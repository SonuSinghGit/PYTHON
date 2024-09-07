class A:
    def displayA(self):
        print("this is A class")
class B():
    def diplayB(self):
        print("this is B class")
class C(A,B):
    def displayC(self):
        print("this ic C class")      

obj=C()
obj.displayA()
obj.diplayB()
obj.displayC()