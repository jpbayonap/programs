
import numpy as np
import  matplotlib.pyplot as plt
from matplotlib import rcParams

from matplotlib.font_manager import FontProperties
fp_ipa = FontProperties(fname=r'C:\WINDOWS\Fonts\YUGOTHB.TTC', size=14)

a=  5.2917721092e-11
r= np.arange(0.5*a , 15*a, a/100)
p = r/a
Eh = 4.35974434e-18
def j(p):
    return Eh*np.exp(-2*p)*(1+(1./p))

def k(s):
    return  Eh*np.exp(-p)*((1./p)-((2/3)*p))
plt.figure(1)

plt.subplot(2,1,1)
plt.plot(p,j(p),'b')
plt.title('クーロン積分',fontproperties= fp_ipa)
plt.xlabel('距離　R/a' , fontproperties =fp_ipa)
plt.ylabel('エネルギー ハートリー' , fontproperties = fp_ipa)


plt.subplot(2,1,2)
plt.plot(p,k(p),'b',p,p*0,'r')
plt.title('共鳴積分', fontproperties = fp_ipa )
plt.xlabel('距離　R/a' , fontproperties =fp_ipa)
plt.ylabel('エネルギー ハートリー' , fontproperties = fp_ipa)



plt.subplots_adjust(bottom=0.1, right=0.8, top=0.8,wspace = 0.8, hspace= 0.8)
plt.show()
plt.savefig(' foo.pdf')
