import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio

#x = np.arange(0.0, 2, 0.01)
#y1 = np.sin(2*np.pi*x)
mat=sio.loadmat('xj.mat')
x = mat['asr']
y1 = mat['olr']
lat = mat['lat']
mean= mat['asr_glob_mean'][0][0]

# create empty array
a1 = np.empty(90)
b1 = np.empty(90)
lat1 = np.empty(90)
for i in range(90):
    a1[i] = x[i][0]
    b1[i] = y1[i][0]
    lat1[i]=lat[i][0]


fig, (ax1,ax2) = plt.subplots(2, 1, sharex=True)

ax1.fill_between(lat1, a1, mean, where=a1<mean,facecolor='cyan',interpolate=True)
ax1.set_ylabel('asr',fontsize=20)
ax1.plot(lat1,a1,'g')
ax1.axhline(mean,color='red',ls='dashed',lw=2,alpha=0.5)
ax1.set_yticklabels(np.arange(100,355,50),fontsize=16)
ax1.set_yticklabels(np.arange(100,355,50),fontsize=16)
#ax1.plot(mean,'r--',lw=2)

ax2.fill_between(lat1, b1, mean, where=b1<mean, facecolor='green')
ax2.set_ylabel('olr',fontsize=20)
ax2.plot(lat1,b1,'y')
ax2.axhline(mean,color='red',ls='dashed',lw=2,alpha=0.5)
ax2.set_yticks(np.arange(200,290,20))
ax2.set_yticklabels(np.arange(200,290,20),fontsize=16)

#ax2.set_ylabel('olr',fontsize=16)
plt.xlabel('lattitude',fontsize=16)
plt.xticks(np.arange(-90,100,30),fontsize=16)


plt.show()