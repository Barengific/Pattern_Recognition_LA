# -*- coding: utf-8 -*-
# NN - lws
# transfer function - linear weighted sum of its input
# activation function - heaviside function

# weights - w = [0.1, -0.5, 0.4]

import numpy as np

#weights
w = np.array([0.1, -0.5, 0.4])

#inputs
x1 = np.array([[0.1], [-0.5], [0.4]])
x2 = np.array([[0.1], [0.5],  [0.4]])

#y = H(wx)
y1 = np.dot(w,x1)
y2 = np.dot(w,x2)

# print(y1)
# print(y2)

y1 = np.heaviside(y1,1)
y2 = np.heaviside(y2,1)
print(y1)
print(y2)