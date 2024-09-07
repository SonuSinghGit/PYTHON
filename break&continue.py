         #  BREAK & CONTINUE
#break & continue are two important keyword in python 
#let's see with an example. let make a list of student name and store in a variable that is student
# BREAK STATEMENT
student=["ram","shyam","kishan","radha","saloni"]
for student in student:
    if student=="radha":
        break;
    print(student) #output(ram,shyam,kishan)

# CONTINUE STATEMENT
student=['ram','rohit','shyam','radha','kishan']
for student in student:
    if student=="shyam":
        continue;
    print(student)    
