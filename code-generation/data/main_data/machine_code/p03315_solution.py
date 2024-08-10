def takahashi_mind(S):
    mind = 0
    for symbol in S:
        if symbol == '+':
            mind += 1
        elif symbol == '-':
            mind -= 1
    return mind

# Test the function with the sample inputs
print(takahashi_mind("+-++"))
print(takahashi_mind("-+--"))
print(takahashi_mind("----"))