from __future__ import division
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import math

def function(x):
    y = (1 / (x + 4))
    return y

def funcQuad():
    def f(x):
        y = np.round((1 / (x + 4)), 4)
        return y
    return f

def function2a(x):
    y = math.sin(1/x)
    return y

def function2b(x):
    y = math.cos(1/x)
    return y

def trapezoid(y, x):
    return integrate.trapz(y, x)

def simpson(y, x):
    return integrate.simps(y, x)

def gausianQuadrature(f):
    return integrate.quadrature(f,0,2, maxiter=5) #using a 5 point rule

def plotFunc():
    x = np.arange(0.1, 2, 0.01)
    y = np.sin(1/x)
    y2 = np.cos(1/x)
    plt.plot(x, y, 'r', label='sin(1/x)')
    plt.plot(x, y2, label='cos(1/x)')
    plt.legend()
    plt.grid(True)
    plt.show()


def adaptiveQuad2a():
    return integrate.quad(function2a, 0.1, 2, limit=4) #limit= is the number of subintervals used
                                                    # epsrl= is error tolerance(not used here)
def adaptiveQuad2b():
    return integrate.quad(function2b, 0.1, 2, limit=4) #limit= is the number of subintervals used

def main():
    xp = np.linspace(0,2,20) #20 intervals
    ylist = []
    for x in xp:
        ylist.append(round(function(x), 4))

    # print "The actual value of the Integral f(x) = 1 / x+4 from 0 to 2 = 0.40547"
    # print "APPROXIMATION with n = 20 intervals:"
    # print "Trapezoid Rule: {}".format(trapezoid(ylist, xp))
    # print "Simpson's Rule: {}".format(simpson(ylist, xp))
    #
    # func = funcQuad()
    # print "APPROXIMATION with 5-point rule (intervals):"
    # print "Gausian Quadrature: {}".format(gausianQuadrature(func))

    plotFunc()
    print "Actual value for Integral of sin(1/x) from 0.1 to 2 = 1.14558"
    print "Adaptive Quadrature: Integral( sin(1/x) ) = {}".format(adaptiveQuad2a())
    print "Actual value for Integral of cos(1/x) from 0.1 to 2 = 0.673832"
    print "Adaptive Quadrature: Integral( cos(1/x) ) = {}".format(adaptiveQuad2b())


if __name__ == '__main__':
    main ()