import cmath
import math
import numpy as np

def dct1(x):
    res = [0] * len(x)
    for k in range(len(x)):
        for n in range(len(x)):
            if n == 0 or n == len(x) - 1:
                alpha = 1/2
            else:
                alpha = 1
            res[k] += 2 * alpha * x[n] * math.cos(cmath.pi * k * n / (len(x)- 1))
    return res

def dct2(x):
    res = [0] * len(x)
    for k in range(len(x)):
        for n in range(len(x)):
            res[k] += 2 * x[n] * math.cos(cmath.pi * k * (2 * n+1) / (2 * len(x)))
    return res



def dct2d(g):
    H = len(g)
    W = len(g[0])
    res = [[0.0 for _ in range(W)] for _ in range(H)]

    for u in range(H):
        for v in range(W):
            alpha_u = 1 / math.sqrt(2) if u == 0 else 1
            alpha_v = 1 / math.sqrt(2) if v == 0 else 1

            sum_val = 0.0
            for x in range(H):
                for y in range(W):
                    cos_x = math.cos((2 * x + 1) * u * math.pi / (2 * H))
                    cos_y = math.cos((2 * y + 1) * v * math.pi / (2 * W))
                    sum_val += g[x][y] * cos_x * cos_y
            res[u][v] = 0.25 * alpha_u * alpha_v * sum_val
    return res

def subtracted(x):
    res = []
    for i in range(len(x)):
        row = []
        for j in range(len(x[0])):
            P_new = x[i][j] - 128.0
            row.append(P_new)
        res.append(row)
    return np.array(res)
            

g = [
    [52, 55, 61, 66, 70, 61, 64, 73],
    [63, 59, 55, 90, 109, 85, 69, 72],
    [62, 59, 68, 113, 144, 104, 66, 73],
    [63, 58, 71, 122, 154, 106, 70, 69],
    [67, 61, 68, 104, 126, 88, 68, 70],
    [79, 65, 60, 70, 77, 68, 58, 75],
    [85, 71, 64, 59, 55, 61, 65, 83],
    [87, 79, 69, 68, 65, 76, 78, 94],
]

# x = subtracted(g)
# dc = dct2d(x) 
# print(dc)
