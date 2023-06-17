import heapq


# Клас для представлення вузла дерева Хаффмана
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Оператор для порівняння вузлів
    def __lt__(self, other):
        return self.freq < other.freq

# Функція для побудови таблиці частот символів
def build_frequency_table(text):
    freq_table = {}
    for char in text:
        if char in freq_table:
            freq_table[char] += 1
        else:
            freq_table[char] = 1
    return freq_table

# Функція для побудови дерева Хаффмана
def build_huffman_tree(freq_table):
    heap = []
    for char, freq in freq_table.items():
        node = HuffmanNode(char, freq)
        heapq.heappush(heap, node)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heapq.heappop(heap)

# Функція для побудови кодового словника символів
def build_code_table(huffman_tree):
    code_table = {}

    def assign_codes(node, code):
        if node.char:
            code_table[node.char] = code
        else:
            assign_codes(node.left, code + '0')
            assign_codes(node.right, code + '1')

    assign_codes(huffman_tree, '')
    return code_table

# Функція для кодування тексту з використанням кодового словника
def encode_text(text, code_table):
    encoded_text = ''
    for char in text:
        encoded_text += code_table[char]
    return encoded_text


# Функція для декодування тексту з використанням дерева Хаффмана
def decode_text(encoded_text, huffman_tree):
    decoded_text = ''
    current_node = huffman_tree

    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char:
            decoded_text += current_node.char
            current_node = huffman_tree

    return decoded_text


# Функція для стиснення файлу з використанням алгоритму Хаффмана
def compress_file(input_file, output_file):
    # Зчитування вхідного файлу
    with open(input_file, 'r') as file:
        text = file.read()

    # Побудова таблиці частот символів
    freq_table = build_frequency_table(text)

    # Побудова дерева Хаффмана
    huffman_tree = build_huffman_tree(freq_table)

    # Побудова кодового словника
    code_table = build_code_table(huffman_tree)

    # Кодування тексту
    encoded_text = encode_text(text, code_table)

    # Запис стиснених даних у вихідний файл
    with open(output_file, 'wb') as file:
        # Запис таблиці частот
        file.write(bytes(str(freq_table), 'utf-8'))
        file.write(b'\n')

        # Запис закодованого тексту
        file.write(bytes(encoded_text, 'utf-8'))


# Функція для розпакування файлу з використанням алгоритму Хаффмана
def decompress_file(input_file, output_file):
    # Читання стисненого файлу
    with open(input_file, 'rb') as file:
        # Читання таблиці частот
        freq_table_str = file.readline().decode('utf-8')
        freq_table = eval(freq_table_str)

        # Читання закодованого тексту
        encoded_text = file.read().decode('utf-8')

    # Побудова дерева Хаффмана
    huffman_tree = build_huffman_tree(freq_table)

    # Декодування тексту
    decoded_text = decode_text(encoded_text, huffman_tree)

    # Запис розпакованого тексту у вихідний файл
    with open(output_file, 'w') as file:
        file.write(decoded_text)




# Стиснення файлу
input_file = 'Garri-Pottier_task_3.txt'
compressed_file = 'Garri-Pottier_task_3_compressed.bin'
compress_file(input_file, compressed_file)

# Розпакування файлу
output_file = 'Garri-Pottier_task_3_output.txt'
decompress_file(compressed_file, output_file)
