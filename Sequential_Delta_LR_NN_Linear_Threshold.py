# -*- coding: utf-8 -*-
# NN - ltu
# transfer function - linear threshold unit
# activation function - heaviside function
# sequential delta learning rule
# delta - w <- w+lr(t-y)x -t target -y output
# using augmented notation

# sigma = 1.5
# w_1 = 2
# weights - w = [-sigma, w_1]
# weights - w = [-1.5, 2]

import numpy as np

#weights
w = np.array([-1.5, 2])
lr = 1

#inputs
# x = [1,x_1]
x1 = np.array([[1, 0], 
               [1, 1]])
t = np.array([1,0])

it = 0
r,c = x1.shape

for i in range(0,15):
    for j in range(0,r):
        # print("x1: ", x1[j])
        # print("t: ", t[j])
        # print("x1: ", x1[j])
        #y = H(wx)
        y = np.heaviside(np.dot(w,x1[j,:]),1)
        t_y = t[j]-y
        temp1 = lr*t_y*x1[j,:]
        w = w+temp1
        print(w)
    


print()
