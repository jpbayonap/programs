
import numpy as np
import  matplotlib.pyplot as plt
from matplotlib import rcParams

from matplotlib.font_manager import FontProperties
fp_ipa = FontProperties(fname=r'C:\WINDOWS\Fonts\YUGOTHB.TTC', size=14)

f = np.arange(0,100000000,100)
R = 200
C = 70e-9
def L(f):
    return 10*np.log(1/(2.*np.pi*f*C*R))
plt.figure(1)

plt.loglog(f,L(f),'b')
plt.title('Elle graph',fontproperties= fp_ipa)
plt.xlabel('log(f)' , fontproperties =fp_ipa)
plt.ylabel('decibels' , fontproperties = fp_ipa)

plt.show()
plt.savefig('elle.pdf')
