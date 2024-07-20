
def atc_137a(input_value: str) -> int:
    A, B = map(int, input_value.split(" "))
    return max(A + B, A - B, A * B)

input_value = input()
print(atc_137a(input_value))