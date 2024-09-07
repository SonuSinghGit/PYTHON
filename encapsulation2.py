class student:
    __name="sonu"
    def __init__(self):
        print(self.__name)
        self.__dispalyinfo()
    
    def __dispalyinfo(self):
        print("this is private function")

obj=student()