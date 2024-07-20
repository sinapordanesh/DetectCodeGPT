def bound_to_work(N, K, C, S):
    work_days = []
    for i in range(N):
        if S[i] == "o":
            if len(work_days) == 0 or i - work_days[-1] > C:
                work_days.append(i+1)
                if len(work_days) == K:
                    break
    return work_days

N, K, C = map(int, input().split())
S = input()
result = bound_to_work(N, K, C, S)
for day in result:
    print(day)