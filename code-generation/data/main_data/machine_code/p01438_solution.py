def max_satisfaction():
    while True:
        n = int(input())
        if n == 0:
            break
        total_satisfaction = 0
        for _ in range(n):
            m, l = map(int, input().split())
            dates = []
            for _ in range(m):
                s, e = map(int, input().split())
                dates.append((s, e))
            dates.sort(key=lambda x: x[1])
            available_slots = [(6, 22)]
            satisfaction = 0
            for start, end in dates:
                for i, (slot_start, slot_end) in enumerate(available_slots):
                    if start >= slot_end:
                        continue
                    if end <= slot_start:
                        continue
                    if start <= slot_start and end >= slot_end:
                        satisfaction += end - start
                        available_slots = available_slots[:i] + available_slots[i + 1:]
                        break
                    if start > slot_start and end >= slot_end:
                        satisfaction += slot_end - start
                        available_slots = available_slots[:i] + [(slot_end, slot_end)] + available_slots[i + 1:]
                    if start <= slot_start and end < slot_end:
                        satisfaction += end - slot_start
                        available_slots = available_slots[:i] + [(end, slot_end)] + available_slots[i + 1:]
                    if start > slot_start and end < slot_end:
                        satisfaction += end - start
                        available_slots = available_slots[:i] + [(slot_start, start), (end, slot_end)] + available_slots[i + 1:]
                total_satisfaction += satisfaction * l
        print(total_satisfaction)

max_satisfaction()