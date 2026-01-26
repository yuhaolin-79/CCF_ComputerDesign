n, m, q = map(int, input().split())

# 存储角色信息
roles = {}

# 读取n个角色定义
for _ in range(n):
    parts = input().split()
    role_name = parts[0]  # 修正：变量名不能有连字符，改为role_name
    nv = int(parts[1])
    operations = parts[2:2+nv]
    no = int(parts[2+nv])
    resource_kinds = parts[2+nv+1:2+nv+1+no]
    nn = int(parts[2+nv+1+no])
    resource_names = parts[2+nv+1+no+1:2+nv+1+no+1+nn]
    
    roles[role_name] = {
        'operations': set(operations),
        'resource_kinds': set(resource_kinds),
        'resource_names': set(resource_names)
    }

# 修正1：role_associations初始化位置（必须在角色循环之后）
role_associations = {}

# 读取m个角色关联
for _ in range(m):
    parts = input().split()
    role_name = parts[0]
    ns = int(parts[1])
    objects = parts[2:2+2*ns]  # 修正：2*ns个元素
    
    if role_name not in role_associations:
        role_associations[role_name] = set()
    
    for i in range(ns):
        obj_type = objects[2*i]
        obj_name = objects[2*i+1]
        role_associations[role_name].add(f"{obj_type}:{obj_name}")

# 修正2：output_lines初始化位置（必须在查询循环之前）
output_lines = []

# 读取q个查询
for _ in range(q):
    parts = input().split()
    user_name = parts[0]
    ng = int(parts[1])
    groups = parts[2:2+ng]
    action = parts[2+ng]
    resource_kind = parts[3+ng]
    resource_name = parts[4+ng]
    
    # 修正3：关联角色查找位置（必须在查询循环内部）
    associated_roles = []
    for role, obj_set in role_associations.items():
        # 检查用户名
        if f"u:{user_name}" in obj_set:
            associated_roles.append(role)
            continue
        # 检查用户组
        for group in groups:
            if f"g:{group}" in obj_set:
                associated_roles.append(role)
                break
    
    # 检查权限
    allowed = False
    for role in associated_roles:
        r = roles[role]
        # 操作检查
        if action not in r['operations'] and '*' not in r['operations']:
            continue
        # 资源类型检查
        if resource_kind not in r['resource_kinds'] and '*' not in r['resource_kinds']:
            continue
        # 资源名称检查
        if r['resource_names'] and resource_name not in r['resource_names']:
            continue
        allowed = True
        break
    
    output_lines.append('1' if allowed else '0')

# 输出结果
for line in output_lines:
    print(line)
    