import matplotlib.pyplot as plt
import numpy as np
l=['Facebook','youtube','linkedin','Instagram']
views=[357,798,343,205]
ex=[0,0,0.5,0.2]
plt.pie(views,labels=l,explode=ex)

#plt.xticks(bins)

plt.savefig('d:/ajax1.pdf',dpi=500,orientation='landscape',facecolor='blue',format='pdf')
plt.show()
