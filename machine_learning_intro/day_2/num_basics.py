import numpy as np

print(np.version.version)
print(np.array([1, 2, 6]))
# shape of your array shape(行、列）
print(np.array([[1, 2, 5], [2, 3, 6]]).shape)
# 3次元配列　
three_d = np.array([[[12, 13, 14], [15, 16, 17]],
                    [[6, 7, 8], [9, 10, 11]]])
print(three_d)
# shape 表示順番（層、行、列)
print(three_d.shape)

# arange array range function arange(initial,stop,step)
# with complex 引数が　一つ
print(np.arange(5, dtype=complex))
# 5から３０まで、一次元の整数昇順列を作成　引数二つ
print(np.arange(5, 30))
# with five step change　引数が三つ
print(np.arange(5, 30, 5))
# 2 to 20 3step 20<stop<=23
print(np.arange(2, 21, 3))
# 等差数列別解 for loop
print(np.array([n for n in range(2, 21, 3)]))
'''make a three dimensional array of (4,5,,1,4)'''

big3 = np.array([
    [[np.arange(4)], [np.arange(2, 10, 2)], [np.arange(3, 11, 2)], [np.arange(4, 12, 2)], [np.arange(5, 13, 2)]],
    [[np.arange(4)], [np.arange(4)], [np.arange(4)], [np.arange(4)], [np.arange(4)]],
    [[np.arange(4)], [np.arange(4)], [np.arange(4)], [np.arange(4)], [np.arange(4)]],
    [[np.arange(4)], [np.arange(4)], [np.arange(4)], [np.arange(4)], [np.arange(4)]],
])
print(big3)
# (four layers, five rows,  one  column , four inner elements)
print(big3.shape)
# (4 layers,5 rows,4 columns)
big = np.array([
    [np.array([1] * 4), np.array([2] * 4), np.array([3] * 4), np.array([4] * 4), np.array([5] * 4)],
    [np.array([1] * 4), np.array([2] * 4), np.array([3] * 4), np.array([4] * 4), np.array([5] * 4)],
    [np.array([1] * 4), np.array([2] * 4), np.array([3] * 4), np.array([4] * 4), np.array([5] * 4)],
    [np.array([1] * 4), np.array([2] * 4), np.array([3] * 4), np.array([4] * 4), np.array([5] * 4)],
])
print(big)
print("shape of the  tensor:", big.shape)
# １次元配列の要素指定
# ０から５まで　、１単位、整数昇順配列 np.arange(5+1) 6 elements
c = np.arange(6)
print(c)
#  第６位の要素
print(c[5])
# inverse method [-5,-4,-3,-2,-1]
print(c[-1])
# 要素の変換
# 1位を65に変更する。
c[0] = 65
print(c)
# 3位から全ての要素を６７に変更する
c[2:] = 67
print(c)
# 2次元配列の要素指定
d = np.array([np.arange(0, 5), np.arange(5, 10), np.arange(10, 15)])
print(d.shape, d)
print(d[1][4])
print(d[1][2:5])
""" 0 1 2 3 4 列
0
1
2
行
"""
e = np.array([
    [np.arange(0, 5), np.arange(5, 10), np.arange(10, 15)],
    [np.arange(15, 20), np.arange(25, 30), np.arange(35, 40)],
    [np.arange(45, 50), np.arange(55, 60), np.arange(65, 70)],
    [np.arange(75, 80), np.arange(85, 90), np.arange(95, 100)]
])
print(e, e.shape)

# 第１層を抽出する
print(e[0])
# print [27,28,29]
print('second layer,second row, third to fifth collumn:', e[1][1][2:])
# print 8
print(e[3][1][3])

'''配列の計算'''
f = np.array([[1, 2, 3, 4], [6, 8, 10, 12]])
# 四則演算
print(f - 1)
print(f * 3)
print(1 / f)
# **乗
print(f ** 2)
print(f - f)
# 最大値
print('max', np.max(e))
# 最小値
print('min', np.min(e))
# 合算値
print('sum', np.sum(e))
# 平均値
print('mean value', np.mean(e))
# 中央値
print('median', np.median(e))

'''行列の積　np.dot'''
g = np.arange(3)
h = np.arange(3, 6)
print(g.dot(h))
# 別解
print(np.dot(g, h))
A = np.array([5, 10, 15])
# print [35,50,65]
B = A + np.array([30, 40, 50])
print(B)
# print [30,160] (2,1)
C = np.array([A[0] * 6, A[1] * 16])
print(C)
# or with linear algebra  (2,3)*(3,1)
D = np.array([[1, 1, 1], [4, 5, 6]])
print(D.dot(A))
# 他の関数
# 配列の形状を変換する reshape
i = np.arange(12)
print(i.reshape(4, 3))
# 縦軸と横軸を変換する転置行列 transpose
print(i.reshape(4, 3).transpose())
# 0~1 の中で乱数を作成する  random.rand(size) () == 1
# random.randint (low, high , size_array () == 1)

j = np.random.randint(10, 52, 5)
print(j)
print(np.random.rand())

# Linspace 決まった空間をx均等分にする (low, high, parts+1)
k = np.linspace(0, 15, 4)  # three parts
print(k)
# append 配列の末尾で要素を追加する
l = np.append(k, [25, 30])
print(l)
# flatten 高次元配列を１次元化する
m = i.reshape(3, 4)
print(m.flatten())
# all 全て要素が条件を満たすとき[True]
print(np.all(l > 2))
# any 一つの要素だけ条件を満たすとき　[True]
print(np.any(l == 6))
# where 条件を満たす部分を np.where(condition , if Ture, if False)
print(l < 35)
print(np.where(l < 35, 1, 0))

'''excersices '''
r10 = np.random.rand(10)
print('biggest 最大', r10.max(), "minimum 最小", r10.min(), 'difference 差', r10.max() - r10.min())

E = np.arange(40).reshape(4, 5, 2)
print(E)
print('third  layer, from third row', E[2][2:])
E[2][2:] = 2152
print(E)

print(np.linspace(-1, 1, 40))
F = np.where(np.linspace(-1, 1, 40).reshape(4, 5, 2) >= 0, 1, -1)
print(F)