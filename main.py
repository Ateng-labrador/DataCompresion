import matplotlib.pyplot as plt
import math


def evenSmetrri(x):
    res = []
    for i in range(len(x)):
        res.append(x[i])
    for i in range(len(x) - 2, 0, -1):
        res.append(x[i])
    return res

def sinFrame(x):
    res = []
    for k in range(len(x)):
        row = 0
        for n in range(len(x)):
            row += x[n] * math.sin(2 * math.pi * k * n / len(x))
        res.append(row)
    return [round(val, 10) for val in res]

def cosFrame(x):
    res = []
    for k in range(len(x)):
        row = 0
        for n in range(len(x)):
            row += x[n] * math.cos(2 * math.pi * k * n / len(x))
        res.append(row)
    return res


x1 = [i for i in range(5)]
x2 = evenSmetrri(x1)
y = sinFrame(x2)
yc = cosFrame(x2)
print(yc)
 