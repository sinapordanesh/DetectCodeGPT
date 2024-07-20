def ways_to_put_notice(N, H, W):
    return (N-H+1) * (N-W+1) if H <= N and W <= N else 0
