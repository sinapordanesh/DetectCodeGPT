def find_shortest_correct_bracket_sequence(N, S):
    stack = []
    for bracket in S:
        if bracket == '(':
            stack.append('(')
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
    
    answer = ''.join(stack)
    return answer

N = int(input())
S = input()
print(find_shortest_correct_bracket_sequence(N, S))