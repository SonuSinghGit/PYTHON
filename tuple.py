          #TUPLE
#tuple is just like list but it unmutable, once we made tuple we can not change .
#operation can't performe on tuple like list 
# () use insted of [] in tuple. let's see with an example

marks=(95,88,78,78,45,56,67,78,65,56)
print(marks.count(78))#output(3) it's count how many times 78 repeat in the list 
print(marks.count(56))
#to cheeck index of the marks
print(marks.index(88))#outut (1)
print(marks.index(56))#5

#but () are not nessacery in the tuple by default its make tuple. let's see with an example. 

person='ram','shayam','rohit'
print(person)