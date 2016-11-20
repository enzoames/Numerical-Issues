import numpy as np
import matplotlib.pyplot as plt


def plotSplines(y, start, end):
    x = np.linspace(start, end, 400)
    plt.axis([0, 7, 0, 9])
    plt.plot(x, y, linewidth=2)
    plt.grid(True)
    plt.show()

def setDataPoints(xValues, yValues):
    listY = []
    for i in range(2):
        x = np.linspace(xValues[i], xValues[i+1], 100)
        S = spline(xValues, yValues,i)
        y = map(S, x)
        listY = listY + y
    return listY

def spline(xValues, yValues, ii):
    def S(x):
        deltaX = []
        deltaY = []

        for i in range(len(xValues) - 1):
            deltaX.append(xValues[i+1] - xValues[i])
            deltaY.append(yValues[i+1] - yValues[i])

        Ci = calculateCi(deltaX, deltaY)
        Ai = calculateAi(yValues)
        Bi = calculateBi(deltaX, deltaY, Ci)
        Di = calculateDi(Ci, deltaX)
        Sx = (Ai[ii] + Bi[ii] * (x - xValues[ii]) + (Ci[ii] * (x - xValues[ii]) ** 2) + (Di[ii] * (x - xValues[ii]) ** 3))

        return Sx
    return S

def calculateAi(yValues):
    tempAi = []
    for i in range(len(yValues)-1):
        tempAi.append(yValues[i])
    return tempAi

def calculateBi(deltaX, deltaY, Ci):
    tempBi = []
    for i in range(len(Ci)-1):
        tempBi.append( ((deltaY[i] / deltaX[i]) - (deltaX[i] * (2 * Ci[i] + Ci[i+1])) / 3) )
    return tempBi

def calculateCi(deltaX, deltaY):
    tempCi = []
    tempCi.append(0) # The first value for C0 is 0
    i = 0 #because C0 = 0

    while(i<len(deltaX)-1):
        temp = ((3 * ((deltaY[i+1] / deltaX[i+1]) - (deltaY[i] / deltaX[i]))) / (2 * (deltaX[i] + deltaX[i+1])))
        tempCi.append(temp)
        i+=1

    tempCi.append(0) # Cn = 0
    return tempCi

def calculateDi(Ci, deltaX):
    tempDi=[]
    for i in range(len(Ci)-1):
        tempDi.append(((Ci[i+1] - Ci[i])/(3*deltaX[i])))
    return tempDi

def main():
    finalYdata = []

    xValues = [ [1, 2, 3], [3, 4, 5] ]
    yValues = [ [6, 7, 1], [1, 8, 7] ]

    for i in range(2):
        finalYdata += setDataPoints(xValues[i], yValues[i])

    plotSplines(finalYdata, xValues[0][0], xValues[1][2])

if __name__ == '__main__':
    main()









        # xValues = [1, 2, 3]
        # yValues = [6, 7, 3]
        #
        # xValues1 = [3, 4, 5]
        # yValues1 = [3, 1, 4]
        #
        # xValues2 = [5, 6, 7]
        # yValues2 = [4, 6, 8]



        # print "xValues[{}]".format(i)
        # print xValues[i]
        # print "yValues[{}]".format(i)
        # print yValues[i]

    # print "finalYdata: "
    # print finalYdata

    # i = 0
    #
    #
    # for i in range(2):
    #     x = np.linspace(xValues[i], xValues[i+1], 100)
    #     S = spline(xValues, yValues,i)
    #     y = map(S, x)
    #     listY = listY + y
    #
    # xx = np.linspace(xValues[0], xValues[2], 200) #this should go from xValues[0] - xValues[]
    # plt.grid(True)
    # plt.axis([0,5,0,9])
    # plt.plot(xx, listY)
    # plt.show()













        # x = np.linspace(1, 2, 200)
# i = 0
# xx = []
# yy = []

# for i in range(len(xValues)-2):
#     S = spline(xValues, yValues)
#     x = np.linspace(xValues[i], xValues[i+1], 50)
#     yy = yy + plotSpline(S, x)
#     xx.append(x)



# x = np.linspace(xValues[i], xValues[i + 1], 200)
# y = evalualte_S(S, x)
# xx.append(x)

    # print "S(x): {}".format(S(1))











    # def evalualte_S(S, x):
    #     y = map(S, x)
    #     result = []
    #     result.append(y)
    #     return result
    #
    # def plotSplines(x, y):
    #     plt.plot(x, y, linewidth=2)
    #     plt.show()












    # print "Ai: {}".format(Ai)
    # print "Bi: {}".format(Bi)
    # print "Ci: {}".format(Ci)
    # print "Di: {}".format(Di)

    # c2 = 0
    # c1 = calculateCi(deltaX[0], deltaX[1], deltaY[0], deltaY[1])
    # a1 = yValues[1]
    # b1 = ( (deltaY[1] / deltaX[1]) - (deltaX[1]* (2*c1 + c2))/3 )
    # d1 = ( (c2 - c1)/(3*deltaX[1]) )
    #
    # c0 = 0
    # a0  = yValues[0]
    # b0 = ( (deltaY[0] / deltaX[0]) - (deltaX[0] * (2*c0 + c1))/3 )
    # d0 = ( (c1 - c0)/(3*deltaX[0]) )
    #
    # Sx_0 = (a0 + b0*(x-xValues[0]) + (c0 * (x - xValues[0]) ** 2) + (d0 * (x - xValues[0]) ** 3))




    # print "c1: {}".format(c1)


    # print "a0: {}".format(a0)
    # print "b0: {}".format(b0)
    # print "c0: {}".format(c0)
    # print "d0: {}".format(d0)
    # print "delta X: "
    # print deltaX
    # print "delta Y:"
    # print deltaY




    # X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    # C, S = np.cos(X), np.sin(X)
    #
    # plt.plot(X, C)
    # plt.plot(X, S)
    #
    # plt.show()


    # x = np.linspace(-2, 2, 200)
    #
    # y = (x ** 5 + 4 * x ** 4 + 3 * x ** 3 + 2 * x ** 2 + x + 1) #* np.exp(-x ** 2)
    #
    # # plt.figure()  # Make a new figure
    #
    # plt.plot(x, y)  # Plot some data
    #
    # plt.show()


    # Manually calculate the value for all the Ci , Ci+1 , .. Cn
    # temp = ((3 * ((deltaY[1] / deltaX[1]) - (deltaY[0] / deltaX[0]))))
    #
    # tempCi.append(temp )
    #
    # temp = ((3 * ((deltaY[2] / deltaX[2]) - (deltaY[1] / deltaX[1]))))
    #
    # tempCi.append(temp)
    #
    # tempCi[2] = ((tempCi[2] - tempCi[1]/4)*(4/15))
    # tempCi[1] = (tempCi[1]*(1/4) - ((1/4)*(tempCi[2] - tempCi[1]/4)*(4/15)))







    # i = 0 #because C0 = 0
    # while(i<len(deltaX)-2):
    #     temp = ((3 * ((deltaY[i+1] / deltaX[i+1]) - (deltaY[i] / deltaX[i]))) / (2 * (deltaX[i] + deltaX[i+1])))
    #     tempCi.append(temp)
    #     i+=1
    # tempCi.append(0) #the last value for Cn is 0