def is_keyence_string(s):
    if "keyence" in s:
        print("YES")
    else:
        for i in range(len(s)):
            for j in range(i, len(s)):
                new_s = s[:i] + s[j+1:]
                if "keyence" in new_s:
                    print("YES")
                    return
        print("NO")