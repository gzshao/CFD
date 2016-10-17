# function randomWalk(totalStep) is the function to be called by main() or main2()
# main() is used to estimate the error as the steps increase, say if I take 100 random walks, the error would be much larger than if I take 10000 random walks

# main2() is to estimate the error of size=1000 in different instances. If I take only one random walk with size=1000, there might be 515 steps to the right and 485 steps to the left. However, in the next walk, it might be 504 to the right and 496 to the right. main2() is used to display the difference between different walks.

from random import randint
import matplotlib.pyplot as plt
import numpy as np

def randomWalk(totalStep):
    sum=0
    #totalStep=10000
    #current=randint(0,1)
    #sum=1-2*current
    stepArray=np.empty(totalStep)
    distanceArray=np.empty(totalStep)
    choiceArray=np.empty(totalStep)
    count=1
    positiveCount=0.0

    while count<totalStep:
        currentChoice=randint(0,1)
        stepArray[count]=count
        distanceArray[count]=distanceArray[count-1]+(1-2*currentChoice)
        choiceArray[count]=currentChoice
        count+=1
        if currentChoice==1:
            positiveCount+=1

    return positiveCount
    #print("Positive count=")
    #print(positiveCount)
    #plt.plot(stepArray,distanceArray)
    #plt.plot(stepArray,choiceArray)
    #plt.show()

def main():
    sizeArray=np.empty(5)
    errorArray=np.empty(5)
    i=0
    sizeArray=[100,1000,10000,100000,1000000]
    for k in sizeArray:
        error=randomWalk(k)
        #print(error)
        errorArray[i]=abs(error-k/2)/k
        i+=1
    plt.plot(sizeArray,errorArray)
    plt.xscale('log')
    plt.show()

def main2():
    size=5000
    countArray=np.empty(size)
    errorArray=np.empty(size)
    for i in range(size):
        countArray[i]=i
        error=randomWalk(1000)
        errorArray[i]=(error-500)/1000
    #plt.plot(countArray,errorArray)
    plt.hist(errorArray,bins=100)
    plt.show()

if __name__=='__main__':
    main2()