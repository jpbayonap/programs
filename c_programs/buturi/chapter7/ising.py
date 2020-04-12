import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

for i in range(9,12):
	dat = np.loadtxt('ising'+str(i)+'.dat')
	plt.plot(dat.T[0],dat.T[4],".", label= "grid size {}x{}".format(i,i))
plt.legend()
plt.title('Average Magnetic susceptibility as a function of temperatures')
plt.xlabel('temperature T K')
plt.ylabel('Magnetic susceptibility X')
plt.savefig('mags.png',format ='png')
plt.show()
