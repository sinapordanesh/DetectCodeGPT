def icpc_ranking(input_data):
    datasets = input_data.strip().split('\n\n')
    results = []

    for data in datasets:
        lines = data.strip().split('\n')
        M, T, P, R = map(int, lines[0].split())

        team_problems = {team: [0] * P for team in range(1, T + 1)}
        team_time = {team: 0 for team in range(1, T + 1)}
        team_penalty = {team: [0] * P for team in range(1, T + 1)}

        for record in lines[1:]:
            m, t, p, j = map(int, record.split())
            if j == 0:
                team_problems[t - 1][p - 1] = 1
                team_time[t - 1] += m + 20 * team_penalty[t - 1][p - 1]
            else:
                team_penalty[t - 1][p - 1] += 1

        ranking = sorted(range(1, T + 1), key=lambda x: (-sum(team_problems[x]), team_time[x]))

        results.append(','.join(map(str, ranking)))

    return '\n'.join(results)