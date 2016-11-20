import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import scipy.interpolate

x = [1885, 1917, 1919, 1932, 1958, 1963, 1968, 1971, 1974, 1978, 1981, 1985, 1988, 1991, 1995, 1999,
     2001, 2002, 2006, 2007, 2008, 2009, 2012, 2013, 2014, 2015, 2016]
y = [2, 3, 2, 3, 4, 5, 6, 8, 10, 15, 19, 22, 25, 29, 32, 33, 34, 37, 39, 41, 42, 44, 45, 46, 49, 49, 47]


xvals = np.arange(1884, 2020, 1)
func = interpolate.splrep(x, y, s=0)
yvals = interpolate.splev(xvals, func, der=0)

for i in range(len(xvals)):
     print "Year: {}".format(xvals[i]) + "\t" "cost: {}".format(yvals[i])

plt.plot(xvals, yvals)
plt.grid(True)
plt.show()

# pp = scipy.interpolate.spltopp(func[0][1:-1],func[1],func[2])
# print(pp.coeffs)
# print func(2016)







# z = np.polyfit(x, y, 3) # the 3 indicates the degree of the fitting polynomial
# p = np.poly1d(z)
# print p(2015.154)
# print p(2017)

# xvalues = np.arange(1885, 2017, 1)
#
# final = map(p, xvalues)
#
#
# plt.plot(xvalues, final)
# plt.grid(True)
# plt.show()



#
# import numpy as np
# from scipy.optimize import curve_fit
# import matplotlib.pyplot as plt
#
# def exponential_fit(x, a, b, c):
#     return a*np.exp(-b*x) + c
#
# if __name__ == "__main__":
#     x = np.array([0, 1, 2, 3, 4, 5])
#     y = np.array([30, 50, 80, 160, 300, 580])
#     fitting_parameters, covariance = curve_fit(exponential_fit, x, y)
#     a, b, c = fitting_parameters
#
#     next_x = 6
#     next_y = exponential_fit(next_x, a, b, c)
#
#     plt.plot(y)
#     plt.plot(np.append(y, next_y), 'ro')
#     plt.show()