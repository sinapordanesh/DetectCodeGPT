def can_complete_jobs(N, jobs):
    current_time = 0
    for job in jobs:
        if current_time + job[0] > job[1]:
            return "No"
        current_time += job[0]
    return "Yes"