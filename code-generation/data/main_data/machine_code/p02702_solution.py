def count_pairs(S):
    count = 0
    for i in range(len(S)):
        for j in range(i, len(S)):
            num = int(S[i:j+1])
            if num % 2019 == 0:
                count += 1
    return count

S = input()
print(count_pairs(S))