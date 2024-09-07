        # SET
#collection of many number/item but it provides us only unique number
#it means no duplicacy allow
# in set we use {} brackets
# in previous we learn if [] it means list, () it means tuple & {} it means set

marks={54,88,57,88,67,88}#here 88 repeat 3 times but in output its print only ones because no duplicacy allow in sets. 
print(marks)#output(88,57,67,54)
#print(marks[0]), not allow in sets or index are not acceseble here. only apply loos here. 
#if we have to print all the number of sets using loop

marks={86,67,78,67}
for score in marks:
        print(score)#output(67,78,86)