from src import dct, huffmancode, matrix_pip
import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('sampel.jpg', cv2.IMREAD_GRAYSCALE)
h, w = img.shape

img_shifted = dct.subtracted(img)

simbol = []


# Encoding Process
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

# ukuran_asli_bits = h * w * 8
# ukuran_terkompresi_bits = len(bitstream)

# print(f"Ukuran Asli Gambar    : {ukuran_asli_bits} bits")
# print(f"Ukuran Terkompresi     : {ukuran_terkompresi_bits} bits")
# print(f"Rasio Kompresi         : {ukuran_asli_bits / ukuran_terkompresi_bits:.2f}x")
        

# Decoding Process

def rekonstruksi_gambar(bitstream, root, shape_gambar):
    h, w = shape_gambar

    simbol_terkode = huffmancode.decode(bitstream, root)
    img_recpnstructe = np.zeros((h, w), dtype=float)
    idx = 0
    for i in range(0, h - h % 8, 8):
        for j in range(0, w - w % 8, 8):
            block_vector = simbol_terkode[idx : idx + 64]
            idx += 64

            quantized_block = np.zeros((8, 8), dtype=int)
            for k, (r, c) in enumerate(matrix_pip.ZIGZAG_INDICES):
                quantized_block[r, c] = block_vector[k]

            dct_block = quantized_block * matrix_pip.Q_MATRIX

            spatial_block = dct.idct2d(dct_block)

            img_recpnstructe[i:i+8, j:j+8] = np.asarray(spatial_block) + 128.0
    img_recpnstructe = np.clip(img_recpnstructe, 0, 255).astype(np.uint8)
    return img_recpnstructe

img_hasil = rekonstruksi_gambar(bitstream, root, (h, w))

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Gambar Asli")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Hasil Rekonstruksi (Post-Encoding & Decoding)")
plt.imshow(img_hasil, cmap='gray')
plt.axis('off')

plt.show()
