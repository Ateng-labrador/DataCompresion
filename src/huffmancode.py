import heapq

def huffman_code_array1(text):
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


    # Tahap 3
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
    symbols_lengths.sort(key = get_key)
    
    codes = {}
    current_code = 0
    previous_length = 0
    
    for sym, length in symbols_lengths:
        if length > previous_length:
            current_code <<= (length - previous_length)
            previous_length = length
    
        codes[sym] = format(current_code, f'0{length}b')
        current_code += 1
    return codes

