import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
dat1 = np.loadtxt('ising10.dat')
dat2 = np.loadtxt('ising9.dat')
dat3 = np.loadtxt('ising11.dat')


for i in range(3):
    plt.plot(dati[0],dat[1],label='energy {} ,{} '.format(i,dat[i][0]))
