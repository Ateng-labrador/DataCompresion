from . import matrix_pip as mp
import math

def quantization(x):
    """
    
    """
    res = []
    for i in range(len(x)):
        row = []
        for j in range(len(x[0])):
            op = int(math.floor((x[i][j]/mp.Q_MATRIX[i][j])) + 0.5)
            row.append(op)
        res.append(row)
    return res
