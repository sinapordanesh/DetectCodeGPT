#!/usr/bin/env python
# -*- coding: utf-8 -*-

from heapq import heappop,heappush

def bfs(sx,sy,W,H):
    queue = []
    heappush(queue,(0,sx,sy))
    dxdy = [(0,1),(0,-1),(1,0),(-1,0)]
    visited = [[ 10**8 for i in range(W)] for j in range(H)]

    while queue != []:
        count,x,y = heappop(queue)
        if visited[y][x] != 10**8:
            continue
        visited[y][x] = count
        for nx,ny in dxdy:
            if 0 <= x + nx < W and 0 <= y + ny < H:
                if visited[y + ny][x + nx] == 10**8:
                    nextValue = Maze[y + ny][x + nx]
                    if ((nx,ny) == (1,0) and nextValue & 1 > 0) or ((nx,ny) == (0,1) and nextValue & 2 > 0) or ((nx,ny) == (-1,0) and Maze[y][x] & 1 > 0) or ((nx,ny) == (0,-1) and Maze[y][x] & 2 > 0 ):
                        continue
                    else:
                        heappush(queue,(count + 1,x+nx,y+ny))
    return visited

while True:
    w,h = map(int,input().split(" "))
    if h == 0 and w == 0:
        break
    Maze = [[0 for j in range(w)] for i in range(h)]
    for i in range(h-1):
        row = list(map(int,input().split()))
        for j in range(len(row)):
            if row[j] == 1:
                Maze[i][j+1] += 1
        col = list(map(int,input().split()))
        for j in range(len(col)):
            if col[j] == 1:
                Maze[i+1][j] += 2
    else:
        i += 1
        row = list(map(int,input().split()))
        for j in range(len(row)):
            if row[j] == 1:
                Maze[i][j+1] += 1

    ret = bfs(0,0,w,h)[h-1][w-1]
    print(ret + 1 if ret != 10**8 else 0) 