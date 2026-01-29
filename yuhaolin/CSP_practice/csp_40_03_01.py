import sys

def main():
    line1 = sys.stdin.readline().split()
    z = int(line1[0])
    # 读取加密后图片
    matrix = []
    for _ in range(z):
        matrix.append(list(sys.stdin.readline().strip()))
    # 读取密钥序列
    k_len = int(sys.stdin.readline().strip())
    k = list(map(int, sys.stdin.read().split()))
    
    t = k[0]
    ops = []
    idx = 1
    for _ in range(t):
        op_type = k[idx]
        params = k[idx+1:idx+6]
        ops.append((op_type, params))
        idx += 6
    
    def rotate_matrix(mat, times):
        """旋转矩阵，times是顺时针旋转90度的次数""" 
        n = len(mat)
        for _ in range(times % 4):
            mat = [list(row) for row in zip(*mat[::-1])]
        return mat
    
    def rotate_sub(mat, u, v, L, angle, clockwise=True):
        # 提取子矩阵
        r_start, c_start = u-1, v-1
        sub = []
        for r in range(r_start, r_start + L):
            sub.append(mat[r][c_start:c_start+L])
        times = (angle // 90) % 4
        if not clockwise:
            times = (4 - times) % 4
        
        sub = rotate_matrix(sub, times)
        
        # 放回矩阵
        for i in range(L):
            for j in range(L):
                mat[r_start+i][c_start+j] = sub[i][j]
    
    for i in range(t-1, -1, -1):
        op_type, p = ops[i]
        
        if op_type == 1:
            # 加密：子矩阵顺时针旋转 d，整体逆时针旋转 r 次
            # 逆向：整体顺时针旋转 r 次，子矩阵逆时针旋转 d
            ui, vi, Li, di, ri = p
            matrix = rotate_matrix(matrix, ri)
            rotate_sub(matrix, ui, vi, Li, di, clockwise=False)
        elif op_type == 2:
            # 加密：子矩阵翻转
            # 逆向：相同翻转即可
            ui, di, li, ri, oi = p
            r_start, r_end = ui-1, di-1
            c_start, c_end = li-1, ri-1
            
            sub = []
            for r in range(r_start, r_end+1):
                sub.append(matrix[r][c_start:c_end+1])
            if oi == 1:
                # 上下翻转
                sub = sub[::-1]
            else:
                # 左右翻转
                sub = [row[::-1] for row in sub]
            
            for r in range(len(sub)):
                for c in range(len(sub[0])):
                    matrix[r_start+r][c_start+c] = sub[r][c]
    
    # 删除右侧和下方的 ?
    max_r = 0
    max_c = 0
    for r in range(z):
        for c in range(z):
            if matrix[r][c] != '?':
                max_r = max(max_r, r+1)
                max_c = max(max_c, c+1)
    
    print(f"{max_r} {max_c}")
    for r in range(max_r):
        print("".join(matrix[r][:max_c]))
        
if __name__ == "__main__":
    main()        