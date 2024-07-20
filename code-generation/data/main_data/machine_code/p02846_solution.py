def meet_times(T1, T2, A1, A2, B1, B2):
    if A1 * T1 + A2 * T2 == B1 * T1 + B2 * T2:
        return "infinity"
    else:
        lcm = (T1 * T2) // math.gcd(T1, T2)
        t = (A1 * T1 - B1 * T1) * lcm // ((B1 - A1) * T1 + (B2 - A2) * T2)
        if t <= 0:
            return 0
        else:
            if (A1 * T1 < B1 * T1 and A1 * T1 + A2 * T2 < B1 * T1) or (B1 * T1 < A1 * T1 and B1 * T1 + B2 * T2 < A1 * T1):
                return 0
            else:
                if (A1 * T1 == B1 * T1) or (A1 * T1 + A2 * T2 == B1 * T1):
                    return t * 2 - 1
                else:
                    return t * 2

T1, T2, A1, A2, B1, B2 = map(int, input().split())
print(meet_times(T1, T2, A1, A2, B1, B2))