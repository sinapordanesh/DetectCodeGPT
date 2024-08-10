def base_minus_2_representation(N):
    if N == 0:
        return "0"
    
    result = ""
    while N != 0:
        remainder = N % -2
        N = N // -2
        if remainder < 0:
            remainder += 2
            N += 1
        result = str(remainder) + result
    
    return result

# Test cases
print(base_minus_2_representation(-9))
print(base_minus_2_representation(123456789))
print(base_minus_2_representation(0))