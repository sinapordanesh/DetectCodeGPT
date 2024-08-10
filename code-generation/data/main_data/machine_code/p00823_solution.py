def molecular_formula_weight(atomic_table, molecular_formulas):
    atomic_weights = {}
    for item in atomic_table:
        symbol, weight = item.split()
        atomic_weights[symbol] = int(weight)

    def calculate_weight(formula):
        stack = []
        current_num = 1
        total_weight = 0
        for char in formula:
            if char == '(':
                stack.append(total_weight)
                stack.append(current_num)
                total_weight = 0
                current_num = 1
            elif char == ')':
                num = stack.pop()
                prev_weight = stack.pop()
                total_weight = prev_weight + num * total_weight
            elif char.isdigit():
                current_num = int(char)
            else:
                total_weight += atomic_weights[char] * current_num
                current_num = 1
        return total_weight

    result = []
    for formula in molecular_formulas:
        if all(char.isalpha() and char.isupper() for char in formula):
            result.append(str(calculate_weight(formula)))
        else:
            result.append("UNKNOWN")
    return result

atomic_table = ["H 1", "He 4", "C 12", "O 16", "F 19", "Ne 20", "Cu 64", "Cc 333"]
molecular_formulas = ["H2C", "(MgF)2As", "Cu(OH)2", "H((CO)2F)99"]

molecular_formula_weight(atomic_table, molecular_formulas)