import math
import numpy as np
# 2D AXA^T


def dct_I(x):
    res = [0] * len(x)
    for k in range(len(x)):
        for n in range(len(x[0])):
            if n == 0 or n == len(x) - 1:
                alpha = 0.5
            else:
                alpha = 1
            angle = math.cos((math.pi*k*n)/(len(x) - 1))
            res += 2 * alpha * x[n] * angle
    return res


def dct_II(x):
    C = np.zeros((len(x), len(x)))
    for k in range(len(x)):
        if k == 0:
            beta = 1/np.sqrt(2)
        else:
            beta = 1
        for n in range(len(x)):
            angle = (np.pi*k*(2*n+1))/(2*len(x))
            C[k, n] = np.sqrt(2/len(x)) * beta * np.cos(angle)
    return C @ x @ C.T
    

def idct_II(X):
    C = np.zeros((len(X), len(X)))
    for n in range(len(X)):
        if n == 0:
            beta = 1/np.sqrt(2)
        else:
            beta = 1
        for k in range(len(X)):
            angle = (np.pi*n*(2*n+1))/(2*len(X))
            C[n, k] = np.sqrt(2/len(X)) * beta * np.cos(angle)
    return C @ X @ C.T


