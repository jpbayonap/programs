import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.font_manager import FontProperties

fp = FontProperties(fname='osaka.ttf', size=14)
# BITCOINの価格をプロット
bitcoin = pd.read_csv('~/PycharmProjects/machine_learning/python_day2/Bitcoin.csv')
print(bitcoin)
print(bitcoin.shape)
# 折れ線グラフで価格変動をプロット bitcoin.column
price = bitcoin['Price']
date = bitcoin['Date']
# figure size  figsize(horizontal,vertical)
fig = plt.figure(figsize=(14, 8))
plt.plot(date, price)
plt.title('Bitcoin price change')
plt.grid(True)
plt.tick_params(labelcolor='r', labelsize='small',width =0.2)
#roteate axis
plt.xticks(rotation=30)
#Print values
for x, y in zip(bitcoin.Date, bitcoin.Price):
    plt.text(x, y, y, ha='center', va='bottom')

plt.show()

# 棒グラフで日付と価格を両方プロッと
fig = plt.figure(figsize=(15,9))
plt.xticks(rotation=30)
plt.grid(True)
plt.bar(bitcoin.Date, bitcoin.Price,
        color ='g',width=0.5)
plt.xlabel('date')
plt.ylabel('price')
plt.title('bitcoin price fluctuation')

for x, y in zip(bitcoin.Date, bitcoin.Price):
    plt.text(x, y, y, ha='center', va='bottom')
plt.plot()
#dont forget to show
plt.show()


world = pd.read_csv('~/PycharmProjects/machine_learning/python_day2/world2015.csv')

map_dict = {
    'Asia':'green',
    'Europe':'red',
    'Africa': 'yellow',
    'North America':'blue',
    'South America':'blue',
    'Oceania':'c'
}
colors = world.Continent.map(map_dict)
size = world.Population/ 1e6  # one million
plt.xlabel('ハロ',fontproperties = fp)
plt.xscale('log')
plt.xlim(world.GDP_per_capita.min(),world.GDP_per_capita.max())
plt.scatter(world.GDP_per_capita, world.Life_expectancy,c=colors, s=size, alpha=0.5)
plt.grid(True)
plt.show()
