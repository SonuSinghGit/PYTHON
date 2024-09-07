f=open("hello2.txt",'w')
f.write("hello world..!\n")
f.write("how you do in..!\n")
f.close()

f=open("hello3.txt",'w')
lines_list=['sonu\n' , 'vivek\n' , 'ashish\n']
f.writelines(lines_list)
f.close()