# -*- coding: utf-8 -*-
# linear discriminant function,
# using sequential MULTICLASS perceptron learning algorithm
# with augmented notation
# learning is done after each data point is misclassified

# data set
#  x   class
# 1,1    1
# 2,0    1
# 0,2    2
# -1,1   2
# -1,-1  3


# initial values
# a = (w_0,w^t) 
# multi-pla
# a <- a+lr*(y_k) - where y_k is a misclassified exemplar

import numpy as np

a1 = np.array([0, 0, 0])
a2 = np.array([0, 0, 0])
a3 = np.array([0, 0, 0])

lr = 1

y = np.array([[1,1,1, 1, 1],
              [1,2,0,-1,-1],
              [1,0,2, 1,-1]])
# misclassified if, g(x) and w are not on the same positive or negative spectrum
# ie. both on the postive or both on negative

w_ = np.array([1,1,2,2,3])


r,c = y.shape
g1 = ''
g2 = ''
g3 = ''


it = 0
#increase epoch amount to reach convergence
for j in range(0,10):
    print("___Epoch___", j+1)            
    for i in range(0,c):
        it = it+1
        print("[it: ", it)
        print("a1: ", a1)
        print("a2: ", a2)
        print("a3: ", a3) 
        print("y: ", y[:,i])          
        g1 = np.dot(a1.transpose(),y[:,i])
        g2 = np.dot(a2.transpose(),y[:,i])
        g3 = np.dot(a3.transpose(),y[:,i])
        print("#g1: ", g1)
        print("#g2: ", g2)
        print("#g3: ", g3)
        print("w: ", w_[i]) 
        
        if g1 == g2 == g3:
            temp1 = (lr*y[:,i])
            a1 = np.add(a1, temp1)
            
            temp1 = (lr*y[:,i])*(-1)
            a3 = np.add(a3, temp1)
            
            continue
        
        if (g1 < (g2 or g3)) and ((w_[i] == 1) and (g2 > 0)) or ((w_[i] == 1) and (g3 > 0)):
            temp1 = (lr*y[:,i])
            a1 = np.add(a1, temp1)
            if g2 > g3:
                temp1 = (lr*y[:,i])*(-1)
                a2 = np.add(a2, temp1)
            elif g3 > 0:
                temp1 = (lr*y[:,i])*(-1)
                a3 = np.add(a3, temp1)
            
        if (g2 < (g1 or g3)) and ((w_[i] == 2) and (g1 > 0)) or ((w_[i] == 2) and (g3 > 0)):
            temp1 = (lr*y[:,i])
            a2 = np.add(a2, temp1)
            if g1 > g3:
                temp1 = (lr*y[:,i])*(-1)
                a1 = np.add(a1, temp1)
            elif g3 > 0:
                temp1 = (lr*y[:,i])*(-1)
                a3 = np.add(a3, temp1)
        
        if (g3 < (g2 or g1)) and ((w_[i] == 3) and (g2 > 0)) or ((w_[i] == 3) and (g1 > 0)):
            temp1 = (lr*y[:,i])
            a3 = np.add(a3, temp1)
            if g1 > g2:
                temp1 = (lr*y[:,i])*(-1)
                a1 = np.add(a1, temp1)
            elif g2 > 0:
                temp1 = (lr*y[:,i])*(-1)
                a2 = np.add(a2, temp1)

    print("")
    print("__a1: ", a1)
    print("__a2: ", a2)
    print("__a3: ", a3)

   
print()    
print("new a1: ", a1)
print("new a2: ", a2)
print("new a3: ", a3)

