def left_shifted(x):
    """
    left_shifted
    """
    res = []
    shiffted = 2**(8 - 1)
    for i in range(len(x)):
        row = []
        for j in range(len(x[0])):
            op = int(x[i][j]) - shiffted
            row.append(op)
        res.append(row)
    return res


def ileft_shifted(X):
    """
    Ileft_shifted
    """
    res = []
    shiffted = 2**(8 - 1)
    for i in range(len(X)):
        row = []
        for j in range(len(X[0])):
            op = X[i][j] + shiffted
            row.append(op)
        res.append(row)
    return res

    


