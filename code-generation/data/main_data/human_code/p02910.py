S = input()

s_odd = S[::2]
s_even = S[1::2]


def is_valid_str(s_list, valid_strs):
    for s in s_list:
        if s not in valid_strs:
            return False

    return True


even_ok = is_valid_str(s_even, ["L", "U", "D"])
odd_ok = is_valid_str(s_odd, ["R", "U", "D"])

if even_ok and odd_ok:
    print("Yes")
else:
    print("No")

