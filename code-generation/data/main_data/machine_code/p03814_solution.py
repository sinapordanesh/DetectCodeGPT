def construct_string(s):
    start = s.index('A')
    end = s.rindex('Z')
    return end - start + 1

# Sample Test Cases
print(construct_string("QWERTYASDFZXCV")) # 5
print(construct_string("ZABCZ")) # 4
print(construct_string("HASFJGHOGAKZZFEGA")) # 12