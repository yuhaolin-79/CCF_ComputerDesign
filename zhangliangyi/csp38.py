import math

MULTIPLIER = 47055833459  
POW_2_25 = 2 ** 25        
POW_2_12 = 2 ** 12        
POW_2_64 = 2 ** 64        

CHAR_MAP_NORMAL = {
    ' ': 0,
    **{str(d): d+1 for d in range(10)},  # 0-9 → 1-10
    **{chr(ord('A')+i): 11+i for i in range(26)},  # A-Z → 11-36
    '_': 37
}
REVERSE_CHAR_MAP_NORMAL = {v: k for k, v in CHAR_MAP_NORMAL.items()}


TYPICAL_POS_RULES = [
  
    {0: ' ', **{i+1: str(i) for i in range(10)}, **{11+i: chr(ord('A')+i) for i in range(26)}},
    {**{i: str(i) for i in range(10)}, **{10+i: chr(ord('A')+i) for i in range(26)}},

    {i: str(i) for i in range(10)},
    
    {i: chr(ord('A')+i) for i in range(26)},
    
    {i: chr(ord('A')+i) for i in range(26)},
    
    {i: chr(ord('A')+i) for i in range(26)}
]

POW_26_0 = 26 ** 0
POW_26_1 = 26 ** 1
POW_26_2 = 26 ** 2
POW_26_3 = 26 ** 3
WEIGHT_TYPICAL_0 = 36 * 10 * POW_26_3
WEIGHT_TYPICAL_1 = 10 * POW_26_3
WEIGHT_TYPICAL_2 = POW_26_3
WEIGHT_TYPICAL = [WEIGHT_TYPICAL_0, WEIGHT_TYPICAL_1, WEIGHT_TYPICAL_2, POW_26_2, POW_26_1, POW_26_0]

WEIGHT_NORMAL = [38 ** i for i in range(11)][::-1]  

def calculate_hash(code_number, hash_bits):
   
    if hash_bits not in [12, 25]:
        raise ValueError("散列值仅支持12位或25位")
    
    step1 = code_number * MULTIPLIER
    
    divisor = 2 ** (64 - hash_bits)
    step2 = step1 // divisor
    
    mod_value = 2 ** hash_bits
    step3 = step2 % mod_value
    
    return step3

def code_to_normal_number(code):
   
    padded_code = code.ljust(11, ' ')
    
    total = 0
    for i, char in enumerate(padded_code):
        char_value = CHAR_MAP_NORMAL.get(char, 0)
        total += char_value * WEIGHT_NORMAL[i]
    
    return total

def normal_number_to_code(number):
   
    padded_chars = []
    remaining = number
    
    for weight in WEIGHT_NORMAL:
    
        char_value = remaining // weight
        padded_chars.append(REVERSE_CHAR_MAP_NORMAL.get(char_value, ' '))
    
        remaining = remaining % weight
    
    code = ''.join(padded_chars).rstrip(' ')
    return code

def typical_code_to_short_number(code):
   
    padded_code = code.rjust(6, ' ')
    
    char_values = []
    for i, char in enumerate(padded_code):
        if i == 0:
        
            if char == ' ':
                char_values.append(0)
            elif char.isdigit():
                char_values.append(int(char) + 1)
            elif char.isupper():
                char_values.append(ord(char) - ord('A') + 11)
            else:
                char_values.append(0)
        elif i == 1:
        
            if char.isdigit():
                char_values.append(int(char))
            elif char.isupper():
                char_values.append(ord(char) - ord('A') + 10)
            else:
                char_values.append(0)
        elif i == 2:
        
            char_values.append(int(char) if char.isdigit() else 0)
        else:
        
            char_values.append(ord(char) - ord('A') if char.isupper() else 0)
    
    total = sum(v * w for v, w in zip(char_values, WEIGHT_TYPICAL))
    return total

def short_number_to_typical_code(short_number):
    
    remaining = short_number
    typical_chars = []
    
    for i, weight in enumerate(WEIGHT_TYPICAL):
        
        val = remaining // weight
    
        char = TYPICAL_POS_RULES[i].get(val, ' ')
        typical_chars.append(char)
    
        remaining = remaining % weight
    
    code = ''.join(typical_chars).lstrip(' ')
    return code

class CodeLibrary:
    def __init__(self):
    
        self.code_records = []
    
    def add_code(self, code):
        
        if not code:
            return
       
        normal_num = code_to_normal_number(code)
        
        hash_12 = calculate_hash(normal_num, 12)
        hash_25 = calculate_hash(normal_num, 25)
        
        self.code_records.append((code, hash_12, hash_25))
    
    def infer_code_by_hash_12(self, target_hash_12):
        
        return self._infer_code(target_hash_12, hash_type=12)
    
    def infer_code_by_hash_25(self, target_hash_25):
       
        return self._infer_code(target_hash_25, hash_type=25)
    
    def _infer_code(self, target_hash, hash_type):
       
        if hash_type not in [12, 25]:
            return "###"
        
        hash_idx = 1 if hash_type == 12 else 2
        
        for record in reversed(self.code_records):
            code, hash12, hash25 = record
            if record[hash_idx] == target_hash:
                return f"#{code}"
        
        return "###"

def parse_simple_message(bin_str, code_lib):
    
    recv_bin = bin_str[1:29]   
    send_bin = bin_str[29:57]   
    pos_bin = bin_str[57:72]    
    
    recv_val = int(recv_bin, 2)
    send_val = int(send_bin, 2)
    pos_val = int(pos_bin, 2)
    
    if recv_val >= POW_2_25:
        short_num = recv_val - POW_2_25
        recv_code = short_number_to_typical_code(short_num)
        code_lib.add_code(recv_code)
    else:
       
        recv_code = code_lib.infer_code_by_hash_25(recv_val)
    
    if send_val >= POW_2_25:
        short_num = send_val - POW_2_25
        send_code = short_number_to_typical_code(short_num)
        code_lib.add_code(send_code)
    else:
        send_code = code_lib.infer_code_by_hash_25(send_val)
    
    result_parts = [recv_code, send_code]
    if pos_val != 0:
        result_parts.append(str(pos_val))
    
    return ' '.join(result_parts)

def parse_complex_message(bin_str, code_lib):
    
    codeA_bin = bin_str[1:59]   
    hashB_bin = bin_str[59:71] 
    rel_bin = bin_str[71]       
    codeA_num = int(codeA_bin, 2)
    hashB_12 = int(hashB_bin, 2)
    rel_val = int(rel_bin)
    
    codeA = normal_number_to_code(codeA_num)
    code_lib.add_code(codeA)
    
    codeB = code_lib.infer_code_by_hash_12(hashB_12)
    
    if rel_val == 0:
       
        return f"{codeB} {codeA}"
    else:
        return f"{codeA} {codeB}"

def parse_message(bin_str, code_lib):
   
    if len(bin_str) != 72:
        return "### ###"
    
    first_bit = bin_str[0]
    if first_bit == '0':
        return parse_simple_message(bin_str, code_lib)
    else:
        return parse_complex_message(bin_str, code_lib)

def main():
    import sys
    input_lines = [line.strip() for line in sys.stdin if line.strip()]
    if not input_lines:
        return
    
    n = int(input_lines[0])
    messages = input_lines[1:n+1]
    
    code_lib = CodeLibrary()
    
    for msg_bin in messages:
        result = parse_message(msg_bin, code_lib)
        print(result)

if __name__ == "__main__":
    main()