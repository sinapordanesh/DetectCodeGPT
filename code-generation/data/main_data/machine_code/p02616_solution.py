def max_product_modulo(N, K, A):
    A.sort()
    mod = 10**9 + 7
    if A[-1] == 0 and K % 2 == 1:
        return 0
    
    product = 1
    if A[-1] < 0 and K % 2 == 1:
        for i in range(K):
            product = (product * A[-1-i]) % mod
        return product
    
    left, right = 0, N-1
    if K % 2 == 1:
        product = A[right]
        right -= 1
        K -= 1
    
    K //= 2
    for _ in range(K):
        left_product = A[left] * A[left+1]
        right_product = A[right] * A[right-1]
        
        if left_product > right_product:
            product = (product * left_product) % mod
            left += 2
        else:
            product = (product * right_product) % mod
            right -= 2
    
    return product % mod