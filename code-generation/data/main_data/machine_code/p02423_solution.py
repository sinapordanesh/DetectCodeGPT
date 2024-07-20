def bit_operations(x):
    b = bin(x)[2:].zfill(32)
    inv = ''.join(['1' if bit == '0' else '0' for bit in b])
    left_shift = b[1:] + '0'
    right_shift = '0' + b[:-1]
    
    print(b)
    print(inv)
    print(left_shift)
    print(right_shift)

# Sample Test Cases
bit_operations(8)
bit_operations(13)