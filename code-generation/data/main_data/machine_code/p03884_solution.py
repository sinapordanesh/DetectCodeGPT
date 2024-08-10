def find_string(K):
    x = K // 7
    y = K % 7
    
    result = "FESTIVALS" * x
    if y > 0:
        result += "FESTIVALS"[:y]
    
    return result

K = int(input())
print(find_string(K))