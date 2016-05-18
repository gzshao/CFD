import numpy as np
import numba
from numba import jit
import matplotlib.pyplot as plt
from matplotlib import rcParams, cm
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16
from functions import plot_3D

## For relaxing homework
# check boundary condition for omega and psi

nx = 41
ny = 41

l=1.
h=1.

dx=l/(nx-1)
dy=h/(ny-1)

x=np.linspace(0,l,nx)
y=np.linspace(0,h,ny)

l1_target=1e-8
l2_target=1e-6

omega=np.zeros((ny,nx))
psi=np.zeros((ny,nx))

#psi[1:-1,-2]=-dy
#p0[-1,:]=1

def L1norm(new, old):
    norm=np.sum(np.abs(new-old))
    return norm

def laplace2d(p, l1_target):
    l1_norm=1
    pn=np.empty_like(p)
    iterations=0

    while l1_norm>l1_target:
        pn=p.copy()
        p[1:-1,1:-1]=.25*(pn[1:-1,2:]+pn[1:-1,:-2]+pn[2:,1:-1]+pn[:-2,1:-1])

        # 2nd order Neumann B.C. along x=L
        p[1:-1,-1]=.25*(2*pn[1:-1,-2]+pn[2:,-1]+pn[:-2,-1])

        l1_norm=np.sqrt(np.sum((p-pn)**2)/np.sum(pn**2))   # do not divide by zero
        iterations +=1

    return p,iterations

def poisson_2d(p, b, dx, dy, l2_target):
    l2_norm = 1
    iterations = 0
    l2_conv = []
    
    while l2_norm > l2_target:
        
        pd = p.copy()
        
        p[1:-1,1:-1] = 1/(2*(dx**2 + dy**2)) * \
            ((pd[1:-1,2:]+pd[1:-1,:-2])*dy**2 +\
             (pd[2:,1:-1] + pd[:-2,1:-1])*dx**2 -\
             b[1:-1,1:-1]*dx**2*dy**2)
        
        # BCs are automatically enforced
        p[:,-1]=p[:,-2]+dy  # 1st order Neumann B.C.
        # 2nd order Neumann B.C.
        p[1:-1,-1]=1/(2*(dx**2 + dy**2)) * \
            ((2*pd[1:-1,-2]+2*dy)*dy**2 +\
             (pd[2:,-1] + pd[:-2,-1])*dx**2 -\
             b[1:-1,1:-1]*dx**2*dy**2)
        
        l2_norm = L2_rel_error(pd,p)
        iterations += 1
        l2_conv.append(l2_norm)
    
    print('Number of Jacobi iterations: {0:d}'.format(iterations))
    return p, l2_conv

def coupled():
    l1_norm=1
    l2_norm=1
    iterations=0
    
    # converges too slow, need to use JIT
    while (l2_norm > l1_target or l1_norm>l1_target):
        omegaOld = omega.copy()
        psiOld = psi.copy()

        omega[1:-1,1:-1]=.25*(omegaOld[1:-1,2:]+omegaOld[1:-1,:-2]+omegaOld[2:,1:-1]+omegaOld[:-2,1:-1])
        psi[1:-1,1:-1] = 1./(2*(dx**2+dy**2))*((psiOld[1:-1,2:]+psiOld[1:-1,:-2])*dy**2+\
            (psiOld[2:,1:-1]+psiOld[:-2,1:-1])*dx**2+omega[1:-1,1:-1]*dx**2*dy**2)
            #psi[1:-1,1:-2] = 1./(2*(dx**2+dy**2))*((psiOld[2:,1:-2]+psiOld[:-2,1:-2])*dy**2+(psiOld[1:-1,2:-1]+psiOld[1:-1,:-3])*dx**2+omegaOld[1:-1,1:-2]*dx**2*dy**2)
        
        # now set the boundary condition at the y=H, according to the Notebook
        #omega[1:-1,-1]=-(8*psi[1:-1,-2]-psi[1:-1,-3])/2/dy**2-3./dy
        omega[1:-1,-1]=-(8*psiOld[1:-1,-2]-psiOld[1:-1,-3])/2/dy**2-3./dy
        omega[1:-1,0]=-(8*psiOld[1:-1,1]-psiOld[1:-1,2])/2/dy**2
        omega[-1,1:-1]=-(8*psiOld[-2,1:-1]-psiOld[-3,1:-1])/2/dy**2
        omega[0,1:-1]=-(8*psiOld[1,1:-1]-psiOld[2,1:-1])/2/dy**2
        # 2nd order Neumann B.C., note that in that last item on the right, it is [+omega...] not [-omega ...]
        
        # top surface
        #psi[1:-1,-2]=-dy
        #psi[1:-1,-1] =1./(2*(dx**2 + dy**2)) *((psiOld[:-2,-1]+psiOld[2:,-1])*dy**2+(2*psiOld[1:-1,-2]+2*dy)*dx**2+omega[1:-1,-1]*dx**2*dy**2)
        # bottom surface
        #psi[1:-1,0] =1/(2*(dx**2 + dy**2)) *((psiOld[:-2,0]+psiOld[2:,0])*dy**2+(2*psiOld[1:-1,1])*dx**2+omega[1:-1,0]*dx**2*dy**2)
        # right surface
        #psi[-1,1:-1] =1/(2*(dx**2 + dy**2)) *((2*psiOld[-2,1:-1])*dy**2+(psiOld[-1,:-2]+psiOld[-1,2:])*dx**2+omega[-1,1:-1]*dx**2*dy**2)
        # left surface
        #psi[0,1:-1] =1/(2*(dx**2 + dy**2)) *((2*psiOld[1,1:-1])*dy**2+(psiOld[0,:-2]+psiOld[0,2:])*dx**2+omega[0,1:-1]*dx**2*dy**2)
        # 1st order Neumann B.C.
        #psi[1:-1,-1] = psi[1:-1,-2]+dy

        #l1_norm=np.sqrt(np.sum((omega-omegaOld)**2)/np.sum(omegaOld**2))   # do not divide by zero
        #l2_norm=np.sqrt(np.sum((psi-psiOld)**2)/np.sum(psiOld**2))
        l1_norm=L1norm(omega,omegaOld)
        l2_norm=L1norm(psi,psiOld)
        iterations +=1
        if(iterations==50000):
            break

    return psi, omega, iterations


#p, iterations = laplace2d(p0.copy(),l1_target)
psi, omega, iterations=coupled();

plot_3D(x,y,psi)

#plot_3D(x,y,omega)
print(iterations)
print(np.amax(psi))
print(np.amin(psi))
print(np.amax(omega))
print(np.amin(omega))

print(np.round(psi[32,::8], 4))
print(np.round(psi[::8,32], 4))







