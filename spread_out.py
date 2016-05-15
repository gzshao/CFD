import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams, cm
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16

## For spreading out homework

n = 192
Du = 0.00016
Dv = 0.00008
F = 0.035
k = 0.065
dh = 5./(n-1)
T = 8000
dt = .9 * dh**2/(4*max(Du,Dv))
nt = int(T/dt)
x=np.linspace(0,5.,n)
#print(len(x))
y=np.linspace(0,5.,n)


uvinitial = np.load('./uvinitial.npz')
u = uvinitial['U']
v = uvinitial['V']
#print(u[100,:])

#u[-1,:]=u[-2,:]
#u[:,-1]=u[:,-2]
#u[1,:]=u[2,:]
#u[:,1]=u[:,2]

#v[-1,:]=v[-2,:]
#v[:,-1]=v[:,-2]
#v[1,:]=v[2,:]
#v[:,1]=v[:,2]
#print('dt =')
#print(dt)
#print('nt = ')
#print(nt)
#print(u[100,:5])

plt.figure(figsize=(8,5))
#plt.subplot(121)
plt.contourf(x,y,u,20,cmap=cm.viridis)
plt.xlabel('$x$')
plt.ylabel('$y$')
#plt.subplot(122)
#plt.contourf(x,y,v,20,cmap=cm.viridis)
#plt.xlabel('$x$')
#plt.ylabel('$y$')
plt.colorbar();
plt.show()

def ftcs():
    for n in range(nt):
        un=u.copy()
        vn=v.copy()
        u[1:-1,1:-1] = un[1:-1,1:-1]+Du*dt/dh**2*(un[2:,1:-1]+un[:-2,1:-1]+un[1:-1,2:]+un[1:-1,:-2]-4*un[1:-1,1:-1])-dt*un[1:-1,1:-1]*(vn[1:-1,1:-1])**2 +F*dt -F*dt*un[1:-1,1:-1]

#u[1:-1,1:-1]+=Du*dt/dh**2*(un[2:,1:-1]+un[:-2,1:-1]+un[1:-1,2:]+un[1:-1,:-2])
#        u[1:-1,1:-1]+=(-4*Du*dt/dh**2-F*dt)*un[1:-1,1:-1]
#        u[1:-1,1:-1]+=- dt*(vn[1:-1,1:-1])**2*un[1:-1,1:-1]
#        u[1:-1,1:-1]+=F*dt
#u[1:-1,1:-1] = Du*dt/dh**2*(un[2:,1:-1]+un[:-2,1:-1]+un[1:-1,2:]+un[1:-1,:-2])
#       u[1:-1,1:-1] = u[1:-1,1:-1]-4*Du*dt/dh**2*un[1:-1,1:-1]
#        u[1:-1,1:-1] = u[1:-1,1:-1]-un[1:-1,1:-1]*vn[1:-1,1:-1]**2
#        u[1:-1,1:-1] = u[1:-1,1:-1]-F*un[1:-1,1:-1]+F
        ## Neumann boundary with q = 0 at all boundaries
        
        u[-1,:]=u[-2,:]
        u[:,-1]=u[:,-2]
        u[0,:]=u[1,:]
        u[:,0]=u[:,1]

        v[1:-1,1:-1] = vn[1:-1,1:-1]+Dv*dt/dh**2*(vn[2:,1:-1]+vn[:-2,1:-1]+vn[1:-1,2:]+vn[1:-1,:-2]-4*vn[1:-1,1:-1])+dt*un[1:-1,1:-1]*(vn[1:-1,1:-1])**2 -(F+k)*vn[1:-1,1:-1]*dt

#        v[1:-1,1:-1]+=Dv*dt/dh**2*(vn[2:,1:-1]+vn[:-2,1:-1]+vn[1:-1,2:]+vn[1:-1,:-2])
#        v[1:-1,1:-1]+=(-4*Dv*dt/dh**2-(F+k))*vn[1:-1,1:-1]
#        v[1:-1,1:-1]+=dt*un[1:-1,1:-1]*(vn[1:-1,1:-1])**2
                #       v[1:-1,1:-1] = Dv*dt/dh**2*(vn[2:,1:-1]+vn[:-2,1:-1]+vn[1:-1,2:]+vn[1:-1,:-2])
                # v[1:-1,1:-1] = v[1:-1,1:-1]-4*Dv*dt/dh**2*vn[1:-1,1:-1]
                #v[1:-1,1:-1] = v[1:-1,1:-1]+un[1:-1,1:-1]*vn[1:-1,1:-1]**2
                # v[1:-1,1:-1]=v[1:-1,1:-1]-(F+k)*vn[1:-1,1:-1]
        
        v[-1,:]=v[-2,:]
        v[:,-1]=v[:,-2]
        v[0,:]=v[1,:]
        v[:,0]=v[:,1]

    print(u[100,::40])
    return u

uans=ftcs()
plt.figure(figsize=(8,5))
plt.contourf(x,y,uans,20,cmap=cm.viridis)
plt.xlabel('$x_new$')
plt.ylabel('$y_new$')
plt.colorbar();
plt.show()
## end





