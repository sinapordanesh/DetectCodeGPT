def call(n):
    i = 1
    while i <= n:
        x = i
        if x % 3 == 0:
            print(" " + str(i), end="")
        else:
            while x:
                if x % 10 == 3:
                    print(" " + str(i), end="")
                    break
                x //= 10
        i += 1

    print()

# Input
n = int(input())
# Function Call
call(n)