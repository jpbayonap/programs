import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def sig(x):
    return 1/(1+np.exp(-x))
font= {'family':'serif',
    'color': 'darkgreen',
    'weight':'normal',
    'size': 16, }

fp = FontProperties(fname='osaka.ttf', size=14)

x =np.arange(-10, 15, 0.5)
y = sig(x)
plt.plot(x, y, 'k')
plt.title(' sigmond function ', fontdict =font)
plt.text( 5,0.6,r'$\frac{1}{1+ e^{-x}}$', fontdict= font)
plt.xlabel(u'出層値', fontdict = font, fontproperties=fp)
plt.ylabel(u'確率', fontdict= font, fontproperties=fp)
plt.subplots_adjust(left= 0.15)
plt.grid(True)
plt.show()





