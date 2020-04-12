import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from matplotlib import rcParams

# math graph
t = np.arange(0.0, 2.0, 0.02)

fp = FontProperties(fname='osaka.ttf', size=14)


def s(x):
    return np.sin(2 * np.pi * x)


fig, ax = plt.subplots()
# plot fig
ax.plot(t, s(t))
# Cool font
font = {'family': 'serif',
        'color': 'darkgreen',
        'weight': 'normal',
        'size': 14, }

plt.title('function', fontdict=font)
plt.text(0.55, 0.75, r'$ s(t) = \sin(2 \pi t) $', fontdict=font)

# grid
ax.grid(True, linestyle='-.')
# x-y label parameter
ax.tick_params(labelcolor='r', labelsize='medium', width=3)
plt.show()

# 棒グラフ

N = 6
# mean values
men_means = (20, 35, 30, 35, 27, 29)
women_means = (25, 32, 34, 20, 25, 27)
# standard deviation
menStd = (2, 3, 4, 1, 2, 3)
womenStd = (3, 5, 2, 3, 3, 4)
# number of colulmns
ind = np.arange(N)
width = 0.4

p1 = plt.bar(ind, men_means, width, yerr=menStd)
# men at bottom
p2 = plt.bar(ind, women_means, width,
             bottom=men_means, yerr=womenStd)
plt.ylabel('scores', fontdict=font)
plt.xlabel('groups ', fontdict=font)
plt.title('Scores by Group and Gender', fontdict=font)
# tick parameters
plt.tick_params(labelcolor='g', labelsize='medium', width=3)
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5', 'G6'))
#  80< stop <= 100
plt.yticks(np.arange(0, 81, 10))
# Add legend　
plt.legend((p1, p2), ('Men', 'Women'))

plt.show()

# 円グラフ
# define labels for the graph
labels = 'Cats', 'Dogs', 'Birds', 'Sharks'
# percentages of the portions
sizes = [14, 46, 30, 10]
# explode take out a portion for reference
explode = (0, 0.2, 0, 0)

# define  fig
''' startangle = where to position Cats '''
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode,
        labels=labels, autopct='%2.2f%%',
        shadow=True, startangle=90, )
ax1.axis('equal')
plt.title('animals that I like ', fontdict=font)
plt.show()

# 3Dグラフ


X = np.arange(-10, 10, 0.5)
Y = np.arange(-10, 10, 0.5)
# things mesh perfectly  windows wire mesh Create your grid
X, Y = np.meshgrid(X, Y)
G = np.sin(np.sqrt(X ** 2 + Y ** 2))
fig = plt.figure()
axis = Axes3D(fig)
axis.plot_surface(X, Y, G, rstride=1,
                  cstride=1, cmap=cm.viridis)
plt.show()

# 基本操作
# １次元、10要素の配列を作成


data = np.array(np.random.randint(0, 100, 10))
print(data)
plt.plot(data)
# plt.xlabel('一次元配列', fontproperties=fp)
plt.show()

# 軸のラベルと図のタイトル
x = np.array([1, 2, 5])
y = np.array([1, 5, 9])
plt.title('test graph', fontdict=font)
plt.xlabel('x axis', fontdict=font)
plt.ylabel('y axis', fontdict=font)

# 付ける場所に注意
plt.plot(x, y)
# グラフ凡label　ALWAYS AFTER PLOT
plt.legend(['The Blue Team'])
# legend(loc) で表示場所を指定する 0~10
plt.legend(['Here is the Blue Team'], loc=0)
plt.show()

# 線の色、幅とSTYLE    dashed
''' color = 'c' cyan 
 'm' magenta    '--'破線
 'k' black　　　　’ー.’　点線
'b' blue 　　　　　’：’　更に小さい点線
'''
plt.plot(x, y, color='c', linewidth=3, linestyle='--')
plt.legend(['Red team'], loc=4)
plt.show()

''' 数学グラフ'''
xs = np.linspace(-10, 10, 100)
ys1 = 2 * xs + 1
ys2 = xs ** 2
ys3 = 20 * np.sin(2 * np.pi * xs)
plt.title('multiple graphs', fontdict=font)
plt.plot(xs, ys1, color='k', linestyle=':')
plt.plot(xs, ys2, color='b', linestyle='-')
plt.plot(xs, ys3, color='r', linestyle='--')
plt.legend([r'y =2x+1', r'$x^{2}$', r'$3\sin(2\pi x)$'], loc=5)
plt.show()

