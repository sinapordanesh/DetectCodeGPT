def possible_candidates(A, B):
    count = 0
    for i in range(A, B+1):
        if i | A <= B:
            count += 1
    return count

A, B = map(int, input().split())
print(possible_candidates(A, B))