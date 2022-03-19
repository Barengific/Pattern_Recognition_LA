#3D feature space quadratic discriminant function
#g(x) = x_1^2 -x_3^2 +2x_2 *x_3 +4x_1 *x_2 +3x_1 -2x_2+2

import numpy as np

# x = np.array([[0],
#               [1],
#               [1],
#               [1]])

# g = (x[1]^2) -(x[3]^2) +(2*x[2]*x[3]) +(4*x[1]*x[2]) +(3*x[1]) -(2*x[2]) +2
# print(g)


x = np.array([[0],
              [-1],
              [0],
              [3]])

g = (x[1]^2) -(x[3]^2) +(2*x[2]*x[3]) +(4*x[1]*x[2]) +(3*x[1]) -(2*x[2]) +2
print(g)



x = np.array([[0],
              [-1],
              [0],
              [0]])

g = (x[1]^2) -(x[3]^2) +(2*x[2]*x[3]) +(4*x[1]*x[2]) +(3*x[1]) -(2*x[2]) +2
print(g)