def analyze_records(N, M, r, records, q, queries):
    def calculate_time(start_time, end_time):
        return end_time - start_time
    
    def get_student_records(student_id, pc_id, records):
        student_records = []
        for record in records:
            if record[2] == student_id and record[1] == pc_id:
                student_records.append(record)
        return student_records
    
    def get_total_time(student_id, start_time, end_time, records):
        total_time = 0
        for record in records:
            if record[3] == 1 and record[0] >= start_time and record[0] <= end_time:
                login_time = record[0]
                logout_time = None
                for inner_record in records:
                    if inner_record[3] == 0 and inner_record[0] > login_time:
                        logout_time = inner_record[0]
                        break
                if logout_time:
                    total_time += calculate_time(login_time, logout_time)
        return total_time
    
    for query in queries:
        student_id = query[2]
        start_time = query[0]
        end_time = query[1]
        student_records = get_student_records(student_id, 1, records)
        print(get_total_time(student_id, start_time, end_time, student_records))

# Sample Input
analyze_records(4, 2, 10, [[775, 1, 1, 1], [780, 4, 2, 1], [790, 2, 1, 1], [800, 2, 1, 0], [810, 3, 1, 1], [820, 1, 1, 0], [825, 3, 1, 0], [860, 1, 1, 1], [870, 4, 2, 0], [880, 1, 1, 0]], 1, [[780, 870, 1]])