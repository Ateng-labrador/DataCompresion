def encode(text, huffman_codes):
    return "".join(huffman_codes[char] for char in text)

def decode(x):
    pass