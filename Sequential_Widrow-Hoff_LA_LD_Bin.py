# -*- coding: utf-8 -*-
# linear discriminant function,
# using sequential MULTICLASS perceptron learning algorithm
# with augmented notation
# learning is done after each data point is misclassified

# data set
#  x   class
# 0,1    1
# 1,2    1
# 2,1    1
# -3,1   -1
# -2,-1  -1
# -3,-2  -1

# initial values
# a = (w_0,w^t) 
# multi-pla
# a <- a+lr*(b_k-(a*y_k)y_k - where y_k is a misclassified exemplar
# a = parameters
# b = margin vector

import numpy as np

a = np.array([1, 0, 0])
b = np.array([1, 1, 1, 1, 1, 1])

lr = 0.1

y = np.array([[1,1,1,-1,-1,-1],
              [0,1,2, 3, 2, 3],
              [2,2,1,-1, 1, 2]])
# misclassified if, g(x) and w are not on the same positive or negative spectrum
# ie. both on the postive or both on negative

r,c = y.shape
g = ''

it = 0
#increase epoch amount to reach convergence
for j in range(0,10):
    print("___Epoch___", j+1)            
    for i in range(0,c):
        it = it+1
        print("[it: ", it)
        print("a: ", a)
        print("y: ", y[:,i])          
        g = np.dot(a.transpose(),y[:,i])
        print("g: ", g)
        
        temp1 = lr*(b[i]-g)*y[:,i]
        a = np.add(a, temp1)
        
    print("")
    print("__a: ", a)
   
print()    
print("new a: ", a)


