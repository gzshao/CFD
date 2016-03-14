import matplotlib.pyplot as plt
import numpy as np

# parameter setup, all in SI unit
timeStep=0.1  # 1 ms
ms=50       # rocket weight on itself without considering fuel
g=9.81      # gravity
rho=1.091   
a=3.14*0.5**2   # drag cross section
ve=325      # propellant leaving velocity
cd=0.15
mp0=100     # initial fuel weight, in Kg
totalSteps=400

# set up the total steps, and repective arrays for time, velocity, mass of propellant and rocket height
steps=np.arange(0,totalSteps,1)
#timeList=np.arange(0,totalTime,timeStep).tolist
timeArray=timeStep*steps
vArray=np.empty(totalSteps)  # should be empty array
hArray=np.empty(totalSteps)    # empty array
massArray=np.empty(totalSteps)    # set the first value
massArray[0]=mp0
vArray[0]=0
hArray[0]=0

# mass of propellant consumed at 20 Kg/s for 5 s, afterwards, it's all gone
for i in steps[1:]:
    if timeArray[i]<=5:
        massArray[i]=massArray[i-1]-20*timeStep
    else:
        massArray[i]=0

# velocty determined by 3 factors
# 1st is the gravity
# 2nd is the pushing force from propellant
# 3rd is the drag, it is v*abs(v) because the drag direction is different depending on whether rocket is going up or falling down
for i in steps[1:]:
    vArray[i]=vArray[i-1] - g*timeStep + ve*(massArray[i-1]-massArray[i])/(ms+massArray[i-1])- rho*vArray[i-1]*np.absolute(vArray[i-1])*a*cd*timeStep/2/(ms+massArray[i-1])

    hArray[i]=hArray[i-1] + (vArray[i-1])*timeStep

# below is for viewing results of max velocity/height with associated time, time when rocket is impacting the ground
print(np.amax(vArray))
print(np.argmax(vArray))
print('height at max velocity',hArray[50])
print(np.where(vArray==100))
print('max height',np.amax(hArray))
print(np.argmax(hArray))
#print(np.where(hArray[1000:]==0))
#plt.plot(timeArray,hArray)
#plt.show()

for i in steps[1:]:
    hArray[i]=np.absolute(hArray[i])

height=hArray[50:]
print(np.argmin(height))
print(np.amin(height))
#print(vArray[37348])




