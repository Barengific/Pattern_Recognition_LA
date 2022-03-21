# -*- coding: utf-8 -*-
# linear discriminant function, dichotomizer,
# using SEQUENTIAL perceptron learning algorithm
# with augmented notation and sample normalisation
# squential learning is done after each data point is misclassified


# data set
#  x   class
# 1,5    1
# 2,5    1
# 4,1    2
# 5,1    2

# initial values
# a = (w_0,w^t) 
# bpla
# a <- a+lr*(y_k) - where y_k is a misclassified exemplar

import numpy as np

a = np.array([-25, 6, 3])

lr = 1

y = np.array([[1,1,-1,-1],
              [1,2,-4,-5],
              [5,5,-1,-1]])
# misclassified if, g(x) <= 0

#epoch 1
print("___Epoch1___") 
r,c = y.shape

g = ''

for i in range(0,c):
    g = np.dot(a.transpose(),y[:,i])
    print("***g: ", g)
    if g <= 0:
        a = np.add(a, y[:,i])
   
a = lr * a
print()    
print("new a: ", a)

