from scipy import stats
import numpy as np
x=np.array( [0.0323 , 0.020 ,0.05, 0.09 , 0.155 ,0.201 , 0.302 ,0.342 , 0.398 ])
y= np.array( [2734,1938, 1959 , 626 ,321 , 74.5 , 38 , 46.3 , 33])
w= np.polyfit(x,y,1)
print ("w")
