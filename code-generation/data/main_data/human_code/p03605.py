def atc_073a(N: int) -> str:
    try:
        str(N).index("9")
        return "Yes"
    except ValueError:
        return "No"

N = int(input())
print(atc_073a(N))