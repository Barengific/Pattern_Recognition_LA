# -*- coding: utf-8 -*-
# linear discriminant function,
# using SEQUENTIAL perceptron learning algorithm
# with augmented notation and sample normalisation
# learning is done after each data point is misclassified


# data set
#  x   class
# 0,2    1
# 1,2    1
# 2,1    1
# -3,1     -1
# -2,-1    -1
# -3,-2    -1

# initial values
# a = (w_0,w^t) 
# bpla
# a <- a+lr*(y_k) - where y_k is a misclassified exemplar

import numpy as np

a = np.array([1, 0, 0])

lr = 1

y = np.array([[1,1,1, 1, 1, 1],
              [0,1,2,-3,-2,-3],
              [2,2,1, 1,-1,-2]])
# misclassified if, g(x) and w are not on the same positive or negative spectrum
# ie. both on the postive or both on negative

w_ = np.array([1,1,1,-1,-1,-1])


r,c = y.shape
g = ''

it = 0
for j in range(0,3):
    print("___Epoch___", j+1)
    for i in range(0,c):
        print()
        print()
        it = it+1
        print("***___it: ", it)
        print("___a: ", a)
        print("___y: ", y[:,i])
        
        g = np.dot(a.transpose(),y[:,i])
        print("___g: ", g)
        #print("***yi: ", y[:,i])
        print("___w: ", w_[i])
        
        if ((g > 0) and (w_[i] == -1)) or  ((g <= 0) and (w_[i] == 1)):
            temp1 = (lr*w_[i])*y[:,i]
            #print("tempppp____", temp1)
            a = np.add(a, temp1)
        print("___a: ", a)
   
print()    
print("new a: ", a)

