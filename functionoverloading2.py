class Student:
       def sayHello(self, name=None):
              if name is not None:
                     self.name = name
                     print("Hey, " , name)
              else:
                     print("Hey")
stu = Student()
print(stu.sayHello())
print(stu.sayHello('dasu'))