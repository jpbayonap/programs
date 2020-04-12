import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
dat = np.loadtxt('eigen.dat')
dat2 = np.loadtxt('eigen2.dat')
xmin = 0
xmax = 10
n = 1000
delta = np.abs(xmin-xmax)/n

def airy(x):
	return  -np.power((3*np.pi)/2*(x-0.25), 2/3)

x = np.arange(xmin,xmax,delta)
'''
for i in range(3):
    plt.plot(x,dat2[i][1:],label='energy {} ,{} '.format(i,dat2[i][0]))'''

for i in range(3):
    plt.plot(x,dat[i][1:],label='energy {} ,{} '.format(i,dat[i][0]))
    print(airy(i+1))

plt.title('First three eigen functions for the 1D H.O. quantum well with a ={} ,b={} n={}'.format(xmin,xmax,n),c= 'r')
plt.legend( loc='upper right', borderaxespad=0, fontsize=12)
plt.savefig('airy4.png',format ='png')
plt.show()
