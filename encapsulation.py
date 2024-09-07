class student:
    def __init__(self):
        self.__name=""
    def getname(self):
        return self.__name
    def setname(self,a):
        self.__name=a

obj=student()
obj.setname("testing")
a=obj.getname()
print(a)