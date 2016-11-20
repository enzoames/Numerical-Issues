import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

x = [1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960,
     1970, 1980, 1990, 2000, 2010]
y = [3929326, 5308483, 7239881, 9638453, 12866020, 17069453, 23191876, 31443321, 39818449, 50189209, 62947714,
     76212168, 92228496, 106021537, 122775046, 132164569, 150697361, 179323175, 203302031, 226545805, 248709873,
     281421906, 308745538]

yy = y
xx = x
listOfErrors = []


xvals = np.arange(1790, 2011, 1)
func = interpolate.splrep(xx, yy, s=0)
yvals = interpolate.splev(xvals, func, der=0)
old_yvals = []
update = 0
for i in range(len(y)-1):
    old_yvals.append(yvals[len(yvals)-update-1]) # old_yvals holds all the pop for every 10 years, ex 2010, 2000...
    update+=10                                  # using all the given points



xx.pop()  # pop the last element on xx
yy.pop()  # pop the last element on yy
new_yvals = []
updateYear = 2011
for i in range(19): # up to 20 because you need at least 3 points for cubic interpolation
    xvals = np.arange(1790, updateYear, 1)
    func = interpolate.splrep(xx, yy, s=0)
    yvals = interpolate.splev(xvals, func, der=0)

    new_yvals.append(yvals[-1])
    updateYear-=10
    xx.pop()  # pop the last element on xx
    yy.pop()  # pop the last element on yy




for i in range(len(old_yvals)-3): # minus three because new_yvalues has a smaller length
    listOfErrors.append(abs(old_yvals[i] - new_yvals[i]))

listOfErrors.reverse()

####### PLOTING ERROR POINTS ########
newX = np.arange(0,len(listOfErrors), 1)
plt.plot(newX, listOfErrors)
plt.grid(True)
plt.show()

year = 1790
for errors in listOfErrors:
    print "Year: {}".format(year) + "\t" + "Error: {}".format(errors)
    year+=10





################ CUBIC INTERPOLATION WITH THE GIVEN DATA ################
# xvals = np.arange(1790, 2011, 1)
# func = interpolate.splrep(xx, yy, s=0)
# yvals = interpolate.splev(xvals, func, der=0)

# for i in range(len(xvals)):
    #print "Year: {}".format(xvals[i]) + "\t" "Population: {}".format(yvals[i])

# plt.plot(xvals, yvals)
# plt.grid(True)
# plt.show()
#########################################################################



