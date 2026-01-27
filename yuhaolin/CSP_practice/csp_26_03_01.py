import sys

def main():
    line1 = sys.stdin.readline().split()
    n, m, q = map(int, line1)
    
    # 存储角色
    roles = {}
    for _ in range(n):
        parts = sys.stdin.readline().split()
        name = parts[0]
        # 操作
        nv = int(parts[1])
        ops = set(parts[2:2+nv])
        # 资源种类
        idx = 2 + nv
        no = int(parts[idx])
        types = set(parts[idx+1:idx+1+no])
        # 资源名称
        idx = idx + 1 + no
        nn = int(parts[idx])
        names = set(parts[idx+1:idx+1+nn])
        
        roles[name] = (ops, types, names)
    
    # 存储角色关联
    user_to_roles = {}
    group_to_roles = {}
    for _ in range(m):
        parts = sys.stdin.readline().split()
        role_name = parts[0]
        ns = int(parts[1])
        for i in range(ns):
            category = parts[2 + 2*i]
            subject = parts[3 + 3*i]
            if category == 'u':
                user_to_roles.setdefault(subject, set()).add(role_name)
            else:
                group_to_roles.setdefault(subject, set()).add(role_name)
    
    # 处理查询
    results = []
    for _ in range(q):
        parts = sys.stdin.readline().split()
        user_name = parts[0]
        ng = int(parts[1])
        groups = parts[2:2+ng]
        
        op = parts[2+ng]
        res_type = parts[3+ng]
        res_name = parts[4+ng]
        
        relevant_roles = set()
        if user_name in user_to_roles:
            relevant_roles.update(user_to_roles[user_name])
        for g in groups:
            if g in group_to_roles:
                relevant_roles.update(group_to_roles[g])
        
        allowed = "0"
        for r_name in relevant_roles:
            r_ops, r_types, r_names = roles[r_name]
            if ('*' in r_ops or op in r_ops) and \
               ('*' in r_types or res_type in r_types) and \
               (not r_names or res_name in r_names):
                allowed = "1"
                break
        results.append(allowed)
        
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    main()