import numpy as np
import matplotlib.pyplot as plt

def func_1(x):

    return 3*(1 if np.abs(x)>np.pi/2 else -1)

l= 100
period = 2*np.pi

interval= [(-np.pi+j*(period/l))for j in range(l)]

""" with riemann aprox  n= 1000"""

def am(interval,n):
    a_m = 0
    for x in interval:
        a_m = a_m + period/l *func(x)*np.cos(n*x)

    return(a_m)

def fourier(t,s_n):

    fourier= np.array([am(interval,n)*np.cos(n*t) for n in range(s_n)])
    return fourier.sum()


y_axis = np.array([fourier(t,100)for t in interval])
y_2= np.array([func_1(x)for x in interval])
plt.figure(1)
plt.plot(interval,y_axis)
plt.figure(2)
plt.plot(interval,y_2)
plt.show()
print(len(interval))


#am(interval,5)

#def trans(x,n):
    #trans= np.array([])
