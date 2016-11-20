from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def FindDD(x,y, delta):
    Fx = []
    for i in range(len(y)):
        # print "x[delta]: {}".format(x[delta])
        # print "x[i]: {}".format(x[i])
        tempy = ((y[i+1] - y[i]) / (x[delta] - x[i]))
        Fx.append(tempy)
        delta += 1
        if delta >= len(x):
            break;

    return Fx


def result(x, xpoint, i):
    xvalue = 1.0
    j = 0
    while (j <= i):
        xvalue = xvalue * (xpoint - x[j])
        j+=1
    return xvalue


def computeNewtonsDDF(DDifference, x, y):
    def N(xpoint):
        NewtonsDDF = 0
        for i in range(len(DDifference)):
            NewtonsDDF+= (DDifference[i] * result(x, xpoint, i))
        return NewtonsDDF + y[0]
    return N


def plotNewton(y, start, end, grapingPoints):
    x = np.linspace(start, end, grapingPoints )
    plt.grid(True)
    plt.plot(x,y, linewidth=2)
    plt.show()


def setDataPoints(Xpoints, Ypoints, Xrange, SIZE):
    DDifference = []
    allOrderDifferences = []
    yy = Ypoints
    for j in range(SIZE - 1):
        yy = FindDD(Xpoints, yy, j + 1)
        allOrderDifferences = allOrderDifferences + yy  # send j + 1 so that (xi+1 - xi) is accurate
        DDifference.append(yy[0])

    N = computeNewtonsDDF(DDifference, Xpoints, Ypoints)  # N is Newtons divided difference formula
    y = map(N, Xrange) #change to Xrange or xPoints

    for i in range(len(Xrange)):
        print "Year: {}".format(Xrange[i]) + "\t" + "cost: {}".format(y[i])

    # graphPoints = len(Xpoints) #change to Xrange
    # start = Xpoints[0]
    # end = Xpoints[-1]
    # plotNewton(y, start, end, graphPoints)


def main():
    xRange = np.arange(1885,2020,1)
    Xpoints = [1885, 1917, 1919, 1932, 1958, 1963, 1968, 1971, 1974, 1978, 1981, 1985, 1988, 1991, 1995, 1999,
               2001, 2002, 2006, 2007, 2008, 2009, 2012, 2013, 2014, 2015, 2016]
    Ypoints = [2, 3, 2, 3, 4, 5, 6, 8, 10, 15, 19, 22, 25, 29, 32, 33, 34, 37, 39, 41, 42, 44, 45, 46, 49, 49, 47]

    SIZE = len(Xpoints)

    #print xRange

    setDataPoints(Xpoints, Ypoints, xRange, SIZE)

if __name__ == '__main__':
    main()



# SIZE = 5
# TEST CODE
# x = [0.0, 1.0, 2.0, 3.0, 4.0]
# y = [0.0, 1.0, 8.0, 27.0, 64.0]
#
# DDifference = []
# allOrderDifferences = []
# yy = y
# for j in range(SIZE - 1):
#     yy = FindDD(x,yy, j+1 )
#     allOrderDifferences = allOrderDifferences + yy #send j + 1 for xi+1 - xi is accurate
#     DDifference.append(yy[0])
#
# N = computeNewtonsDDF(DDifference, x, y) #N is Newtons divided difference formula

# xpoint = 2.5
# y = map(N, xpoint)
# print y












#print "main it : {}".format(i)


# print "i: {}".format(i)
# print "j: {}".format(j)
# print "xpoint: {}".format(xpoint)
# print "x[]: {}".format(x[j])
# print "xvalue: {}".format(xvalue)
# print "\n"


# def calc_Xi_minus_Xiplus1(x, xpoint):
#     for i in range(len(x)):
#         result = x[i]



# NewtonsDDF = (
#   DDifference[0]*(x-X[0])
# + DDifference[1]*(x-X[0])*(x-X[1])
# + DDifference[2]*(x-X[0])*(x-X[1])*(x-X[2])
# + DDifference[3]*(x-X[0])*(x-X[1])*(x-X[2])*(x-X[3])
# + DDifference[4]*(x-X[0])*(x-X[1])*(x-X[2])*(x-X[3])*(x-X[4]) )





# def updateFX(xx, yy, oldFx):
#     #yy.remove(yy[0])
#     #xx.remove(xx[1])
#     newFx = []
#
#     for i in range(len(xx)-1): #may cause index out of range
#         newFx.append((xx[i], oldFx[i]))
#         yy[i] = oldFx[i]
#         i += 1
#     return newFx








#
# #x = 1.5 # We choose an x within the range 0 <= x <= 2
# interpolationApproximation = computeNewtonsDDF(DDifference, x)
#
#
# print "Interpolation Approximation = ", interpolationApproximation
#
# print "\n\n"
# print DDifference




