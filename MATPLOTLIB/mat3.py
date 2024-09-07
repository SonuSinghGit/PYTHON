from matplotlib import pyplot as plt
x=["python","c","c++","java"]
y=[85,70,60,83]
plt.xlabel("languages",fontsize=15)
plt.ylabel("Number",fontsize=15)
plt.title("student record",fontsize=15)
c=["y","b","m","g"]
plt.bar(x,y,width=0.4,color=c,label="marks details")
plt.legend()
plt.show()