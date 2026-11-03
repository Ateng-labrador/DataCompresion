import cmath
import math
from scipy.io import wavfile
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
import numpy as np

def SineWindow(x):
    """
    Windowing scale
    """
    res = []
    for i in range(len(x)):
        row = x[i] * math.sin(math.pi*(i + 0.5)/len(x))
        res.append(row)
    return res

def process_full_audio(x, N=1024, M=512):
    """
    Farming
    """
    window_frames = []

    for start in range(0, len(x) - N + 1, M):
        frame = x[start:start + N]

        window_frame = SineWindow(frame)

        window_frames.append(window_frame)
    return window_frames

def dft(x):
    res = []
    for k in range(len(x)):
        row = 0.0
        for n in range(len(x)):
            angle = -1j * 2 * math.pi * (k/len(x))*n
            row += x[n] * cmath.exp(angle)
        res.append(row)
    return res


def dct_II(x):
    res = []
    for k in range(len(x)):
        row = 0.0
        for n in range(len(x)):
            if k == 0:
                beta = 1/math.sqrt(2)
            else:
                beta = 1
            angle = (math.pi * k * (2*n + 1))/(2*len(x))
            row += math.sqrt(2/len(x)) * beta * x[n] * math.cos(angle)
        res.append(row)
    return res


def mdct(x):
    res = []
    for k in range(len(x)//2):
        row = 0.0
        for n in range(len(x)):
            angle = ((2 * math.pi / len(x))*(k + 0.5)*(n + 0.5 + len(x)/4))
            row += x[n] * math.cos(angle)
        res.append(row)
    return res

samplerate, data = wavfile.read("nada_1.wav")
data_potong = data[120000:150000]
data_bersih = data_potong[0:512]


data_new = process_full_audio(data_potong, N=512, M=256)


data_dft = [dft(i) for i in data_new]
data_mdct = [mdct(i) for i in data_new]
data_dct = [dct_II(i) for i in data_new]

N = 256
fs = samplerate

k = np.arange(N)
freq_hz = (k) * fs / N

magnitudo = np.abs(data_mdct[0]) * 2 / N
plt.plot(freq_hz, magnitudo)
plt.show()

