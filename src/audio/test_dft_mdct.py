import cmath
import math
from scipy.io import wavfile
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
import numpy as np


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

N_1 = 512
N_2 = 256
N_3 = 512
fs = samplerate
freq_1 = np.arange(N_1) * fs / N_1
freq_2 = np.arange(N_2) * fs / N_2
freq_3 = np.arange(N_3) * fs / N_3


data_dft = dft(data_bersih)
data_mdct = mdct(data_bersih)
data_dct = dct_II(data_bersih)


magnitude_1 = 2 * np.abs(data_dft) / N_1
magnitude_2 = 2 * np.abs(data_mdct) / N_2
magnitude_3 = 2 * np.abs(data_dct) / N_3

peaks_1, _ = find_peaks(magnitude_1, height=1000)
peaks_2, _ = find_peaks(magnitude_2, height=10000)
peaks_3, _ = find_peaks(magnitude_2, height=10000)


fig, axis = plt.subplots(2, 2)
axis[0, 0].plot(freq_1, magnitude_1)
axis[0, 0].scatter(freq_1[peaks_1], magnitude_1[peaks_1], color='red')
for p in peaks_1:
    axis[0, 0].annotate(
        f"{freq_1[p]:.2f}",
        xy=(freq_1[p], magnitude_1[p]),
        xytext=(0, 8),
        textcoords="offset points",
        ha="center"
    )


axis[0, 1].plot(freq_2, magnitude_2)
axis[0, 1].scatter(freq_2[peaks_2], magnitude_1[peaks_2], color='red')
for p in peaks_2:
    axis[0, 1].annotate(
        f"{freq_2[p]:.2f}",
        xy=(freq_2[p], magnitude_2[p]),
        xytext=(0, 8),
        textcoords="offset points",
        ha="center"
    )

axis[1, 0].plot(freq_3, magnitude_3)
axis[1, 0].plot(freq_3[peaks_3], magnitude_3[peaks_3], color='red')
for p in peaks_3:
    axis[1, 0].annotate(
        f"{freq_3[p]:.2f}",
        xy=(freq_3[p], magnitude_3[p]),
        xytext=(0, 8),
        textcoords="offset points",
        ha="center"
    )

plt.tight_layout()
plt.show()
