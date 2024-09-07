from matplotlib import pyplot as plt
views=[534,258,689,401,724,689,350]
days=range(1,8)
plt.plot(days,views,label='Youtube viewership',color='k',marker='H',markerfacecolor='r',ls='-.',lw=3)
plt.xlabel ('Number of days')
plt.ylabel('Youtube views')
plt.legend()
plt.title("Viewer graph for youtube videos")
plt.show()
