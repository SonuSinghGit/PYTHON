l=[23,54,24,67]
print(len(l))
s="welcome"
print(len(s))
#OVER LOADING(same function name but different parameters)

class demo:
    def showinfo(self,name):
        print("welcome to python"+name)

obj=demo()
obj.showinfo(" agc")
obj.showinfo(" sonu")#overloading