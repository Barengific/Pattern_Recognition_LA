# -*- coding: utf-8 -*-
# linear discriminant function, dichotomizer,
# using batch perceptron learning algorithm
# with augmented notation and sample normalisation
# data set

#  x   class
# 1,5    1
# 2,5    1
# 4,1    2
# 5,1    2

# initial values
# a = (w_0,w^t) 
# bpla
# a <- a+lr*sum(y)


import numpy as np

a = np.array([[-25],
              [6],
              [3]])

lr = 1

y = np.array([[1,1,-1,-1],
              [1,2,-4,-5],
              [5,5,-1,-1]])

#epoch 1
r,c = y.shape

g = ''
for i in range(0,c):
    g = np.dot(a.transpose(),y[:,i])
    print(g)

