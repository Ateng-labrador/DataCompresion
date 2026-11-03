import math
import cmath


# Filter bank

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

# encoderr
def down_sampling(x, K):
    return x[::K]

# decoder
def up_sampling(X_freq, K):
    Y_freq = []
    for f in range(len(X_freq)//K):
        sum_terms = 0.0 + 0.0j
        for r in range(K):
            idx = (f + r * (len(X_freq)//K)) % len(X_freq)
            sum_terms += X_freq[idx]
        Y_freq.append(sum_terms/K)
    return Y_freq

