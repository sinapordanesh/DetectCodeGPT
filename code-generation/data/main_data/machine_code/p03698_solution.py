def all_characters_different(S):
    if len(set(S)) == len(S):
        return "yes"
    else:
        return "no"