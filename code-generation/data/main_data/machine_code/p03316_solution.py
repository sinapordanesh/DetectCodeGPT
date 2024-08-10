def check_divisibility(N):
    total = sum(map(int, str(N)))
    if N % total == 0:
        print("Yes")
    else:
        print("No")

# Input
N = int(input())

# Function Call
check_divisibility(N)