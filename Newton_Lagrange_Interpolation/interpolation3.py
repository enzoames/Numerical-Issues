import numpy as np
import matplotlib.pyplot as plt

def plot(f, points):
	x = range(300, 500)
	y = map(f, x)
	# print y
	plt.plot( x, y, linewidth=2.0)
	xList = []
	yList = []
	for x_p, y_p in points:
		xList.append(x_p)
		yList.append(y_p)
	# print xList
	# print yList
	plt.plot(xList, yList, 'ro')

	plt.show()

def compareResult(P, points):
	T = 350
	for i in range(len(points)-1):
		eT = 0.02424 * ((T/303.16)**1.27591)
		print "e({}) = ".format(T) + str(eT) + "\tP({}) = ".format(T) + str(P(T))
		T+=100

def lagrange(points):
	def P(x):
		total = 0
		n = len(points)
		for i in xrange(n):
			xi, yi = points[i]

			def g(i, n):
				tot_mul = 1
				for j in xrange(n):
					if i == j:
						continue
					xj, yj = points[j]
					tot_mul *= (x - xj) / float(xi - xj)
				return tot_mul

			total += yi * g(i, n)

		return total



	return P

def main():
	# points = [(300,0.024), (400,0.035), (500,0.046), (600,0.058), (700,0.067),
	# (800,0.083), (900,0.097), (1000,0.111), (1100,0.125), (1200,0.140),
	# (1300,0.155), (1400,0.170), (1500,0.186), (1600, 0.202), (1700,0.219),
	# (1800,0.235), (1900,0.252), (2000,0.269)]
	points = [(300,0.024), (400,0.035), (500,0.046)]
	P = lagrange(points)
	# print P
	compareResult(P, points)
	plot(P, points)
if __name__ == '__main__':
	main()





	# points = [(300,0.024), (400,0.035), (500,0.046)]

	# nr = 2
	# print "(" + str(points[nr][0]) + ", " + str(points[nr][1]) +") P(" + str(points[nr][0]) +")= " +str(P(points[nr][0]))
