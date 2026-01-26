import sys
MOD = 10**9 + 7

def main():
    line = sys.stdin.readline()
    n = int(line.strip())
    
    # 存储变量当前长度
    values = {}
    # 存储简介变量的表达式
    formulas = {}
    is_indirect = {}
    
    def get_len(var_name):
        # 初始全部为0
        if var_name not in is_indirect:
            return 0
        # 直接赋值
        if not is_indirect[var_name]:
            return values.get(var_name, 0)
        
        # 间接赋值
        total_len = 0
        for op in formulas[var_name]:
            if op.startswith('$'):
                dep_var = op[1:] # 去掉'$',递归求长
                total_len = (total_len + get_len(dep_var)) % MOD
            else:
                total_len = (total_len + len(op)) % MOD
        return total_len
    
    for i in range(1, n + 1):
        parts = sys.stdin.readline().split()
        op_type = parts[0]
        
        if op_type == '1':
            target_var = parts[1]
            expr_parts = parts[2:]
            
            curr_len = 0
            for op in expr_parts:
                if op.startswith('$'):
                    curr_len = (curr_len + get_len(op[1:])) % MOD
                else:
                    curr_len = (curr_len + len(op)) % MOD
            
            values[target_var] = curr_len
            is_indirect[target_var] = False
        
        elif op_type == '2':
            target_var = parts[1]
            expr_parts = parts[2:]  
            
            formulas[target_var] = expr_parts
            is_indirect[target_var] = True
            
        elif op_type == '3':
            target_var = parts[1]
            print(get_len(target_var))
            
if __name__ == "__main__":
    main()         
                
        