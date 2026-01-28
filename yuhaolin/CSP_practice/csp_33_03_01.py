import sys
from fractions import Fraction

def parse_formula(formula):
    """解析化学方程式，返回{元素名：原子个数}"""
    res = {}
    i = 0
    while i < len(formula):
        # 提取元素名
        start_element = i
        while i < len(formula) and formula[i].islower():
            i += 1
        element = formula[start_element:i]
        # 提取原子数
        start_num = i
        while i < len(formula) and formula[i].isdigit():
            i += 1
        num = int(formula[start_num:i])
        
        res[element] = num
    return res

def get_rank(martrix):
    """计算矩阵的秩"""
    if not martrix or not martrix[0]:
        return 0
    
    rows = len(martrix)
    cols = len(martrix[0])
    rank = 0
    curr_row = 0
    
    for j in range(cols):
        # 寻找主元
        pivot = curr_row
        while pivot < rows and martrix[pivot][j] == 0:
            pivot += 1
        
        if pivot == rows:
            continue
        # 交换行
        martrix[curr_row], martrix[pivot] = martrix[pivot], martrix[curr_row]
        
        # 消元
        for i in range(rows):
            if i != curr_row and martrix[i][j] != 0:
                factor = martrix[i][j] / martrix[curr_row][j]
                for k in range(j, cols):
                    martrix[i][k] -= factor * martrix[curr_row][k]
        
        rank += 1
        curr_row += 1
        if curr_row == rows:
            break
    
    return rank

def main():
    line = sys.stdin.readline()
    n = int(line.strip())
    
    for _ in range(n):
        parts = sys.stdin.readline().split()
        m = int(parts[0])
        formulas = parts[1:]
        
        parsed_list = [parse_formula(f) for f in formulas]
        elements = sorted(list(set(el for p in parsed_list for el in p)))
        
        martrix = []
        for el in elements:
            row = [Fraction(p.get(el, 0)) for p in parsed_list]
            martrix.append(row)
        
        rank = get_rank(martrix)
        
        if rank < m:
            print("Y")
        else:
            print("N")

if __name__ == "__main__":
    main()