#dichotomizer - linear discriminant function
#g(x) = w^t *x + w_0
#if g(x) > 0 then class 1 otherwise class 2

import numpy as np

w = np.array([[2],[1]])
w_0 = -5
x = np.array([[1,2,3],
              [1,2,3]])

g = np.dot(w.transpose(),x)+w_0
# print(g)




# augmented feature space
#g(x) = a^t *y
# if g(x) > 0 then class 1 otherwise class 2

a = np.array([[-5],
              [2],
              [1]])

y = np.array([[1,1,1],
              [1,2,3],
              [1,2,3]])

g = np.dot(a.transpose(),y)
print(g)



