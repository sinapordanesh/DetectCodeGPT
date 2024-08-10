def max_rectangle(a_I, a_O, a_T, a_J, a_L, a_S, a_Z):
    max_K = 0
    if a_I >= 1 and a_O >= 1 and a_T >= 1:
        max_K = min(a_I, a_O, a_T) * 2
    return max_K

a_I, a_O, a_T, a_J, a_L, a_S, a_Z = map(int, input().split())
print(max_rectangle(a_I, a_O, a_T, a_J, a_L, a_S, a_Z))