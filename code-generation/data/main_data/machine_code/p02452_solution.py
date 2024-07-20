def contains_all_elements(A, B):
    a_index = 0
    b_index = 0
    
    while a_index < len(A) and b_index < len(B):
        if A[a_index] == B[b_index]:
            b_index += 1
        a_index += 1
        
    return 1 if b_index == len(B) else 0

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

print(contains_all_elements(A, B))