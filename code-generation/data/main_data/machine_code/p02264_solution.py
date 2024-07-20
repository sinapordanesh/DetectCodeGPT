def round_robin_schedule(n, q, processes):
    queue = []
    total_time = 0
    for process in processes:
        queue.append(process)

    while queue:
        current_process = queue.pop(0)
        if current_process[1] > q:
            total_time += q
            current_process = (current_process[0], current_process[1] - q)
            queue.append(current_process)
        else:
            total_time += current_process[1]
            print(current_process[0], total_time)

n, q = map(int, input().split())
processes = []
for _ in range(n):
    name, time = input().split()
    processes.append((name, int(time)))

round_robin_schedule(n, q, processes)