# -*- coding: utf-8 -*-

#augmented feature space, dichotomizer, linear discriminant function
# g(x) = a^t *y
# y = (1, x)

import numpy as np

a = np.array([[-3],
              [1],
              [2],
              [2],
              [2],
              [4]])

y1 = np.array([[1],
              [0],
              [-1],
              [0],
              [0],
              [1]])

y2 = np.array([[1],
              [1],
              [1],
              [1],
              [1],
              [1]])

g = np.dot(a.transpose(),y1)
print(g)

g = np.dot(a.transpose(),y2)
print(g)



