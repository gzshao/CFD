import matplotlib.pyplot as plt
import numpy as np

timeStep=0.1  # 1 ms
ms=50
g=9.81
rho=1.091
a=3.14*0.5**2
ve=325
cd=0.15
mp0=100
totalSteps=400

#timeList=np.arange(0,time_step_in_year*(nSteps+1),time_step_in_year).tolist()  # this is an array
steps=np.arange(0,totalSteps,1)
#timeList=np.arange(0,totalTime,timeStep).tolist
timeArray=timeStep*steps
vArray=np.empty(totalSteps)  # should be empty array
hArray=np.empty(totalSteps)    # empty array
massArray=np.empty(totalSteps)    # set the first value
massArray[0]=mp0
vArray[0]=0
hArray[0]=0

for i in steps[1:]:
    if timeArray[i]<=5:
        massArray[i]=massArray[i-1]-20*timeStep
    else:
        massArray[i]=0

#print(massArray)

for i in steps[1:]:
    vArray[i]=vArray[i-1] - g*timeStep + ve*(massArray[i-1]-massArray[i])/(ms+massArray[i-1])- rho*vArray[i-1]*np.absolute(vArray[i-1])*a*cd*timeStep/2/(ms+massArray[i-1])

    hArray[i]=hArray[i-1] + (vArray[i-1])*timeStep

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