# 軸の表示範囲を指定する
plt.plot(xs, ys1)
plt.plot(xs, ys2)
plt.xlim((2, 3))
plt.ylim((4, 8))
plt.legend(['y= 2x+1', r'$y = x^{2}$'], loc=3)
plt.show()

# sigmond
e = np.e
y = 1 / (1 + e ** -xs)
plt.title('sigmond', fontdict=font)
plt.plot(xs, y)
plt.show()

'''棒グラフ'''
score = np.array(np.random.randint(0, 30, 5))
plt.bar([0, 1, 2, 3, 4], score)
plt.show()

''' x　必須　格棒X軸上の数値
　　height 　各棒の高さ
    width 　棒の太さ
    Ｃolor
    edgecolor 棒の枠線のいろ
    xerr ,yerr 　Ｘ，Ｙ軸方向の誤差範囲
'''
# 色と棒の太さ
height = np.array(np.random.randint(0, 80, 5))
plt.bar(x=[0, 1, 2, 3, 4], height=height,
        color='c', width=0.6)
plt.show()
# 積み上げ棒グラフ
height1 = np.array([10, 20, 34, 25, 50])
height2 = np.array(np.random.randint(0, 80, 5))

plt.bar(x=[0, 1, 2, 3, 4], height=height1,
        color='b', width=0.5)
plt.bar(x=[0, 1, 2, 3, 4], height=height2,
        bottom=height1, color='orange', width=0.5)
plt.show()

# Error bar label and titles
price = np.array(np.random.randint(10, 120, 5))
std = np.array(np.random.randint(0, 10, 5))

plt.xlabel('stock', fontdict=font)
plt.ylabel('Price', fontdict=font)
plt.title('Stock Price')
plt.bar(x=[0, 1, 2, 3, 4], height=price, yerr=std,
        color='g', width=0.6)
plt.show()

# 軸っ森野表示内容 and grid
x_axis = ['Andes', 'Facebook', 'Rakuten', 'Google', "Amazon"]

plt.xlabel('Stock', fontdict=font)
plt.ylabel('Price', fontdict=font)
plt.title('Stock price report', fontdict=font)
plt.bar(x=x_axis, height=price, yerr=std,
        color='red', width=0.4)
plt.grid(True)
plt.show()

# 各棒上にその棒の数字を入れる
plt.xlabel('Stock', fontdict=font)
plt.ylabel('Price', fontdict=font)
plt.title('2nd Stock price report', fontdict=font)
plt.bar(x=x_axis, height=price,
        color='yellow', width=0.5)
# use for to print over the bars
for a, b in zip(x_axis, price):
    plt.text(a, b, b, ha='center', va='bottom')

plt.grid(True)
plt.show()

'''Scatter plots 散布図'''
# mistake page 46
world = pd.read_csv('~/PycharmProjects/machine_learning/python_day2/world2015.csv')
plt.scatter(world.GDP_per_capita, world.Life_expectancy)
plt.xlabel('gdp per capita')
plt.ylabel('life expectancy')

plt.show()

# 点の太さを人口数と正比例で運動する

size = world.Population / 1e6
plt.scatter(world.GDP_per_capita, world.Life_expectancy, s=size, alpha=0.5)
plt.show()

# 対数グラフ
plt.xscale('log')
plt.xlim(world.GDP_per_capita.min(), world.GDP_per_capita.max())
plt.scatter(world.GDP_per_capita, world.Life_expectancy, s=size, alpha=0.5)
plt.show()

# 色を付ける
map_dict = {
    'Asia': 'green',
    'Europe': 'red',
    'Africa': 'yellow',
    'North America': 'blue',
    'South America': 'blue',
    'Oceania': 'c'
}
# 　worls csv　中の Continent コラムの要素をそれぞれの色に変換する
colors = world.Continent.map(map_dict)
size = world.Population / 1e6  # one million
plt.xscale('log')  # X軸に対数を取る
plt.xlim(world.GDP_per_capita.min(), world.GDP_per_capita.max())
plt.scatter(world.GDP_per_capita, world.Life_expectancy, c=colors, s=size, alpha=0.5)
plt.show()

#

map_dict = {
    'Asia': 'green',
    'Europe': 'red',
    'Africa': 'yellow',
    'North America': 'blue',
    'South America': 'blue',
    'Oceania': 'c'
}
# 　worls csv　中の Continent コラムの要素をそれぞれの色に変換する
fp = FontProperties(fname='osaka.ttf', size=14)
colors = world.Continent.map(map_dict)
size = world.Population / 1e6  # one million
plt.xscale('log')  # X軸に対数を取る

