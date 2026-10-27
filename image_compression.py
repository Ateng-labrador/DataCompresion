import numpy as np
from src import shiffted, dct_new, huffmancode, quantization, zigzag_scan, code, matrix_pip
import cv2
import src.quantization

def encode(img):
    h, w = img.shape

    result_img = []
    for i in range(0, h - h % 8, 8):
        for j in range(0, w - w % 8, 8):
            # potong block 8 x 8
            block_8x8 = img[i:i+8, j:j+8]
            # shifted
            shifted_block = shiffted.left_shifted(block_8x8)
            # 2d-DCT 
            dct_block = dct_new.dct_II(shifted_block)
            # kuantisasi
            quantized_block = quantization.quantization(dct_block)
            # Zig-zag scanning (Matriks 8 x 8)
            vector_1d = zigzag_scan.zigzag_scan(quantized_block)
            # kumpulkan ke list utama
            result_img.extend(vector_1d)
    codes = huffmancode.huffman_code_array1(result_img)
    bitstream = code.encode(result_img, codes)
    return bitstream, codes, (h, w)


def decode(bitstream, codes, shape):
    h, w = shape

    simbol_1d = code.decode(bitstream, codes)

    reconstructed_img = np.zeros((h, w))
    idx = 0

    for i in range(0, h - h % 8, 8):
        for j in range(0, w - w % 8, 8):
            # rekonstruksi rce / dpcm
            block_8x8 = simbol_1d[idx : idx + 64]
            idx += 64

            # Inverse Zig-Zag (Vektor 1D -> Matriks 8 x 8)
            quantized_block = zigzag_scan.invers_zigzag_scan(block_8x8)

            # Dequantization (Perkalian elemen dengan Q_Matriks)
            dct_block = quantized_block * matrix_pip.Q_MATRIX

            # Inverse 2D-DCT
            shiffted_block = dct_new.idct_II(dct_block)

            # Inverse Level Shift
            block_8x8 = shiffted.ileft_shifted(shiffted_block)

            # save the image
            reconstructed_img[i:i+8, j:j+8] = block_8x8
    return np.clip(reconstructed_img, 0 , 255).astype(np.uint8)

image = cv2.imread('sampel.jpg')

img_ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

decoded_channels = []
for c in range(3):
    channel_data = img_ycrcb[:, :, c]

    bitstream, codes, size = encode(img=channel_data)

    recon_channel = decode(bitstream=bitstream, codes=codes, shape=size)

    decoded_channels.append(recon_channel)

img_ycrcb_recon = cv2.merge(decoded_channels)

img_new = cv2.cvtColor(img_ycrcb_recon, cv2.COLOR_YCR_CB2BGR)

cv2.imwrite('hasil_rekonstruksi_berwarna.jpeg', img_new)