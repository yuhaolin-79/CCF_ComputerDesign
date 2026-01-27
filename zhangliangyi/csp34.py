import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n, m = map(int, data[0].split())
    words = []
    all_chars = set()
    
    for i in range(1, n + 1):
        s, f_str = data[i].split()
        f = int(f_str)
        words.append((s, f))
        for ch in s:
            all_chars.add(ch)
    
    # 初始词汇表：所有出现字符按字典序
    initial_vocab = sorted(all_chars)
    result_vocab = initial_vocab.copy()
    
    # 若m不超过初始词汇表大小（题目保证m≥len(initial_vocab)，但安全处理）
    if len(result_vocab) >= m:
        for i in range(m):
            print(result_vocab[i])
        return
    
    # 初始化每个单词的字符序列和频率
    sequences = [list(word) for word, _ in words]
    freqs = [f for _, f in words]
    
    need = m - len(initial_vocab)
    for _ in range(need):
        # 统计所有相邻词汇对的总频率
        pair_freq = {}
        for idx, seq in enumerate(sequences):
            if len(seq) < 2:
                continue
            f = freqs[idx]
            for i in range(len(seq) - 1):
                pair = (seq[i], seq[i + 1])
                pair_freq[pair] = pair_freq.get(pair, 0) + f
        
        # 无可用词汇对则终止（题目保证不会发生，但健壮性处理）
        if not pair_freq:
            break
        
        # 按规则选择最优词汇对：
        # 1. 频率降序 → 2. 拼接长度升序 → 3. prev长度升序 → 4. 拼接字符串字典序升序
        best_pair = min(
            pair_freq.items(),
            key=lambda x: (
                -x[1], 
                len(x[0][0]) + len(x[0][1]), 
                len(x[0][0]), 
                x[0][0] + x[0][1]
            )
        )[0]
        
        new_word = best_pair[0] + best_pair[1]
        result_vocab.append(new_word)
        
        # 更新所有序列：贪心替换所有不重叠的(best_pair[0], best_pair[1])
        new_sequences = []
        for seq in sequences:
            new_seq = []
            i = 0
            while i < len(seq):
                if i + 1 < len(seq) and seq[i] == best_pair[0] and seq[i + 1] == best_pair[1]:
                    new_seq.append(new_word)
                    i += 2
                else:
                    new_seq.append(seq[i])
                    i += 1
            new_sequences.append(new_seq)
        sequences = new_sequences
    
    # 输出前m个词汇（题目保证result_vocab长度≥m）
    for i in range(m):
        print(result_vocab[i])

if __name__ == "__main__":
    main()