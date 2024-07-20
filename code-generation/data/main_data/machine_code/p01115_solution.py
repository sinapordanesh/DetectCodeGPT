def expression_mining(n, s):
    def evaluate(expression):
        return eval(expression.replace('*', '*').replace('+', '+'))
    
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub = s[i:j]
            if sub.count('(') == sub.count(')') and evaluate(sub) == n:
                count += 1
    return count

while True:
    n = int(input())
    if n == 0:
        break
    s = input()
    print(expression_mining(n, s))