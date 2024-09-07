        #DICTIONARY
# in dictionary we store key value pair like student subject name and marks obtained in that subject. 
#Also student name and his parents name altogether. lets see an example. 

marks={'math':76,'english':89,'chemistry':88}
print(marks['math']) #output(76)
print(marks["chemistry"])# output(88)

#lets see we store student name and his parents name altogether. 
information={"rohit":"ramesh","ram":"dashrath"}
print(information["ram"])#output(dashrath)

# if we add new suubject marks and then print

marks={"math":55,"hindi":85}
print(marks["math"])#output(55)
marks["physics"]=98;#add marks of physics
print(marks )
#we change the marks of physics 78 insted of 98
marks["physics"]=78;
print(marks)

