import csv
head=[]
rows=[]
f=open('4cse1new.csv', mode='r')
csvr=csv.reader(f)

head=next(csvr,None)
print(head)
for i in csvr:
    print(i)
