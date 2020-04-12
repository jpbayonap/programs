import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

#my cool font
font ={'family': 'serif','color': 'darkred',
       'weight': 'normal',
       'size': 18}
fp = FontProperties(fname='osaka.ttf', size=14)

# y probability
y = np.array([0.2,0.3])
# true values
t = np.array([1,0])
def mse(y,t):
    return  0.5*(np.sum((y-t)**2) )

print(mse(y,t))
