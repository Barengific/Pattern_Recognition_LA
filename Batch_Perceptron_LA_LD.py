# -*- coding: utf-8 -*-
# linear discriminant function, dichotomizer,
# using batch perceptron learning algorithm
# with augmented notation and sample normalisation
# learning is done after each epoch
# 

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

# a = np.array([[-25],
#               [6],
#               [3]])
a = np.array([-25,
              6,
              3])

lr = 1

y = np.array([[1,1,-1,-1],
              [1,2,-4,-5],
              [5,5,-1,-1]])
# misclassified if, g(x) <= 0

#epoch 1
print("___Epoch1___") 
r,c = y.shape

g = ''
_x = np.array([[0],[0],[0]])
for i in range(0,c):
    g = np.dot(a.transpose(),y[:,i])
    print("***g: ", g)
    if g <= 0:
        _x = np.insert(_x, 1, y[:,i], axis=1)

_r,_c = _x.shape
for i in range(1,_c):    
    a = np.add(a, _x[:,i])
    
a = lr * a
print()    
print("new a: ", a)



#epoch 2
print("___Epoch2___") 
r,c = y.shape

g = ''
_x = np.array([[0],[0],[0]])
for i in range(0,c):
    g = np.dot(a.transpose(),y[:,i])
    print("***g: ", g)
    if g <= 0:
        _x = np.insert(_x, 1, y[:,i], axis=1)

_r,_c = _x.shape
for i in range(1,_c):    
    a = np.add(a, _x[:,i])
    
a = lr * a
print()    
print("new a: ", a)
