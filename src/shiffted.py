def left_shifted(x):
    """
    left_shifted
    """
    res = []
    shiffted = 2**(8 - 1)
    for i in range(len(x)):
        row = []
        for j in range(len(x[0])):
            op = x[i][j] - shiffted
            row.append(op)
        res.append(row)
    return res


