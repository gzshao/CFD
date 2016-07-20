import sympy
import numpy as np
from numpy import pi
import cmath
from sympy import re, im, I
from sympy.utilities.lambdify import lambdify
import matplotlib.pyplot as plt

# Fast Fourier Transform

n = 1024
s = np.random.random(n)
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
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


x=DFT_slow(s)


print(np.allclose(x,np.fft.fft(s)))
print(x[:5])

#plt.subplot(211)
#plt.plot(s)
#plt.subplot(212)
#plt.xlim(-10,1000)
#plt.plot(x)
plt.ylim(-500,500)
plt.plot(x,'g^',s,'r--')
plt.show()
