import csv
import sys
try:
    f=open("movie.csv","r")
    f1=open("movies.csv","w")
    next(f)
    csvreader=csv.reader(f)
    csvwriter=csv.writer(f1,lineterminator="\n")
    for i in csvreader:
        if i not in (None,''):
            if i[2]<'1988' and i[3]=='4.2' and i[4]<'10800':
              print(i)
              csvwriter.writerow(i)
    f.close()
    f1.close()          
except:
    print(sys.exc_info()[0])
else:
    print("No Error Occurs")    
finally:
    print("Code Is Executed")