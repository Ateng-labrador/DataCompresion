from . import matrix_pip as mp


def zigzag_scan(x):
    res = []
    for r, c in mp.ZIGZAG_INDICES:
        res.append(x[r][c])
    return res
