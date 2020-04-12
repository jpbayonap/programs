import matplotlib.pyplot as plt
import numpy as np
dat1 = np.loadtxt('pi_comp.dat')
dat = np.loadtxt('pi_madhava.dat')
plt.title('madhava '+ r'$\pi$'
+ ' approximation ')
plt.yscale('log')
plt.ylabel(r'$\log(\pi -S_n)$')
plt.xlabel('partial sum number n')
plt.plot(dat[:,0],dat[:,1], label =' madhava approximation   '+ r'$\sqrt{12}\;\sum_i \frac{-3^{-i}}{2i+1}$')
plt.plot(dat1[:,0],dat1[:,2], label= 'tanget approximation  '+ r'$4\; \sum_i (\frac{-1}{2n+1})^i$')
plt.legend()
plt.savefig('madhava.png', format= 'png')
plt.show()
