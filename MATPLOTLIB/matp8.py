import matplotlib.pyplot as plt
y_views=[534,689,258,401,724,689,435,534,545,435,423,789,905,561]
#f_views=[123,342,700,304,405,650,325,59,87,456,342,657,43,32]
#t_views=[202,209,176,415,824,389,550]
bins=[100,200,300,400,500,600,700,800,900,1000]
#days=range(1,15)
plt.hist(y_views,bins,label='Youtube views')
plt.xlabel ('Number of days')
plt.ylabel('Youtube views')
plt.legend(loc='upper left')
plt.title("Bar Graph for comparative analysis")
#plt.grid(True,ls='-.',color='red',lw=1)
#plt.xticks(bins)
plt.savefig('d:/ajax1.pdf',dpi=500,orientation='landscape',facecolor='blue',format='pdf')
plt.show()
