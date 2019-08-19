import glob
import matplotlib.pyplot as plt
import csv
import numpy as np

import pandas as pd

y0 = []
y1 = []
y2=[]
y3=[]
y4=[]
x=[]
with open('datos0.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row  in plots:
        y0.append(row[0])
        x.append(row[2])


with open('datos1.txt','r') as csvfile:

    plots = csv.reader(csvfile, delimiter=',')
    for row  in plots:
        y1.append(row[0])

plt.plot(x,y0, label='Loaded from file!')
plt.plot(x,y1, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
