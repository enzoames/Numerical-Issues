import matplotlib.pyplot as plt
import numpy as np
import math

def FindDD(xx,yy,xyValues):
    oldFx = []
    newYY = []
    i = 1
    for x,y in xyValues:
        tempy = yy[i] - y
        tempy = tempy / (xx[i] - x)
        oldFx.append(tempy)
        i+=1
        if(i >= len(xx) ):
            break;
    return updateFX(xx, yy, oldFx)

def updateFX(xx, yy, oldFx):
    yy.remove(yy[0])
    xx.remove(xx[1])
    newFx = []
    i=0
    for i in range(len(xx)):
        newFx.append((xx[i], oldFx[i]))
        yy[i] = oldFx[i]
        i+=1
    return newFx

def computeNewtonsDDF(DDifference, x):
    X = [1.5, 2.0, 3.0]
    Y = [2.98]
    NewtonsDDF = Y[0] + DDifference[0]*(x-X[0]) + DDifference[1]*(x-X[0])*(x-X[1])
    return NewtonsDDF

def createPlot():
    x = [0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 3.5, 4.0]
    y = [1.90, 2.39, 2.71, 2.98, 3.20, 3.20, 2.98, 2.74]
    plt.xlabel("Position in apparatus")
    plt.ylabel("Dosage")
    plt.axis([0,4,0,4])
    plt.plot(x,y, 'rx')
    plt.grid(True)
    plt.show()

def main():
    SIZE = 3
    xx = [1.5, 2.0, 3.0]
    yy = [2.98, 3.20, 3.20]
    xyValues = [ (1.5, 2.98), (2.0, 3.20), (3.0, 3.20) ]

    DDifference = []
    for j in range(SIZE - 1):
        print "xx: ", xx
        print "yy: ", yy
        xyValues = FindDD(xx,yy,xyValues)
        DDifference.append(yy[0])
        print "iteration {}:".format(j+1) , xyValues
        print " "

    x = 2.5 #find the approximation at x = 2.5
    interpolationApproximation = computeNewtonsDDF(DDifference, x)
    print "Interpolation Approximation = ", interpolationApproximation
    # createPlot()

if __name__ == '__main__':
    main()
