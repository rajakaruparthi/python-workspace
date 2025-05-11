import sklearn
import csv
from sklearn.linear_model import LinearRegression

# load data

import numpy as np

p = [1, 2, 3]
matrix = np.array([[1, 2], [1, 2]])
vector = [3, 5]  # 2*2 1*2
#
# print(matrix @ vector)
#
# print(vector @ matrix)

a = np.arange(2).reshape((1, 1, 2))
print(a)
print("-----")
b = np.arange(6).reshape((3, 2))
print(b)
c = np.inner(a, b)  # inner product of a and b
print(c)
shp = c.shape
print("shp--", shp)

y = np.zeros((3, 3, 4))

t = np.ones((2, 3, 4))
# y = np.zeros((1, 3, 4))
print(y)
print(t)


A = [[1,1,1],
     [3,2,1],
     [2,1,2]]

Ainv = np.linalg.inv(A)

print(Ainv)



A = [[1,1,1],
     [3,2,1],
     [2,1,2]]

s = [15, 28, 23]



A = [[ 1 , 1, 1],
     [ 0,  1 ,  2],
     [ 0,  0 ,  1  ]]
s = [15, 17, 5]




Ainv = [[-1.5 , 0.5,  0.5],
 [ 2   ,0 , -1 ],
 [ 0.5 ,-0.5,  0.5]]


s = [9, 7, 2]

