def best_matched_pair(N, arr):
    arr.sort(reverse=True)
    for i in range(N-1):
        num1 = str(arr[i])
        num2 = str(arr[i+1])
        if len(num1) != len(num2):
            continue
        valid = True
        for j in range(len(num1)-1):
            if int(num1[j]) + 1 != int(num1[j+1]):
                valid = False
                break
        if valid:
            return arr[i] * arr[i+1]
    return -1

# Read input values
N = int(input())
arr = list(map(int, input().split()))

# Call the function and print the result
print(best_matched_pair(N, arr))