plt.xlabel('人当たりGDP', FontProperties=fp)
plt.ylabel('平均寿命', FontProperties=fp)
plt.title('平均寿命と人当たりgdpの関係', FontProperties=fp)

# 　フラフの説明文章を入れる print a explanation of the graph
plt.text(8000, 50, '人当たりGDPが大きほど\ｎ平均寿命が高くなります', fontproperties=fp, size=12)  # \n next line

plt.xlim(world.GDP_per_capita.min(), world.GDP_per_capita.max())
plt.scatter(world.GDP_per_capita, world.Life_expectancy, c=colors, s=size, alpha=0.5)
plt.grid(True)
plt.show()

# Population vs GDP per capita
fig = plt.figure(figsize=(14, 8))
map_dict = {
    'Asia': 'yellow',
    'Europe': 'red',
    'Africa': 'black',
    'North America': 'blue',
    'South America': 'g',
    'Oceania': 'c'
}
colors = world.Continent.map(map_dict)
size = world.Population / 10e6
plt.xscale('log')
plt.xlabel('GDP per capita')
plt.ylabel('Population')
plt.text(1000, 800000000, 'no reation between GDP and population', size=20)
plt.xlim(world.GDP_per_capita.min(), world.GDP_per_capita.max())
plt.scatter(world.GDP_per_capita, world.Population, s=size, c=colors, alpha=0.5)
plt.grid(True)
plt.show()

# 円グラフ
# 円グラフ
# Control size  by default it takes the least element size (set it always)
fig = plt.figure(figsize=(8, 8))
plt.title('Pie chart', size=15)
# 各ブブンのラベル　 labels
labels = ['Python', 'Java', 'C++', 'Ruby']

# 各部分の数字　比率
values = [20, 30, 40, 10]

# 各部分の色
colors = ['orange', 'red', 'blue', 'magenta']

# wedgeprops ={'linewidth':, 'width': ,'edgecolor': }
# linewidth 枠線の太さ
# width　円中心の空白
# edgecolor　枠線の色
exp = [0.1, 0, 0, 0]
auto = '%0.1f%%'
rad = 1
wp = {'linewidth': 4, 'width': 0.6, 'edgecolor': 'green'}
ftsize = {'fontsize': 16, 'color': 'purple', 'weight': 'bold'}
pdist = 0.8
rot = 90
plt.pie(values, labels=labels, colors=colors,
        shadow=True, explode=exp, autopct=auto,
        pctdistance=pdist, radius=rad, wedgeprops=wp,
        startangle=rot, textprops=ftsize)
plt.show()

# two rings
# two rings one explode
from matplotlib import cm
plt.title('Most Popular Programming Languages',size=20)
# first ring 内円
val1 = [10, 10, 20, 10, 15, 25, 3, 7]
# second ring 外円
val2 = [20, 30, 40, 10]

# first ring labels
lab1 = ['Amateur', 'Pro'] * 4

# second ring labels
lab2 = ['Python', 'Java', 'c++', 'Ruby']

# colors first ring
col1 = ['red', 'darkred', 'yellow', 'yellow', 'blue', 'darkblue', 'green', 'darkgreen']
col2 = ['orange', 'c', 'purple', 'brown']
# use cm attribute from matplotlib
col3 = cm.Set1(np.arange(8) / 8.)
# size
fig = plt.figure(figsize=(10, 10))
exp1 = [0.4, 0.4, 0, 0, 0, 0, 0, 0]
exp2 = [0.4, 0, 0, 0]
auto = '%0.1f%%'
rad1 = 1.5
rad2 = 3
wp = {'linewidth': 4, 'width': 0.9, 'edgecolor': 'green'}
wp2 = {'linewidth': 4, 'width': 0.9, 'edgecolor': 'green'}
# textprops は文字のスタイルを設定する
ftsize = {'fontsize': 12, 'color': 'white', 'weight': 'bold'}
ftsize2 = {'fontsize': 14, 'color': 'black', 'weight': 'bold'}
pdist1 = 0.8
pdist2 = 1.2
rot = 90
plt.title('Most Popular Programming Languages', size=20)
# plot inner ring
plt.pie(val1, labels=lab1, colors=col3,
        explode=exp1, autopct=auto,
        shadow=True, pctdistance=pdist1,
        startangle=rot, radius=rad1, textprops=ftsize,
        wedgeprops=wp)
plt.pie(val2, labels=lab2, colors=col2,
        explode=exp2, autopct=auto,
        shadow=True, pctdistance=pdist2,
        startangle=rot, radius=rad2, textprops=ftsize2,
        wedgeprops=wp2)

plt.show()
