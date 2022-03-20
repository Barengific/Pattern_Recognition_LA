# -*- coding: utf-8 -*-
#Dichotomizer 2D feature space quadratic discriminant function
#g(x) = x^t *A*x +x^t *b +c 

import numpy as np

# i)
x1 = np.array([[0],
              [-1]])

x2 = np.array([[1],
              [1]])

A = np.array([[2, 1],
              [1, 4]])

b = np.array([[1],
              [2]])

c = -3

g = np.dot(np.dot(x1.transpose(),A),x1) +(np.dot(x1.transpose(),b)) +(c)
print(g)

g = np.dot(np.dot(x2.transpose(),A),x2) +(np.dot(x2.transpose(),b)) +(c)
print(g)



# ii)
x1 = np.array([[0],
              [-1]])

x2 = np.array([[1],
              [1]])

A = np.array([[-2, 5],
              [5, -8]])

b = np.array([[1],
              [2]])

c = -3


g = np.dot(np.dot(x1.transpose(),A),x1) +(np.dot(x1.transpose(),b)) +(c)
print(g)

g = np.dot(np.dot(x2.transpose(),A),x2) +(np.dot(x2.transpose(),b)) +(c)
print(g)
