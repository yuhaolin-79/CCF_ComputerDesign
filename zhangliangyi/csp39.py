def build_huffman_decoder(tree_str):
    decoder = {}
    index = 0
    def dfs(current_path):
        nonlocal index
        if index >= len(tree_str):
            return
        flag = tree_str[index]
        index += 1
        if flag == '1':
            char = tree_str[index]
            index += 1
            decoder[current_path] = char
            return
        else:
            dfs(current_path + '0')
            dfs(current_path + '1')
    dfs('')
    return decoder

def huffman_decode(binary_str, decoder):
    result = []
    current = ''
    for bit in binary_str:
        current += bit
        if current in decoder:
            result.append(decoder[current])
            current = ''
    return ''.join(result)

def decode_string(s, huffman_decoder):
    if s.startswith('H') and len(s) > 1 and all(c in '0123456789abcdefABCDEF' for c in s[1:]):
        hex_str = s[1:]
        p = int(hex_str[-2:], 16)
        data_hex = hex_str[:-2]
        binary_str = ''
        for c in data_hex:
            binary_str += bin(int(c, 16))[2:].zfill(4)
        if p > 0:
            binary_str = binary_str[:-p]
        return huffman_decode(binary_str, huffman_decoder)
    else:
        if s.startswith('HH'):
            return s[1:]
        else:
            return s

def get_entry_by_id(table_id, static_table, dynamic_table, S):
    if table_id <= S:
        return static_table[table_id]
    else:
        dyn_index = table_id - S - 1
        return dynamic_table[dyn_index]

def main():
    import sys
    input_lines = [line.strip() for line in sys.stdin if line.strip()]
    ptr = 0
    S, D = map(int, input_lines[ptr].split())
    ptr += 1
    static_table = [None]
    for _ in range(S):
        key, value = input_lines[ptr].split()
        static_table.append((key, value))
        ptr += 1
    tree_str = input_lines[ptr]
    ptr += 1
    huffman_decoder = build_huffman_decoder(tree_str)
    N = int(input_lines[ptr])
    ptr += 1
    dynamic_table = []
    for _ in range(N):
        parts = input_lines[ptr].split()
        ptr += 1
        type_cmd = int(parts[0])
        if type_cmd == 1:
            table_id = int(parts[1])
            key, value = get_entry_by_id(table_id, static_table, dynamic_table, S)
            print(f"{key}: {value}")
        elif type_cmd in (2, 3):
            i = int(parts[1])
            if i == 0:
                key_str = parts[2]
                value_str = parts[3]
                key = decode_string(key_str, huffman_decoder)
            else:
                key, _ = get_entry_by_id(i, static_table, dynamic_table, S)
                value_str = parts[2]
            value = decode_string(value_str, huffman_decoder)
            print(f"{key}: {value}")
            if type_cmd == 2:
                dynamic_table.insert(0, (key, value))
                if len(dynamic_table) > D:
                    dynamic_table.pop()

if __name__ == "__main__":
    main()