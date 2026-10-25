import numpy as np
from . import matrix_pip as mp


def zigzag_scan(x):
    """
    
    """
    res = []
    for r, c in mp.ZIGZAG_INDICES:
        res.append(x[r][c])
    return res


def invers_zigzag_scan(X):
    """
    
    """
    matrix_2d = np.zeros((8, 8), dtype=int)
    for idx, (r, c) in enumerate(mp.ZIGZAG_INDICES):
        matrix_2d[r, c] = X[idx]
    return matrix_2d
