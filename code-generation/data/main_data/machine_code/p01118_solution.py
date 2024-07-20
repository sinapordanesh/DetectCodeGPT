def on_screen_keyboard(h, w, OSK, s):
    def find_char(char):
        for i in range(h):
            for j in range(w):
                if OSK[i][j] == char:
                    return (i, j)
        return None

    def min_button_presses(start, end):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        cur_pos = start
        total_presses = 0
        for char in end:
            next_pos = find_char(char)
            total_presses += abs(next_pos[0] - cur_pos[0]) + abs(next_pos[1] - cur_pos[1]) + 1
            cur_pos = next_pos
        return total_presses

    return min_button_presses((0, 0), s)


# Sample Input
print(on_screen_keyboard(3, 9, ["ABCDEFGHI", "JKLMNOPQR", "STUVWXYZ_"], "ICPC"))  
print(on_screen_keyboard(5, 11, ["___________", "____A______", "________M__", "___________", "_C_________"], "ACM"))
print(on_screen_keyboard(4, 21, ["1_2_3_4_5_6_7_8_9_0_-", "QqWwEeRrTtYyUuIiOoPp@", "AaSsDdFfGgHhJjKkLl;_:", "ZzXxCcVvBbNnMm,_._/__"], "ICPC2019,AsiaYokohamaRegional,QualificationRound"))