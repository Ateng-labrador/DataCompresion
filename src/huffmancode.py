import heapq

class Node:
    # Node
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    # cout freq char
    """
    freq.get(i, 0) + 1: Memeriksa apakah karakter i sudah ada di dalam dictionary
        - Jika belum ada, fungsi .get(i, 0) akan mengembalikan nilai awal 0.
        - Jika sudah ada, .get(i, 0) akan mengambil nilai frekuesi yaang sudah
        tercatat sebelumnya
        - Nilai tersebut ditambah 1, lalu disimpan kembali ke freq[i]
    """
    if not text:
        return None, {}

    freq = {}
    for i in text:
        freq[i] = freq.get(i, 0) + 1

    heap = [Node(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)

    # marge two small node until 1 root
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)
    root = heap[0]

    huffman_codes = {}
    def generate_codes(node, current_code=""):
        if node is None:
            return
        if node.char is not None:
            huffman_codes[node.char] = current_code or "0"
            return
        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")
    generate_codes(root)
    return root, huffman_codes

# Proses mengubah tekst asli ke angka biner yang sudah terkompresi 
def encode(text, huffman_codes):
    return "".join(huffman_codes[char] for char in text)


# Proses mengubah code hasil biner menjadi teks asli
def decode(encoded_text, root):
    if not root:
        return []

    if root.char is not None:
        return [root.char for _ in encoded_text]

    decoded_text = []
    current = root
    for bit in encoded_text:
        current = current.left if bit == '0' else current.right

        if current.char is not None: # Daun ditemukan
            decoded_text.append(current.char)
            current = root
    return decoded_text


# text = "KHANSA"
# root, codes = build_huffman_tree(text)

# encoded = encode(text, codes)
# decoded = decode(encoded, root)

# print(f"\nTeks Asli     : {text}")
# print(f"Hasil Enkoding : {encoded}")
# print(f"Hasil Dekoding : {decoded}")
