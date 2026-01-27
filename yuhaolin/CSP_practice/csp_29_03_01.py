import sys

def main():
    def get_input_list():
        line = sys.stdin.readline()
        return line.split() if line else []

    # 读取用户数量 n
    res = get_input_list()
    if not res: return
    n = int(res[0])
    
    # attr_val_to_dns[attr][val] = {dn1, dn2, ...}
    attr_val_to_dns = {}
    # attr_to_dns[attr] = {dn1, dn2, ...}
    attr_to_dns = {}
    
    for _ in range(n):
        # 逐行读取每个用户的信息
        user_info = get_input_list()
        if not user_info: break
        
        dn = int(user_info[0])
        num_attrs = int(user_info[1])
        
        for i in range(num_attrs):
            a = int(user_info[2 + i*2])
            v = int(user_info[3 + i*2])
            
            # 构建倒排索引
            if a not in attr_val_to_dns:
                attr_val_to_dns[a] = {}
                attr_to_dns[a] = set()
            if v not in attr_val_to_dns[a]:
                attr_val_to_dns[a][v] = set()
            
            attr_val_to_dns[a][v].add(dn)
            attr_to_dns[a].add(dn)

    # 读取表达式数量 m
    res = get_input_list()
    if not res: return
    m = int(res[0])

    def parse_and_evaluate(s, start):
        """解析表达式并返回匹配的 DN 集合以及结束位置"""
        if s[start] in ('&', '|'):
            op = s[start]
            # 跳过 op 和 '(' -> 索引 +2
            curr = start + 2 
            set1, next_pos = parse_and_evaluate(s, curr)
            # 跳过中间的 ')' 和 '(' -> 索引 +2
            curr = next_pos + 2
            set2, next_pos = parse_and_evaluate(s, curr)
            # 结果以最后一个 ')' 结束
            res_set = (set1 & set2) if op == '&' else (set1 | set2)
            return res_set, next_pos + 1
        else:
            # 原子表达式解析 (Base Expr)
            op_idx = -1
            op_type = ''
            # 查找操作符 : 或 ~
            for i in range(start, len(s)):
                if s[i] == ':':
                    op_idx = i
                    op_type = ':'
                    break
                elif s[i] == '~':
                    op_idx = i
                    op_type = '~'
                    break
            
            attr = int(s[start:op_idx])
            
            # 提取 Value 值，遇到 ) 停止
            end_idx = op_idx + 1
            while end_idx < len(s) and s[end_idx].isdigit():
                end_idx += 1
            val = int(s[op_idx+1 : end_idx])
            
            res = set()
            if attr in attr_to_dns:
                if op_type == ':':
                    # 断言：具有该属性且值相等
                    res = attr_val_to_dns[attr].get(val, set())
                else:
                    # 反断言：具有该属性且值不等
                    # 结果 = (拥有该属性的人) - (拥有该属性且值相等的人)
                    res = attr_to_dns[attr] - attr_val_to_dns[attr].get(val, set())
            
            return res, end_idx

    # 循环读取并处理 m 个表达式
    for _ in range(m):
        expr_str = sys.stdin.readline().strip()
        if not expr_str: break
        
        matched_dns, _ = parse_and_evaluate(expr_str, 0)

        res_list = sorted(list(matched_dns))
        print(" ".join(map(str, res_list)))

if __name__ == "__main__":
    main()