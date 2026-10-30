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
    
# decode
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

# decode
def synthesize_subbands(subband_inputs, synthesis_filterbank, M):
    """
    
    """
    N = len(synthesis_filterbank[0])
    L = len(subband_inputs[0])

    # Panjang akhir sinyal
    total_length = L * M + N - 1
    reconstructed_audio = [0.0] * total_length

    for m in range(M):
        g_m = synthesis_filterbank[m]
        subband_data = subband_inputs[m]

        # Upsampling
        upsampled_signal = [0.0] * (L * M)
        for idx, sample in enumerate(subband_data):
            upsampled_signal[idx * M] = sample

        # Filtering & Summation
        for i in range(len(upsampled_signal)):
            for n in range(N):
                reconstructed_audio[i + n] += upsampled_signal[i] * g_m[n]
    
    return reconstructed_audio
