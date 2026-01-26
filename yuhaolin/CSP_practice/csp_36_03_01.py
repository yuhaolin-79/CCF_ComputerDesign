import sys

def main():
    line1 = sys.stdin.readline().split()
    n, N, q = map(int, line1)
    
    groups = [[] for _ in range(N)]
    write_sets = [set() for _ in range(N)]
    
    for _ in range(q):
        line = sys.stdin.readline().split()
        o, a = map(int, line)
        
        g_idx = (a // n) % N
        group = groups[g_idx]
        write_set = write_sets[g_idx]
        
        hit_idx = -1
        for i in range(len(group)):
            if group[i] == a:
                hit_idx = i
                break
        if hit_idx != -1:
            group.pop(hit_idx)
            group.append(a)
            if o == 1:
                write_set.add(a)
        else:
            if len(group) == n:
                old_a = group.pop(0)
                if old_a in write_set:
                    print(1, old_a)
                    write_set.remove(old_a)
            
            print(0, a)
            
            group.append(a)
            if o == 1:
                write_set.add(a)
            else:
                write_set.discard(a)

    
if __name__ == "__main__":
    main()
                    
                