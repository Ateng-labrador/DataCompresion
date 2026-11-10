import math

SCALE_FACTOR = [2.0 / (2.0 ** (i/3.0)) for i in range(63)]

def scale_factor_idx(max_abs_val):
    if max_abs_val == 0:
        return 62

    for idx, sf_val in enumerate(scale_factor):
        if sf_val >= max_abs_val and (
            idx == 62 or scale_factor[idx + 1] < max_abs_val
        ):
            return idx
    return 0

def scale_factor(x):
    res = []
    for i in range(0, len(x), 12):
        cutt = x[i : i + 12]
        max_abs = max(abs(val) for val in cutt)
        sf_index = scale_factor_idx(max_abs)
        sf_value = SCALE_FACTOR[sf_index]

        res.append({sf_index, sf_value})
    return res
     

