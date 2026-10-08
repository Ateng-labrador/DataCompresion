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


def idct1(X):
    res = [0] * len(X)
    for n in range(len(X)):
        for k in range(len(X)):
            if k == 0 or k == len(X) - 1:
                alpha = 1/2
            else:
                alpha = 1
            res[n] += (1/(len(X) - 1)) * alpha * X[k] * math.cos((math.pi * k * n) / (len(X) - 1))
    return res

 
def idct2(X):
    res = [0] * len(X)
    for n in range(len(X)):
        for k in range(len(X)):
            if k == 0:
                beta = 1/2
            else:
                beta = 1
            res[n] += (2/len(X)) * beta * X[k] * math.cos((math.pi * k * (2 * n + 1)) / (2 * len(X)))
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


def idct2d(G):
    H = len(G)
    W = len(G[0])
    res = [[0.0 for _ in range(W)] for _ in range(H)]

    for x in range(H):
        for y in range(W):
            sum_val = 0.0


            for u in range(H):
                for v in range(W):
                    alpha_u = 1 / math.sqrt(2) if u == 0 else 1.0
                    alpha_v = 1 / math.sqrt(2) if v == 0 else 1.0


                    cos_x = math.cos((2 * x + 1) * u * math.pi / (2 * H))
                    cos_y = math.cos((2 * y + 1) * v * math.pi / (2 * W))
                    sum_val += alpha_u * alpha_v * G[u][v] * cos_x * cos_y
            res[x][y] = 0.25 * sum_val
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
    [52.0, 55.0, 61.0, 66.0, 70.0, 61.0, 64.0, 73.0],
    [63.0, 59.0, 55.0, 90.0, 109.0, 85.0, 69.0, 72.0],
    [62.0, 59.0, 68.0, 113.0, 144, 104.0, 66.0, 73.0],
    [63.0, 58.0, 71.0, 122.0, 154, 106.0, 70.0, 69.0],
    [67.0, 61.0, 68.0, 104.0, 126.0, 88.0, 68.0, 70.0],
    [79.0, 65.0, 60.0, 70.0, 77.0, 68.0, 58.0, 75.0],
    [85.0, 71.0, 64.0, 59.0, 55.0, 61.0, 65.0, 83.0],
    [87.0, 79.0, 69.0, 68.0, 65.0, 76.0, 78.0, 94.0],
]

# x = subtracted(g)

# x = [1, 2, 3, 4, 5, 6, 7, 8]

# dc = dct1(x) 
# dci = idct1(dc)

# dc2 = dct2(x)
# dci2 = idct2(dc2)

# print(x)
# print(dci)


# print(x)
# print(dci2)

dc2d = dct2d(g)
tidc2d = idct2d(dc2d)

print(g)
print('\n')
print(tidc2d)