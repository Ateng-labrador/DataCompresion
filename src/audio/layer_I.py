import math
import cmath


def dft(x):
    N = len(x)
    res = []
    for f in range(len(x)):
        row = 0.0 + 0.0j
        for n in range(len(x)):
            con = -11j * 2 * math.pi * f * n / len(x)
            row += x[n] * cmath.exp(con)
        res.append(row)
    return res




def Z_transform(x, z):
    x_z = 0.0 + 0.0j
    for n in range(len(x)):
        x_z += x[n] * (z ** (-n))
    return x_z


def down_sampling(x):
    res = []
    for n in range(len(x)):
        row = 0.0
        for k in range(len(x)):
            con = -1j * 2 * math.pi * k / len(x)
            row += 1/len(x)


def up_sampling(x):
    pass

