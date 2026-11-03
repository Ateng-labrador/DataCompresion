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



data_new = process_full_audio(data_potong, N=512, M=256)

# 512
data_dft = [dft(i) for i in data_new]
# 512
data_dct = [dct_II(i) for i in data_new]
# 256
data_mdct = [mdct(i) for i in data_new]


N1 = 512
N2 = 512
N3 = 256
fs = samplerate

k1 = np.arange(N1)
k2 = np.arange(N2)
k3 = np.arange(N3)

freq_hz1 = (k1) * fs / N1
freq_hz2 = (k2) * fs / N2
freq_hz3 = (k3) * fs / N3


magnitudo1 = np.abs(data_dft[0]) * 2 / N1
magnitudo2 = np.abs(data_dct[0]) * 2 / N2
magnitudo3 = np.abs(data_mdct[0]) * 2 / N3

peaks_1, _ = find_peaks(magnitudo1, height=1000)
peaks_2, _ = find_peaks(magnitudo2, height=500)
peaks_3, _ = find_peaks(magnitudo3, height=500)

fig, axis = plt.subplots(1, 3)
axis[0].plot(freq_hz1, magnitudo1)
axis[0].set_title('Spektrum DFT')
axis[0].scatter(freq_hz1[peaks_1], magnitudo1[peaks_1], color='red')
for p in peaks_1:
    axis[0].annotate(
        f"{freq_hz1[p]:.2f}",
        xy=(freq_hz1[p], magnitudo1[p]),
        xytext=(0, 8),
        textcoords="offset points",
        ha="center"
    )


axis[1].plot(freq_hz2, magnitudo2)
axis[1].set_title('Spektrum DCT')
axis[1].scatter(freq_hz2[peaks_2], magnitudo2[peaks_2], color='red')
for p in peaks_2:
    axis[1].annotate(
        f"{freq_hz2[p]:.2f}",
        xy=(freq_hz2[p], magnitudo2[p]),
        xytext=(0, 8),
        textcoords="offset points",
        ha="center"
    )


axis[2].plot(freq_hz3, magnitudo3)
axis[2].set_title('Spektrum MDCT')
axis[2].scatter(freq_hz3[peaks_3], magnitudo3[peaks_3], color='red')
for p in peaks_3:
    axis[2].annotate(
        f"{freq_hz3[p]:.2f}",
        xy=(freq_hz3[p], magnitudo3[p]),
        xytext=(0, 8),
        textcoords="offset points",
        ha="center"
    )

plt.tight_layout()
plt.show()

