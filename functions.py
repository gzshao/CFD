from matplotlib import pyplot
import numpy
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from math import pi

def plot_3D(x, y, p):
    '''Creates 3D plot with appropriate limits and viewing angle
        
        Parameters:
        ----------
        x: array of float
        nodal coordinates in x
        y: array of float
        nodal coordinates in y
        p: 2D array of float
        calculated potential field
        
        '''
    fig = pyplot.figure(figsize=(11,7), dpi=100)
    ax = fig.gca(projection='3d')
    X,Y = numpy.meshgrid(x,y)
    surf = ax.plot_surface(X,Y,p[:], rstride=1, cstride=1, cmap=cm.viridis,linewidth=0, antialiased=False)
        
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$z$')
    ax.view_init(30,45)
    pyplot.show()

def p_analytical(x, y):
    X, Y = numpy.meshgrid(x,y)
    
    p_an = numpy.sinh(1.5*numpy.pi*Y / x[-1]) /\
    (numpy.sinh(1.5*numpy.pi*y[-1]/x[-1]))*numpy.sin(1.5*numpy.pi*X/x[-1])
    
    return p_an

def poisson_IG(nx, ny, xmax, xmin,ymax, ymin):
    dx=(xmax-xmin)/(nx-1)
    dy=(ymax-ymin)/(ny-1)
    x=np.linspace(xmin,xmax,dx)
    y=np.linspace(ymin,ymax,dy)
    X,Y=np.meshgrid(x,y)
    L=xmax-xmin
    b=-2*(pi/L)**2*np.sin(pi*X/L)*np.cos(pi*Y/L)

    p_i=np.zeros(ny,nx)

    return X,Y,x,y,p_i,b,dx,dy,L

#nx = 41
#ny = 41

#x = numpy.linspace(0,1,nx)
#y = numpy.linspace(0,1,ny)

#p_an = p_analytical(x,y)

#plot_3D(x,y,p_an)