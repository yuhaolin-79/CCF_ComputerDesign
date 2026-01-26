import sys

def main():
    line1 = sys.stdin.readline().split()
    n, m = map(int, line1)
    
    word_freq = {}
    chars = set()
    for _ in range(n):
        line = sys.stdin.readline().split()
        s, f = line[0], int(line[1])
        word_freq[s] = word_freq.get(s, 0) + f
        for char in s:
            chars.add(char)
            
    vocab = sorted(list(chars))
    for v in vocab:
        print(v)
    
    if len(vocab) >= m:
        return
    
    words_split = {word: list(word) for word in word_freq}
    
    for _ in range(m - len(vocab)):
        pair_freqs = {}
        for word, seq in words_split.items():
            f = word_freq[word]
            if len(seq) < 2:
                continue
            for i in range(len(seq) - 1):
                pair = (seq[i], seq[i+1])
                pair_freqs[pair] = pair_freqs.get(pair, 0) + f
                
        if not pair_freqs:
            break
        
        best_pair = None
        max_f = -1
        
        for pair, f in pair_freqs.items():
            combined = pair[0] + pair[1]
            curr_key = (-f, len(combined), len(pair[0]), combined)
            
            if best_pair is None or curr_key < best_key:
                best_pair = pair
                best_key = curr_key
                
        new_token = best_pair[0] + best_pair[1]
        print(new_token)
        
        target_p1, target_p2 = best_pair
        for word in words_split:
            seq = words_split[word]
            new_seq = []
            i = 0
            while i < len(seq):
                if i < len(seq) - 1 and seq[i] == target_p1 and seq[i+1] == target_p2:
                    new_seq.append(new_token)
                    i += 2
                else:
                    new_seq.append(seq[i])
                    i += 1
            words_split[word] = new_seq
            
if __name__ == "__main__":
    main()