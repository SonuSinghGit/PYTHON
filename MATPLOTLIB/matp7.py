import matplotlib.pyplot as plt
y_views=[534,258,689,401,724,689,350,456,345,234,57,87,65,16]
f_views=[123,342,700,304,405,650,325,59,87,456,342,657,43,32]
#t_views=[202,209,176,415,824,389,550]
days=range(1,15)
#plt.bar(days,y_views,label='Youtube views')
#plt.bar(days,f_views,label='facebook views')
plt.bar([a-0.25 for a in days],y_views,label='Youtube views',width=0.25,align='edge')
plt.bar([a+0.25 for a in days],f_views,label='facebook views',width=-0.25,align='edge')

#plt.plot(days,t_views,label='twitter views',color='r',marker='v',markerfacecolor='g',ls='dashed')
plt.xlabel ('Number of days')
plt.ylabel('Youtube views')
plt.legend(loc='upper left')
plt.title("Bar Graph for comparative analysis")
plt.grid(True,ls='-',color='red',lw=3)
plt.xticks(days)
plt.savefig('d:/ajax1.pdf',dpi=500,orientation='landscape',facecolor='blue',format='pdf')
plt.show()
