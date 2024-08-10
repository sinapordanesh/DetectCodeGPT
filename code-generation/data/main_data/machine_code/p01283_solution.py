def strange_string_manipulation():
    def entropy(s, a, c, string):
        n = len(string)
        freq = {}
        for char in string:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        entropy = 0
        for key in freq:
            prob = freq[key] / n
            entropy -= prob * math.log(prob, 2)
        return entropy

    while True:
        N = int(input())
        if N == 0:
            break
        data = list(map(int, input().split()))
        min_entropy = float('inf')
        res = (0, 0, 0)
        for S in range(16):
            for A in range(16):
                for C in range(16):
                    output = [(S*A*i + C) % 256 for i in range(N)]
                    current_entropy = entropy(S, A, C, output)
                    if current_entropy < min_entropy:
                        min_entropy = current_entropy
                        res = (S, A, C)
        print(res[0], res[1], res[2])

strange_string_manipulation()