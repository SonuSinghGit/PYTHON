                   #LIST

''' we store premitive datatype(int,string,float,boolean) in list. and in other word,
  list are collection of item and it's complex datatype'''

marks=[90,97,87,"hello"] #here marks is a list & we store diff. datatype in list
print(type(marks)) 

#if we have print individual subject marks

marks=[56,97,98,67,]
print(marks[1]) #here only index [1] value will be print

#here one difference in indexing in python is that, index is having negative also that is
# -1,-2,-4..... -1 means index from the last(67), -2 means(98) 

marks=[80,78,57,89]
print(marks[-1]) #output=89

#if we need a selective subject marks lets suppose we don't need marks of last two index. 
#then we make a new list for that 
#LETS SEE THIS EXAMPLE

marks=[67,46,67,79,89,35,68]
print(marks[0:5])#here index 5 not include so marks will be print only 4th index.
#so output=(67,46,67,79,89) 

    #FOR LOOP IN LIST
marks=[56,86,84]  
for score in marks: #'for' and 'in' is a keyword while 'score' is a variable
    print(score) 

#APPEND OPERATION(ADD) IN LIST
marks=[82,72,84]
marks.append(89) #89 will be add on last index of the marks list
print(marks) #output=(82,72,84,89)

#IF WE HAVE INSERT MARKS IN THE STARTING OR ANY WHERE ELSE
marks=[75,65,95]
marks.insert(1,81) #81 will be insert at index 1
print(marks) #output=(75,81,65,95)

#TO CHEECK THE NUMBER OR ELEMENT EXISTING IN THE LIST OR NOT
marks=[73,76,81]
marks.insert(3,99)#99 insert at index 3 #output=(73,76,81,99)
print(99 in marks)#output=(true) 

#TO FIND LENGTH OF THE LIST OF GIVEN DATA
marks=[75,57,79]
marks.append(99)#99 add in the marks list
print(len(marks))#output=(4)

#PRINT MARKS USING WHILE LOOP
marks=[45,67,89]
i=0
while i<len(marks):#while operate on lenght
  print(marks[i])
  i=i+1

  #IF WE HAVE TO EMPTY THIS LIST
marks=[46,78,99]
i=0
while i<len(marks):
  print(marks[i])
  i=i+1

marks.clear()
print(marks)

marks=[45,67,67,34,89]
i=0
while i<len(marks):#while operate on lenght
  print(marks[i])
  i=i+1
marks.clear()
print(marks)
