def sliding_minimum_element(N, L, arr):
    from collections import deque

    result = []
    min_q = deque()

    for i in range(N):
        while min_q and min_q[0] < i - L + 1:
            min_q.popleft()
        
        while min_q and arr[min_q[-1]] > arr[i]:
            min_q.pop()

        min_q.append(i)

        if i >= L - 1:
            result.append(arr[min_q[0]])

    return result

# Sample Input
N = 7
L = 3
arr = [1, 7, 7, 4, 8, 1, 6]
print(*sliding_minimum_element(N, L, arr))