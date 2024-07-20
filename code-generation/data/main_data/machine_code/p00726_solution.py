def uncompress_genome_sequences(s, i):
    stack = []
    repeat = 0
    seq = ""
    
    for char in s:
        if char.isdigit():
            repeat = repeat * 10 + int(char)
        elif char == "(":
            stack.append((seq, repeat))
            seq = ""
            repeat = 0
        elif char == ")":
            last_seq, last_repeat = stack.pop()
            seq = last_seq + seq * last_repeat
        else:
            seq += char
    
    if i < len(seq):
        return seq[i]
    else:
        return 0

# Sample Input
print(uncompress_genome_sequences("ABC", 3))
print(uncompress_genome_sequences("ABC", 0))
print(uncompress_genome_sequences("2(4(AB)3(XY))10C", 30))
print(uncompress_genome_sequences("1000(1000(1000(1000(1000(1000(NM))))))", 999999))