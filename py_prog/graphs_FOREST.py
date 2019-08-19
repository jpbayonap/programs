import matplotlib.pyplot as plt
import csv
import numpy as np
from io import StringIO
import pandas as pd

y = []

x=[]

with open('datoselap50.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for counter ,row  in enumerate(plots):
        if counter < 8:

            x.append(float(row[2][0:8]))
            y.append(float(row[0]))
        else:
            y.append(float(row[0]))
def split_data(array,step,parts):

    datos=[]
    for i  in  range(parts):

        datos.append(array[step*(i):(i+1)*step])


    return datos


hey = split_data(y,8,5)

print(hey)
print(x)

'''
fig = plt.figure()

plt.subplot(4, 1, 1)
plt.plot(hey[0],color= 'red')
plt.ylim(0.0000,  2.0)
plt.xlim(0.0000,  8.0)
plt.ylabel('percentage')
plt.title(' 50 size grid percentage of burned trees\n with variable burning time \n fixed probability of ignition ')
plt.legend(['0.2 probability'])
plt.subplot(4, 1, 2)
plt.plot(hey[1],color= 'blue')
plt.ylim(0.0000,  2.0)
plt.xlim(0.0000,  8.0)
plt.ylabel('percentage')
plt.legend(['0.3 probability'])
plt.subplot(4, 1, 3)
plt.plot(hey[2],color ='orange')
plt.ylim(0.0000,  2.0)
plt.xlim(0.0000,  8.0)
plt.ylabel('percentage')
plt.legend(['0.4 probability'])
plt.subplot(4, 1, 4)
plt.plot(hey[3],color='purple')
plt.ylabel('percentage')
plt.legend(['0.5 probability'])
plt.ylim(0.0000,  2.0)
plt.xlim(0.0000,  8.0)
fig.subplots_adjust(hspace=0.5, wspace=50.0)
plt.xlabel('burning time')
plt.ylabel('percentage')

plt.show()
'''



fig = plt.figure()

plt.subplot(2, 1, 1)
plt.plot(x,hey[0],color= 'blue')
#plt.ylabel('time steps')
plt.ylabel('percentage')
#plt.yticks([i for i in cool_range(0,160,40)] )
plt.ylim(0,1.5)
plt.xlim(0.0000,  8.0)
#plt.title(' time steps requiered to completely burn \n with variable burning time ')
plt.title('  percentage of burned trees\n with variable burning time ')
plt.legend(['50 size , 0.4 probability  '])

plt.subplot(2, 1, 2)
plt.plot(x,hey[1],color= 'green')
#plt.yticks([i for i in cool_range(0,200,40)] )
plt.ylim(0,1.5)

plt.xlim(0.0000,  8.0)
#plt.ylabel('time steps')
plt.ylabel('percentage')
plt.xlabel('time to burn (steps)')
fig.subplots_adjust(hspace=0.4, wspace=50.0)
plt.legend(['100 size , 0.4 probability'])




fig2 = plt.figure()
plt.subplot(2, 1, 1)
plt.plot(x,hey[2],color ='green')
#plt.yticks([i for i in cool_range(0,320,80)] )
plt.xlim(0.0000,  8.0)
#plt.ylabel('time steps')
plt.ylabel('percentage')
plt.legend(['50 size , 0.5 probability'])
plt.ylim(0,1.5)
#plt.title('  time steps requiered to completely burn \n with variable burning time ')
plt.title('  percentage of burned trees\n with variable probability ')
plt.subplot(2, 1, 2)
plt.plot(x,hey[3],color='purple')
#plt.yticks([i for i in cool_range(0,560,120)] )
#plt.ylabel('time steps')
plt.ylabel('percentage')
plt.legend(['100 size , 0.5 probability'])
plt.ylim(0,1.5)
plt.xlim(0.0000,  8.0)
fig.subplots_adjust(hspace=0.4, wspace=50.0)

plt.xlabel('time to burn(steps)')
#plt.ylabel('time steps')


plt.show()
