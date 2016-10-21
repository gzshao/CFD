import sympy
import numpy as np
from numpy import pi
import cmath
from sympy import re, im, I
from sympy.utilities.lambdify import lambdify
import matplotlib.pyplot as plt

#Fourier Transform

n = 1000
#noise = np.random.random(n)
#count = np.arange(1024)
count=np.arange(0,1,1.0/1300)
print(count.shape[0])
signal = np.sin(2*20*pi*count)
s= signal #+noise
#signal = np.sin()
'''
x = np.arange(n)

# Forward Discrete Fourier Transform (DFT)
Fvector = -2*1j*pi/n*np.arange(n)
#freq = np.empty(n)

#print(Fvector[:5])
#print(freq[:5])

#for k in range(200):
freq= np.exp(Fvector[:]*np.arange(n))*x[:]
#freq[0] = np.exp(Fvector[:]*0)*x[:]

result=np.fft.fft(s)
#print(freq[0])
print(len(freq))
print(np.allclose(freq[:],np.fft.fft(s)))

'''
def DFT_slow(x):
    """Compute the discrete Fourier Transform of the 1D array x"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    #n = np.arange(N)  # n = np.arange(1,N+1,1)   # from 1 to N, rather than from 0 to N-1
    n = np.arange(1,N+1,1)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    y = np.exp(x)
    return np.dot(M, y)


xp=DFT_slow(s)
x=np.absolute(xp)
#x=np.real(xp)

#print(np.allclose(x,np.fft.fft(s)))
#print(s[:10])

#plt.subplot(211)
#plt.plot(s)
#plt.subplot(212)
#plt.xlim(-10,1000)
#plt.plot(x)
#plt.ylim(-5,5)
#plt.plot(x,'g^',s,'r--')
plt.plot(x)
plt.show()
