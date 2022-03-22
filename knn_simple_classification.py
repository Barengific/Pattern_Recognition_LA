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

nu = [[1.0, 0.0],
               [2.0, 0.0],
               [2.0, 0.0],
               [3.0, 0.0],
               [3.0, 0.0]]

for i in range(0,c):
    it = it+1
    print("[it: ", it)
    dist = np.linalg.norm(x - y[:,i])
    nu[i][1] = dist
    print(dist)
    
dtype = [('class', float), ('val', float)]
a = np.array(nu, dtype=dtype)     
   
print(a) 
print()    
print(nu)



