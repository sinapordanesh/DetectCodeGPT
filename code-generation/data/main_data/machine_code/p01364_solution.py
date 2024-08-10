def final_position(N, D, instructions):
    x = 0
    y = 0
    for instr in instructions:
        Lspeed, Rspeed, time = instr
        vx = (Lspeed + Rspeed) / 2
        vy = (Rspeed - Lspeed) / 2
        theta = vx * time
        delta_x = D * (1 - cos(radians(theta)))
        delta_y = D * sin(radians(theta))
        x += delta_x
        y += delta_y
    return x, y