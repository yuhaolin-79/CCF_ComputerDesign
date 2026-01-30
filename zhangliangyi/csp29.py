def find_matching_bracket(s, start):
    count = 1
    for i in range(start + 1, len(s)):
        if s[i] == '(':
            count += 1
        elif s[i] == ')':
            count -= 1
            if count == 0:
                return i
    return -1

def parse_expr(s):
    if s[0] in '&|':
        op = s[0]
        idx1 = s.find('(')
        idx2 = find_matching_bracket(s, idx1)
        sub1 = s[idx1+1:idx2]
        idx3 = s.find('(', idx2+1)
        idx4 = find_matching_bracket(s, idx3)
        sub2 = s[idx3+1:idx4]
        f1 = parse_expr(sub1)
        f2 = parse_expr(sub2)
        if op == '&':
            return lambda attr: f1(attr) and f2(attr)
        else:
            return lambda attr: f1(attr) or f2(attr)
    else:
        op_pos = -1
        for i, c in enumerate(s):
            if c in ':~':
                op_pos = i
                break
        attr_num = int(s[:op_pos])
        op = s[op_pos]
        val = int(s[op_pos+1:])
        def check(attr):
            if attr_num not in attr:
                return False
            return attr[attr_num] == val if op == ':' else attr[attr_num] != val
        return check

n = int(input())
users = {}
dn_list = []
for _ in range(n):
    parts = list(map(int, input().split()))
    dn = parts[0]
    dn_list.append(dn)
    k = parts[1]
    attr = {}
    idx = 2
    for __ in range(k):
        a = parts[idx]
        v = parts[idx+1]
        attr[a] = v
        idx += 2
    users[dn] = attr

m = int(input())
for _ in range(m):
    expr = input().strip()
    checker = parse_expr(expr)
    matched = []
    for dn in dn_list:
        if checker(users[dn]):
            matched.append(dn)
    matched.sort()
    print(' '.join(map(str, matched)))