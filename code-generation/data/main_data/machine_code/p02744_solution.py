def generate_normal_form_strings(N):
    import itertools
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for perm in itertools.product(alphabet, repeat=N):
        s = ''.join(perm)
        is_normal = True
        for i in range(N):
            for j in range(i+1, N):
                if i != j and s[i] < s[j]:
                    if any(s[i] == s[x] and s[j] < s[x] for x in range(N)):
                        is_normal = False
                        break
        if is_normal:
            print(s)

# Test the function
generate_normal_form_strings(1)