import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16


#### my homework function #####

# convention of symbols:
# u10, u20 and u30, f10, f20 andf30 means initial conditions
# u1, u2 and u3, f1, f2 and f3 are calculated values at t>0
# u_gap, f1_gap, f2_gap, f3_gap are for u and f values between integer points as defined in the Richtmyer equations
############################################

nx = 81
nt = 50
dx = 0.25
dt = 0.0002
rho_L = 1
rho_R = 0.125
u_L = 0
u_R = 0
p_L = 100000
p_R= 10000
gamma=1.4

# density
def rho(nx,rho_L,rho_R):
    rho = rho_R*np.ones(nx)
    rho[:int((nx-1)*1./2.)] = rho_L
    return rho

# velocity
def u(nx,u_L,u_R):
    u = u_R*np.ones(nx)
    u[:int((nx-1)*1./2.)] = u_L
    return u

# pressure
def p(nx,p_L,p_R):
    p = p_R*np.ones(nx)
    p[:int((nx-1)*1./2.)] = p_L
    return p

x = np.linspace(-10,10,nx)

# this step is to convert from rho, velocity and pressure to u10, u20, u30

u10 = rho(nx,rho_L, rho_R)
u20 = u(nx, u_L, u_R)*u10
u30 = p(nx, p_L, p_R)/(gamma-1) + 1/2./u10*u20**2

plt.plot(x, u10, color='#003366', ls='-', lw=3)
plt.plot(x, u20, color='#003366', ls='-', lw=3)
plt.plot(x, u30, color='#003366', ls='-', lw=3)
plt.ylabel('Initial condition')
plt.xlabel('Distance')
#plt.ylim(-0.5,11.)
plt.show()

u1=np.zeros((nt+1,nx))
u2=np.zeros((nt+1,nx))
u3=np.zeros((nt+1,nx))

def u_gap(u,f,dt,dx):
    # of dimension len(u1)-1
    # u is known u
    # f is known f
    return 1/2.*(u[1:]+u[:-1]) - dt/dx/2.*(f[1:]-f[:-1])   # this should be minus rather than plus

def f1(u2):
    return u2[:]

def f2(u1,u2,u3):
    return u2[:]**2/u1[:]+(gamma-1.)*(u3[:]-1/2.*u2[:]**2/u1[:])

def f3(u1,u2,u3):
    return (u3[:]+(gamma-1)*(u3[:]-1./2.*u2[:]**2/u1[:]))*u2[:]/u1[:]

def whole(u10,u20,u30,dt,dx):
    # f10, f20, f30 mean f1, f2, f3 at interger time step
    # f1gap, f2gap, f3gap mean f1, f2, f3 at half time step
    
    # firstly, calculate f from known u
    # secondly, calculate u_gap from known f and known u
    # thirdly, calculate f_gap from known u_gap
    # lastly, calculate u of next time step from known u and f_gap
    #u10=
    #u20=
    #u30=
    for t in range(1,nt+1):
        
        
        f10=f1(u20)
        f20=f2(u10,u20,u30)
        f30=f3(u10,u20,u30)
    
        u1_gap=u_gap(u10,f10,dt,dx)
        u2_gap=u_gap(u20,f20,dt,dx)
        u3_gap=u_gap(u30,f30,dt,dx)
    
        f1_gap=f1(u2_gap)
        f2_gap=f2(u1_gap,u2_gap,u3_gap)
        f3_gap=f3(u1_gap,u2_gap,u3_gap)

        u1[t,1:-1]=u10[1:-1]-dt/dx*(f1_gap[1:]-f1_gap[:-1])
        u1[t,0]=rho_L
        u1[t,-1]=rho_R

        u2[t,1:-1]=u20[1:-1]-dt/dx*(f2_gap[1:]-f2_gap[:-1])
        u2[t,0]=u_L*rho_L
        u2[t,-1]=u_R*rho_R
        
#        u20 = u(nx, u_L, u_R)*u10
#        u30 = p(nx, p_L, p_R)/(gamma-1) + 1/2./u10*u20**2

        u3[t,1:-1]=u30[1:-1]-dt/dx*(f3_gap[1:]-f3_gap[:-1])
        u3[t,0]=p_L/(gamma-1)+1./2./rho_L*u_L**2
        u3[t,-1]=p_R/(gamma-1)+1./2./rho_R*u_R**2

        u10=u1[t,:].copy()
        u20=u2[t,:].copy()
        u30=u3[t,:].copy()
    
    import csv
    with open('pressure.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(u3)
    print('pressure at 2.5m is:')
    print (1.4-1.0)*(u30[50]-1./2.*u20[50]**2/u10[50])

    print(u10[50])
    print(u20[50])
    print(u30[50])

    return u30
    #return 3D matrix containing u1[:,:], u2[:,:] and u3[:,:]

# need to convert u10, u20, u30 back to rho, u and p
xyz=whole(u10,u20,u30,dt,dx)
plt.plot(x, xyz, color='#003366', ls='-', lw=3)
plt.ylabel('Pipe pressure')
plt.xlabel('Distance')
plt.show()

#from matplotlib import animation
#from JSAnimation.IPython_display import display_animation
#from JSAnimation import HTMLWriter

#def init():
#    line.set_data([], [])
#    return line,

#def animate(data):
#    x = np.linspace(0,4,nx)
#    y = data
#    line.set_data(x,y)
#    return line,


############



