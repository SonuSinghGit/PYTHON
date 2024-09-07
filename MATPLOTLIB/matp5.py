from matplotlib import pyplot as plt
day=[1,2,3,4,5,6,7]
no=[2,3,1,4,5,3,6]
color=['r','g','b','m','y','b','r']
size=[200,323,168,400,522,322,600]
plt.scatter(day,no,c=color,s=size ,alpha=0.4,marker="*")
plt.title("scatter graph")
plt.xlabel("day")
plt.ylabel("no")
plt.show()