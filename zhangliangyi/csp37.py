MOD = 10**9 + 7
var_info = {}
def calc_expr(operands):

    result_parts = []
    for op in operands:
        if op.startswith('$'):
        
            sub_var_name = op[1:]
            sub_var_value = get_var_value(sub_var_name)
            result_parts.append(sub_var_value)
        else:
            result_parts.append(op)
    return ''.join(result_parts)

def get_var_value(var_name):

    if var_name not in var_info:
        return ""
    
    var_data = var_info[var_name]
    var_type = var_data['type']
    content = var_data['content']
    
    if var_type == 1:
        return content
    elif var_type == 2:
    
        return calc_expr(content)

def main():
    import sys
    input_lines = sys.stdin.read().splitlines()
    n = int(input_lines[0])
    
    for line in input_lines[1:n+1]:
        parts = line.split()
        if not parts:
            continue
        
        stmt_type = parts[0]
        if stmt_type == '1':
        
            var_name = parts[1]
            expr_operands = parts[2:]
        
            final_value = calc_expr(expr_operands)
        
            var_info[var_name] = {
                'type': 1,
                'content': final_value
            }
        elif stmt_type == '2':
        
            var_name = parts[1]
            expr_operands = parts[2:]
        
            var_info[var_name] = {
                'type': 2,
                'content': expr_operands
            }
        elif stmt_type == '3':
        
            var_name = parts[1]
            var_value = get_var_value(var_name)
            length_mod = len(var_value) % MOD
            print(length_mod)

if __name__ == "__main__":
    main()