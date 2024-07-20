def calculate_expression(expression):
    try:
        result = eval(expression)
        if abs(result.real) > 10000 or abs(result.imag) > 10000:
            return "overflow"
        if result.real == 0 and result.imag == 0:
            return "0"
        if result.real == 0:
            return f"{result.imag}i"
        if result.imag == 0:
            return str(result.real)
        return f"{result.real}{result.imag:+}i"
    except:
        return "overflow"

sample_input = [
    "(1-10*1)+00007+(3+10*1)",
    "3+4*1*(4+10*1)",
    "(102+10*1)*(99+10*1)",
    "2*1+3+9999*1+4"
]

for exp in sample_input:
    print(calculate_expression(exp))