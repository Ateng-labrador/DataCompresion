def encode(text, huffman_codes):
    return "".join(huffman_codes[char] for char in text)

def decode1(encoded_text, root):
    if not root:
        return []

    if root.char is not None:
        return [root.char for _ in encoded_text]

    decode_text = []
    current = root
    for bit in encoded_text:
        current = current.left if bit == '0' else current.right

        if current.char is not None:
            decode_text.append(current.char)
            current = root
    return decode_text

def decode(encoded_text, codes):
    reverse_codes = {v: k for k, v in codes.items()}

    decoded_text = []
    current_bit = ""

    for bit in encoded_text:
        current_bit += bit
        if current_bit in reverse_codes:
            decoded_text.append(reverse_codes[current_bit])
            current_bit = ""
    return decoded_text
