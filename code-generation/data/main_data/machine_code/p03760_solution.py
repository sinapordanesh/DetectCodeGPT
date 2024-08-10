def restore_password(O, E):
    password = ''
    i = 0
    for char in O:
        password += char
        if i < len(E):
            password += E[i]
        i += 1
    return password

# Call the function with the given sample input
print(restore_password("xyz", "abc"))
print(restore_password("atcoderbeginnercontest", "atcoderregularcontest"))