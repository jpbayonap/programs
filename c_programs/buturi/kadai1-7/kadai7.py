import matplotlib.pyplot as plt
import pandas as pd

kdata = pd.read_table('kadai7_1.dat', sep='')

plt.plot(kdata[:,0],kdata[:,1] , c= 'r' , label = 'error')
plt.title('second approximation')
plt.xlabel('delta')
plt.ylabel('difference')
plt.legend()
plt.show()
