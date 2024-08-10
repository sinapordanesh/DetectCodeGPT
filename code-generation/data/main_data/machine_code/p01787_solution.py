def rle_replacement(A, B, C):
    def decode_RLE(s):
        result = []
        i = 0
        while i < len(s):
            result.append((s[i], int(s[i+1])))
            i += 2
        return result
    
    def encode_RLE(arr):
        result = ""
        for c, l in arr:
            result += c + " " + str(l) + " "
        return result + "$"
    
    A = decode_RLE(A)
    B = decode_RLE(B)
    C = decode_RLE(C)
    
    for i in range(len(A) - len(B) + 1):
        if A[i:i+len(B)] == B:
            A = A[:i] + C + A[i+len(B):]
            break
    
    return encode_RLE(A)

A = "R 100 L 20 E 10 $"
B = "R 5 L 10 $"
C = "X 20 $"
print(rle_replacement(A, B, C))

A = "A 3 B 3 A 3 $"
B = "A 1 B 3 A 1 $"
C = "A 2 $"
print(rle_replacement(A, B, C))