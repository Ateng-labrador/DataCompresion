import math

# encode
def generate_filterbank(h, M):
    """
    (encoder)
    h : list/array prototipe
    M : jumlah subband
    """
    N = len(h)
    filterbank = []
    for m in range(M):
        subfilter = []
        for n in range(N):
            op = h[n] * math.cos(((math.pi/M) * (m + 0.5) * (n - (N - 1)/2)))
            subfilter.append(op)
        filterbank.append(subfilter)
    return filterbank

# encode
def analyze_subbands(x, filterbank, M):
    """
    
    """
    subband_outputss = []
    N = len(filterbank[0])
    for h_m in filterbank:
        y_m = []
        for i in range(0, len(x) - N + 1, M):
            res = 0
            for n in range(N):
                res += x[i + n] * h_m[N - 1 - n]
            y_m.append(res)
        subband_outputss.append(y_m)
    return subband_outputss
    

def generate_synthesis_filterbank(h, M):
    """
    
    """
    N = len(h)
    filterbank = []
    for m in range(M):
        subfilter = []
        for n in range(N):
            op = (2/M) *  h[n] * math.cos(((math.pi/M) * (m + 0.5) * (n - (N - 1)/2)))
            subfilter.append(op)
        filterbank.append(subfilter)
    return filterbank
    
