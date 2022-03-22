# -*- coding: utf-8 -*-
# simple classification problem
# k-nearest neighbour classifier
# use euclidean distance, 
# i.e dist between the dataset & new feature vector

# data set
# x             class
# 0.15,0.35     1
# 0.15,0.28     2
# 0.12,0.2      2
# 0.1,0.32      3
# 0.06,0.25     3

import numpy as np

k1 = 1
k3 = 3

y = np.array([[0.15,0.15,0.12,0.1,0.06],
              [0.35,0.28,0.2,0.32,0.25]])

x = np.array([0.1,0.25])

r,c = y.shape
g = ''

it = 0

nu = np.array([[1.0, 0.0],
               [2.0, 0.0],
               [2.0, 0.0],
               [3.0, 0.0],
               [3.0, 0.0]])

for i in range(0,c):
    # it = it+1
    # print("[it: ", it)
    dist = np.linalg.norm(x - y[:,i])
    nu[i][1] = dist
    #print(dist)
    
order = np.argsort(nu[:, 1])[::1]
resOrder = nu[order, :]
print(resOrder)    

# when k = 1
resK1 = resOrder[:k1,0]
# print("k1: ", resK1)
values, counts = np.unique(resK1[:], return_counts=True)
ind = np.argmax(counts)
print("k1: ", values[ind]) 


# when k = 3
resK1 = resOrder[:k3,0]
# print("k1: ", resK1)
values, counts = np.unique(resK1[:], return_counts=True)
ind = np.argmax(counts)
print("k3: ", values[ind]) 



