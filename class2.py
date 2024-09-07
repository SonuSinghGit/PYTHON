class A:
    "LEARN CODING"
    age=10
    print(age)
    
obj=A()#10
print(obj.age)#10
print(A.age)#10
print(A.__doc__)#learn coding



class A:
    age=23
    def function(self):
        "welcome to python"
        name="sonu singh"
        print(name)
obj=A()
obj.function()#sonu singh
print(obj.age)#23
print(A.age)#23
print(obj.function.__doc__)#welcome to python


#class with arguments
class A:
    
    def function(self,age,name,address,):
        print(age," ",name," ",address)
obj=A()
obj.function(12,"sonu","siwan")#12 sonu siwan

#using constructor
class A:
    
    def __init__(self,age,name,address,):
        print(age," ",name," ",address)
obj=A(22,"yash","mairwa")#22 yash mairwa
obj=A("vivek",34,"2300")#vivek 34 2300
