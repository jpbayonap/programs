import matplotlib.pyplot as plt
import csv
import numpy as np

import pandas as pd

y = []

x=[]
def cool_range(start, stop,step):
    j= start
    while j <= stop :
        yield j
        j += step
with open('yoonprob.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for counter ,row  in enumerate(plots):
        if counter < 11:
            x.append(float(row[2][0:11]))
            y.append(float(row[0]))
        else:
            y.append(float(row[0]))
    '''for row  in plots:
        x.append(float(row[2]))
        y.append(float(row[1]))'''
'''
    for counter ,row  in enumerate(plots):
            if counter < 11:
# time
                x.append(float(row[2][0:11]))
                y.append(float(row[1]))
            else:
                y.append(float(row[1]))'''


def split_data(array,step,parts):

    datos=[]
    for i  in  range(parts):

        datos.append(array[step*(i):(i+1)*step])

    return datos


hey = split_data(y,11,4)
#dude = split_data(x,11,4)  if you want to split it
print(hey)
#print(dude)
print(x)



'''
fig = plt.figure()

plt.subplot(2, 1, 1)
plt.plot(x,hey[0],color= 'red')
#plt.ylabel('time steps')
plt.ylabel('probability of ignition')
plt.yticks([i for i in cool_range(0,160,40)] )
plt.xlim(0.0000,  1.0)
#plt.title(' time steps requiered for a 100 size grid percentage of burned trees\n with variable probability ')
plt.title('  100 size grid percentage of burned trees\n with variable probability ')
plt.legend(['1 step'])

plt.subplot(2, 1, 2)
plt.plot(x,hey[1],color= 'blue')
plt.yticks([i for i in cool_range(0,200,40)] )


plt.xlim(0.0000,  1.0)
#plt.ylabel('time steps')
plt.ylabel('probability of ignition')
plt.legend(['3 step'])

plt.subplot(2, 1, 1)
plt.plot(x,hey[2],color ='orange')
plt.yticks([i for i in cool_range(0,320,80)] )
plt.xlim(0.0000,  1.0)
#plt.ylabel('time steps')
plt.ylabel('probability of ignition')
plt.legend(['5 step'])

plt.subplot(2, 1, 2)
plt.plot(x,hey[3],color='purple')
plt.yticks([i for i in cool_range(0,560,120)] )
#plt.ylabel('time steps')
plt.ylabel('probability of ignition')
plt.legend(['7 step'])

plt.xlim(0.0000,  1.0)
fig.subplots_adjust(hspace=0.4, wspace=50.0)

plt.xlabel('probability')
#plt.ylabel('time steps')
plt.ylabel('probability of ignition')

plt.show()
'''




fig = plt.figure()

plt.subplot(2, 1, 1)
plt.plot(x,hey[0],color= 'red')
#plt.ylabel('time steps')
plt.ylabel('percentage')
#plt.yticks([i for i in cool_range(0,160,40)] )
plt.ylim(0,2)
plt.xlim(0.0000,  1.0)
#plt.title(' time steps requiered \n with variable probability ')
plt.title('  percentage of burned trees\n with variable probability ')
plt.legend(['50 size , 5 burning  '])

plt.subplot(2, 1, 2)
plt.plot(x,hey[1],color= 'blue')
#plt.yticks([i for i in cool_range(0,200,40)] )
plt.ylim(0,1.5)

plt.xlim(0.0000,  1.0)
#plt.ylabel('time steps')
plt.ylabel('percentage')
plt.xlabel('probability of ignition')

plt.legend(['100 size . 5 burning'])
fig2 = plt.figure()
plt.subplot(2, 1, 1)
plt.plot(x,hey[2],color ='orange')
#plt.yticks([i for i in cool_range(0,320,80)] )
plt.xlim(0.0000,  1.0)
#plt.ylabel('time steps')
plt.ylabel('probability of ignition')
plt.legend(['50 size , 7 burning'])
plt.ylim(0,1.5)
#plt.title(' time steps requiered \n with variable probability ')
plt.title('  percentage of burned trees\n with variable probability ')
plt.subplot(2, 1, 2)
plt.plot(x,hey[3],color='purple')
#plt.yticks([i for i in cool_range(0,560,120)] )
#plt.ylabel('time steps')
plt.ylabel('probability of ignition')
plt.legend(['100 size ,7 burning'])
plt.ylim(0,1.5)
plt.xlim(0.0000,  1.0)
fig.subplots_adjust(hspace=0.4, wspace=50.0)

plt.xlabel('probability')
#plt.ylabel('time steps')
plt.ylabel('probability of ignition')

plt.show()
