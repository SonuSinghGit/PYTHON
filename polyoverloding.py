class area:
    def find_area(self,x=None,y=None):
        
        if x!=None and y!=None:
            print(x*y)
        elif x!=None:
            print(x*x)
        else:
            print("nothing found ")
            
obj=area()#function oveloading(same function but diff. parameters)
obj.find_area()
obj.find_area(12,2)
obj.find_area(6)