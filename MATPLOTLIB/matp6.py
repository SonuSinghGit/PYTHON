import matplotlib.pyplot as plt
y_views=[534,258,689,401,724,689,350]
f_views=[123,342,700,304,405,650,325]
t_views=[202,209,176,415,824,389,550]
days=range(1,8)
plt.plot(days,y_views,label='Youtube views',color='b',marker='2',markerfacecolor='g',ls='-.')
plt.plot(days,f_views,label='facebook views',color='g',marker='v',markerfacecolor='g',ls='dashed')
plt.plot(days,t_views,label='twitter views',color='r',marker='v',markerfacecolor='g',ls='dashed')
plt.xlabel ('Number of days')
plt.ylabel('Youtube views')
plt.legend(loc='upper left')
plt.title("Viewer graph for youtube videos")

#plt.bar(days,y_views,label='Youtube views',color='b',ls='-.')
#plt.bar(days,f_views,label='facebook views',color='g',ls='dashed')
#plt.bar(days,t_views,label='twitter views',color='r',ls='dashed')
#plt.grid(True,ls='-.',color='red',lw=1)
#plt.xticks(days)
plt.savefig('d:/ajax1.pdf',dpi=500,orientation='landscape',facecolor='blue',format='pdf')

plt.show()
