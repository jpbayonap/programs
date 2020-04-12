import numpy as np
y= np.array([7,8])
x =np.array([[3,5 ],[4,2]])
b= np.array([1,1])
z =np.array([[5,6],[8,9] ])
"""from 0 to stop-1 """
cool = np.array([n for n in range(0,5,1)])
print('this is x:',x)
print('this is y:',y)
print('this is z:',z)
print("x times y:",x.dot(y))
print('出層　XY+B', x.dot(y)+b)
print('y plus z:' , y+z )
print(cool)