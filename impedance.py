import sympy
import numpy as np
import cmath
from sympy import re, im, I
from sympy.utilities.lambdify import lambdify
import matplotlib.pyplot as plt
# calculate the real and imaginary part of the impedance near electrode in a solution
# the physical model can be found at Gamry website describing resistance, capacitance and Warburg impedance
# the model is Rs -- (Cd||Rp--W)
# website: http://www.gamry.com/application-notes/EIS/basics-of-electrochemical-impedance-spectroscopy/

sigma = 1.
delta = 1e-8
D = 5e-10

rs=20.
rp=450.
cd=40e-3

#rs = sympy.symbols('rs')
#cd = sympy.symbols('cd')
#rp = sympy.symbols('rp')
#w = sympy.symbols('w')
omega = sympy.symbols('omega')

# finite Warburg impedance
#w = sigma*omega**(-1/2)*(1-I)*cmath.tanh(delta*(I*omega/D)**(1/2))

# infinite Warburg impedance
w = sigma*omega**(-1/2)*(1-I)

impedance = rs + 1/(1/(rp+w)+I*omega*cd)
#impedance = rs + 1/(1/rp+I*omega*cd)

#print(impedance)


result = lambdify(omega,impedance)
#print(im(result(rsV,rpV,wV,cdV)))

xAxis=np.empty(40)
yAxis=np.empty(40)

freq = np.logspace(5,-5,50)
#print(freq)
#print(result(1000))

for n in range(40):
    yAxis[n] = im(result(freq[n]))
    xAxis[n] = re(result(freq[n]))

#print(freq[:5])
#print(xAxis[:5])
#print(yAxis[:5])
plt.plot(xAxis,yAxis)
plt.gca().invert_yaxis()
plt.show()

