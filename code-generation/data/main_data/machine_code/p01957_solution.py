def validate_tournament_chart(S, results):
    def dfs(chart):
        if len(chart) == 1:
            return 1
        left = chart[1]
        right = chart[3]
        left_result = dfs(left)
        right_result = dfs(right)
        if left_result == -1 or right_result == -1:
            return -1
        if left_result != right_result:
            return -1
        return left_result + 1

    chart = S[2:-2].split("]-[")
    chart = [x.split("-") for x in chart]
    results_dict = {}
    for result in results:
        results_dict[result[0]] = result[1]
    for i in range(len(chart)):
        chart[i] = [x.strip("[]") for x in chart[i]]
    result = dfs(chart)
    if result == -1:
        print("No")
    else:
        valid = True
        for key, value in results_dict.items():
            if result != value:
                valid = False
                break
        if valid:
            print("Yes")
        else:
            print("No")

# Sample Input 1
S1 = "[[m-y]-[a-o]]"
results1 = [("o", 0), ("a", 1), ("y", 2), ("m", 0)]
validate_tournament_chart(S1, results1)

# Sample Input 2
S2 = "[[r-i]-[m-e]]"
results2 = [("e", 0), ("r", 1), ("i", 1), ("m", 2)]
validate_tournament_chart(S2, results2)