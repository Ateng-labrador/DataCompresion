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


def huffman_code_array(text):
    if not text:
        return {}

    # For Count Probabily fo codeword
    freq = {}
    for i in text:
        freq[i] = freq.get(i, 0) + 1

    # Mengembalikan angka satu jika panjang frequensi cuman satu
    if len(freq) == 1:
        return {list(freq.keys())[0]:"0"}

    # melakaukan iterasi huruf frequnnsi
    def get_freq(c):
        return freq[c]

    # mengurutkan symbols
    symbols = sorted(freq.keys(), key=get_freq)
    n = len(symbols)

    # ambil jumlah frequnsinya
    A = [freq[s] for s in symbols]

    leaf_ptr = 0
    rigt_ptr = 0

    # Node 1
    for i in range(n, 2 * n - 1):
        if leaf_ptr < n and (rigt_ptr >= i - n or A[leaf_ptr] < A[n + rigt_ptr]):
            w1 = A[leaf_ptr]
            A[leaf_ptr] = i
            leaf_ptr += 1
        else:
            w1 = A[n + rigt_ptr]
            A[n + rigt_ptr] = i
            leaf_ptr += 1

    # Node 2
        if leaf_ptr < n and (rigt_ptr >= i - n  or A[leaf_ptr] < A[n + rigt_ptr]):
            w2 = A[leaf_ptr]
            A[leaf_ptr] = i
            leaf_ptr += 1
        else:
            w2 = A[n + rigt_ptr]
            A[n + rigt_ptr] = i
            rigt_ptr += 1
        A[i] = w1 + w2
    A[2 * n - 2] = 0

    lengths = []
    for i in range(n):
        dept = 0
        curr = i
        while curr != 2 * n - 2:
            curr = A[curr]
            dept += 1
        lengths.append(dept)

    def get_key(x):
        return x[1], x[0]

    symbols_lengths = list(zip(symbols, lengths))
    symbols_lengths.sort(get_key)

    codes = {}
    current_code = 0
    previous_length = 0

    for sym, lengths in symbols_lengths:
        if lengths > previous_length:
            current_code <<= (lengths - previous_length)
            previous_length = lengths

        codes[sym] = format(current_code, f'0{lengths}b')
        current_code += 1
    return codes

def huffman_code_array1(text):
    """
    1. Tahap pertama
        - menghitung jumlah frekuensi pada setiap kata yang tersimpan
        - melakukan pengurutan berdasarkan jumlah frekuensi (frekuesnsi kecil ke besar)
        - 
    
    2. Tahap Kedua
        
    
    
    """

    # Tahap 1
    freq = {}
    for item in text:
        freq[item] = freq.get(item, 0) + 1

    def get_freq(c):
        return freq[c]

    # isinya urutan huruf
    symbols = sorted(freq.keys(), key=get_freq)
    n = len(symbols)
    # mengambil jumlah frequnsi pada dictionary
    A = [freq[s] for s in symbols] + [0] * n


    # Tahap 2
    leaf_ptr = 0
    root_ptr = 0
    for i in range(n, 2 * n - 1):
        # 1. Ambil Node Terkecil Pertama
        if leaf_ptr < n and (root_ptr >= i - n or A[leaf_ptr] < A[n + root_ptr]):
            w1 = A[leaf_ptr]
            A[leaf_ptr] = i
            leaf_ptr += 1
        else:
            w1 = A[n + root_ptr]
            A[n + root_ptr] = i
            root_ptr += 1

        # 2. Ambil Node Terkecil Kedua
        if leaf_ptr < n and (root_ptr >= i - n or A[leaf_ptr] < A[n + root_ptr]):
            w2 = A[leaf_ptr]
            A[leaf_ptr] = i
            leaf_ptr += 1
        else:
            w2 = A[n + root_ptr]
            A[n + root_ptr] = i
            root_ptr += 1
        A[i] = w1 + w2
    A[2 * n - 2] = 0
    return A
        
# next menggunakna Min-Heap (Priority Queue) berbasis Array
x = "khansa"
print(huffman_code_array1(x))





