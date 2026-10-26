import math
import numpy as np


def dct_I(x):
    """
    
    """
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
    """
    
    """
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
    """
    
    """
    C = np.zeros((len(X), len(X)))
    for k in range(len(X)):
        if k == 0:
            beta = 1/np.sqrt(2)
        else:
            beta = 1
        for n in range(len(X)):
            angle = (np.pi*k*(2*n+1))/(2*len(X))
            C[k, n] = np.sqrt(2/len(X)) * beta * np.cos(angle)
    return C.T @ X @ C


def mdct(x):
    """
    
    """
    res = []
    for k in range(len(x)//2):
        op = 0
        for n in range(len(x)):
            angle = ((2*math.pi / len(x)) * (k + 0.5) * (n + 0.5 + len(x)/4))
            op += x[n] * math.cos(angle)
        res.append(op)
    return res
            

def imdct(X):
    """
    
    """
    res = []
    for k in range(len(X) * 2):
        op = 0
        for n in range(len(X)):
            angle = ((2*math.pi / len(X)) * (k + 0.5) * (n + 0.5 + len(X)/4))
            op += 2/len(X) * X[n] * math.cos(angle)
        res.append(op)
    return res

