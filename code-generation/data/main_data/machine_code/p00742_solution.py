def verbal_arithmetic(data):
    results = []
    for i in range(0, len(data), 2):
        n = int(data[i])
        equation = data[i+1:]
        count = 0
        for j in range(10 ** n):
            values = {chr(ord('A') + k): int(str(j)[k]) for k in range(n)}
            if sum(evaluate(equation, values)) == 0:
                count += 1
        results.append(count)
    return results

def evaluate(equation, values):
    result = []
    for term in equation:
        val = 0
        for char in term:
            val = val * 10 + values[char]
        result.append(val)
    return result

data = [
    "3",
    "ACM",
    "IBM",
    "ICPC",
    "3",
    "GAME",
    "BEST",
    "GAMER",
    "4",
    "A",
    "B",
    "C",
    "AB",
    "3",
    "A",
    "B",
    "CD",
    "3",
    "ONE",
    "TWO",
    "THREE",
    "3",
    "TWO",
    "THREE",
    "FIVE",
    "3",
    "MOV",
    "POP",
    "DIV",
    "9",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "IJ",
    "0"
]

print(*verbal_arithmetic(data), sep="\n")