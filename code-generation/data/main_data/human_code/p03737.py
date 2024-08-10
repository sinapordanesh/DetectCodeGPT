def abc059a(s1: str, s2: str, s3: str) ->str:
    return s1[0].upper() + s2[0].upper() + s3[0].upper()

s1, s2, s3 = map(str, input().split())
print(abc059a(s1, s2, s3))
