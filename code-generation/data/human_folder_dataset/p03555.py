def atc_077a(input_value: str) -> str:
    C1 = input_value[0]
    C2 = input_value[1]

    if C1[0] == C2[2] and C1[1] == C2[1] and C1[2] == C2[0]:
        return "YES"
    else:
        return "NO"


C1 = input()
C2 = input()
print(atc_077a([C1, C2]))