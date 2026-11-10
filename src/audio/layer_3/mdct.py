import math
import cmath


def mdct(x):
    """
    
    """
    res = []
    for k in range(len(x)//2):
        row = 0.0
        for n in range(len(x)):
            angle = ((2 * math.pi / len(x))*(k + 0.5)*(n + 0.5 + len(x)/4))
            row += x[n] * math.cos(angle)
        res.append(row)
    return res
