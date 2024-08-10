def non_decreasing_sequence(N, A, B):
    def is_non_decreasing(nums):
        return all(nums[i] <= nums[i+1] for i in range(len(nums)-1))

    if is_non_decreasing(A):
        return 0
    for i in range(N-1):
        if A[i] > B[i] and A[i+1] > B[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
            B[i], B[i+1] = B[i+1], B[i]
    return 1 if is_non_decreasing(A) else -1