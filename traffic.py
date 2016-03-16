import matplotlib.pyplot as plt
import numpy as np

vmax=136.
L=11.
rhomax=250.
nx=51
deltaT=0.001
deltaX=L/(nx-1)      # or L/nx
steps=np.arange(0,51,1)

x=np.linspace(0,L,nx)
rho0=np.ones(nx)*20
rho0[10:20]=50

for j in steps[1:]:
    copy=np.copy(rho0)
    #for n in np.arange(1,nx-1,1)
    #rho0[n]= (vmax/rhomax*2*copy[n]*(copy[n]-copy[n-1])/deltaX - vmax*(copy[n]-copy[n-1])/deltaX) * deltaT + \
    #            copy[n]
    rho0[1:]= (vmax/rhomax*2*copy[1:]*(copy[1:]-copy[:-1])/deltaX-vmax*(copy[1:]-copy[:-1])/deltaX)*deltaT+copy[1:]

rho0[0]=20


print(np.max(rho0))
print(np.mean(rho0))
plt.plot(x,rho0)
plt.ylabel('Distance / Km')
plt.xlabel('Car density')
plt.title('Traffic')
plt.grid(True)
plt.show()



