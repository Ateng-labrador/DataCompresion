from src import dct, huffmancode, matrix_pip
import numpy as np
import cv2

img = cv2.imread('sampel.jpg', cv2.IMREAD_GRAYSCALE)
h, w = img.shape

img_shifted = dct.subtracted(img)

simbol = []

for i in range(0, h - h % 8, 8):
    for j in range(0, w - w % 8, 8):
        block = img_shifted[i:i+8, j:j+8]

        # Step 1: 2D - DCT
        dct_block = dct.dct2d(block)

        # Step 2: Kuantisasi
        quantized_block = np.round(dct_block / matrix_pip.Q_MATRIX).astype(int)

        # Step 3: Pemindaian Zig - Zag
        vector_1d = [quantized_block[r, c] for r, c in matrix_pip.ZIGZAG_INDICES]

        simbol.extend(vector_1d)

root, codebook = huffmancode.build_huffman_tree(simbol)
bitstream = huffmancode.encode(simbol, codebook)

ukuran_asli_bits = h * w * 8
ukuran_terkompresi_bits = len(bitstream)

print(f"Ukuran Asli Gambar    : {ukuran_asli_bits} bits")
print(f"Ukuran Terkompresi     : {ukuran_terkompresi_bits} bits")
print(f"Rasio Kompresi         : {ukuran_asli_bits / ukuran_terkompresi_bits:.2f}x")
        




