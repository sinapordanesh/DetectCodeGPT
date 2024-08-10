def find_permutation(N, A, B):
    if format(A, 'b').count('1') % 2 != format(B, 'b').count('1') % 2:
        return "NO"
    res = []
    for i in range(2**N):
        if i != A and i != B:
            res.append(i)
    if format(A ^ res[0], 'b').count('1') % 2 == 1:
        res = [B] + res + [A]
    else:
        res = [A] + res + [B]
    return "YES\n" + " ".join(map(str, res))

N, A, B = map(int, input().split())
print(find_permutation(N, A, B))