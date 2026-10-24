import numpy as np
from src import shiffted, dct_new, huffmancode, quantization, zigzag_scan, code
import cv2
import src.quantization


image = cv2.imread('sampel.jpg', cv2.IMREAD_GRAYSCALE)

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
    pass

x, y , z= encode(image)
print(z)
    