# print "xx: ", xx
# print "yy: ", yy




# Finally compute f(x) = e^x * sin(x) at x = 1
# fx_ = math.exp(x) * math.sin(x)
# We compare both results and ensure that the interpolation is accurate to
#   four decimal places
# print "f(x) =  ", fx_






# xx = [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0] #The x values chosen


# The y values obtained by plugging x into the equation
# yy = [0.0, math.exp(1.0)*math.sin(1.0), math.exp(2.0)*math.sin(2.0)]

# yy = [0.0, math.exp(0.25)*math.sin(0.25), math.exp(0.5)*math.sin(0.5), math.exp(0.75)*math.sin(0.75), math.exp(1.0)*math.sin(1.0),
# math.exp(1.25)*math.sin(1.25), math.exp(1.5)*math.sin(1.5), math.exp(1.75)*math.sin(1.75), math.exp(2.0)*math.sin(2.0)]


# xyValues = [ (0.0, 0.0), (0.25, math.exp(0.25)*math.sin(0.25)), (0.5, math.exp(0.5)*math.sin(0.5)),
# (0.75, math.exp(0.75)*math.sin(0.75)), (1.0, math.exp(1.0)*math.sin(1.0)), (1.25, math.exp(1.25)*math.sin(1.25)), (1.5, math.exp(1.5)*math.sin(1.5)),
# (1.75, math.exp(1.75)*math.sin(1.75)), (2.0, math.exp(2.0)*math.sin(2.0)) ]



# print "xx: ", xx
# print "yy: ", yy
# print "xyValues:",  xyValues
# print " "
# result = interpolation(xx,yy,xyValues)
# print "xx: ", xx
# print "yy: ", yy
# print result
# print " "
# result2 = interpolation(xx,yy,result)
# print "xx: ", xx
# print "yy: ", yy
# print result2
# print " "
# result3 = interpolation(xx,yy,result2)
# print "xx: ", xx
# print "yy: ", yy
# print result3
# print " "
# result4 = interpolation(xx,yy,result3)
# print "xx: ", xx
# print "yy: ", yy
# print result4


# WORKS
# xx = [0.0, 1.0, 2.0]
# yy = [0.0, math.exp(1)*math.sin(1), math.exp(2)*math.sin(2) ]
#
# xyValues = [ (0.0, 0.0), (1.0, math.exp(1)*math.sin(1)), (2.0, math.exp(2)*math.sin(2)) ]
##

#WORKS
# xx = [0.0 , 2.0, 3.0]
# yy = [1.0, 2.0, 4.0]
# xyValues = [ (0.0, 1.0), (2.0,2.0), (3.0, 4.0) ]
##

    # + DDifference[2]*(x-X[0])*(x-X[1])*(x-X[2])
    # + DDifference[3]*(x-X[0])*(x-X[1])*(x-X[2])*(x-X[3])
    # + DDifference[4]*(x-X[0])*(x-X[1])*(x-X[2])*(x-X[3])*(x-X[4])
    # + DDifference[5]*(x-X[0])*(x-X[1])*(x-X[2])*(x-X[3])*(x-X[4])*(x-X[5])
    # + DDifference[6]*(x-X[0])*(x-X[1])*(x-X[2])*(x-X[3])*(x-X[4])*(x-X[5])*(x-X[6])
    # + DDifference[7]*(x-X[0])*(x-X[1])*(x-X[2])*(x-X[3])*(x-X[4])*(x-X[5])*(x-X[6])*(x-X[7])



# xx = [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0] #The x values chosen
    # #The y values obtained by plugging x into the equation
    # yy = [0.0, math.exp(0.25)*math.sin(0.25), math.exp(0.5)*math.sin(0.5),
    # math.exp(0.75)*math.sin(0.75), math.exp(1.0)*math.sin(1.0), math.exp(1.25)*math.sin(1.25),
    # math.exp(1.5)*math.sin(1.5), math.exp(1.75)*math.sin(1.75), math.exp(2.0)*math.sin(2.0)]
    # # My x and y values in a list of tuples
    # xyValues = ( (0.0, 0.0), (0.25, math.exp(0.25)*math.sin(0.25)),
    # (0.5, math.exp(0.5)*math.sin(0.5)), (0.75, math.exp(0.75)*math.sin(0.75)),
    # (1.0, math.exp(1)*math.sin(1)), (1.25, math.exp(1.25)*math.sin(1.25)),
    # (1.5, math.exp(1.5)*math.sin(1.5)), (1.75, math.exp(1.75)*math.sin(1.75)),
    # (2.0, math.exp(2)*math.sin(2)) )
