import sys

def main():
    MOD = 10**9 + 7
    data = sys.stdin.read().split()
    ptr = 0
    n = int(data[ptr])
    ptr += 1
    m = int(data[ptr])
    ptr += 1
    
    total_elements = len(data)
    query_start = total_elements - m * (n + 1)
    tokens = data[ptr:query_start]
    ptr = query_start
    
    for _ in range(m):
        target_idx = int(data[ptr]) # 要求的偏导变量编号
        ptr += 1
        a_values = []
        for i in range(n):
            a_values.append(int(data[ptr]))
            ptr += 1
            
        stack = [] # 栈中存储（value, derivative）
        
        for token in tokens:
            if token == '+':
                v2, dv2 = stack.pop()
                v1, dv1 = stack.pop()
                stack.append(((v1 + v2) % MOD, (dv1 + dv2) % MOD))
            elif token == '-':
                v2, dv2 = stack.pop()
                v1, dv1 = stack.pop()
                stack.append(((v1 - v2) % MOD, (dv1 - dv2) % MOD))  
            elif token == '*':
                v2, dv2 = stack.pop()
                v1, dv1 = stack.pop()
                # 乘法导数公式: (uv)' = u'v + uv'
                new_v = (v1 * v2) % MOD
                new_dv = (dv1 * v2 + v1 * dv2) % MOD
                stack.append((new_v, new_dv))
            elif token.startswith('x'):
                idx = int(token[1:])
                val = a_values[idx-1] % MOD
                d_val = 1 if idx == target_idx else 0
                stack.append((val, d_val))
            else:
                val = int(token) % MOD
                stack.append((val, 0))
        
        # 栈顶元素的第二个值即为偏导数
        print(stack[0][1] % MOD) 

if __name__ == "__main__":
    main()            
        
    