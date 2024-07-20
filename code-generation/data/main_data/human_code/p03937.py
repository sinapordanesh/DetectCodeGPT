#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	A_fix
# CreatedDate:  2020-09-27 15:12:42 +0900
# LastModified: 2020-09-27 15:23:26 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def Possible_or_Impossible(visited, H, W):
    for v in visited:
        if -1 in v:
            return 0
    return 1



def DFS(visited, maze, H, W, u):
    visited[u[0]][u[1]] = 1
    if visited[u[0]+1][u[1]] == -1 and maze[u[0]+1][u[1]] == 1:
        if DFS(visited, maze, H, W, [u[0]+1, u[1]]) == 1:
            return 1
        visited[u[0]+1][u[1]] = -1

    if visited[u[0]][u[1]+1] == -1 and maze[u[0]][u[1]+1] == 1:
        if DFS(visited, maze, H, W, [u[0], u[1]+1]) == 1:
            return 1
        visited[u[0]][u[1]+1] = -1

    if Possible_or_Impossible(visited, H, W) == 1:
        return 1


def main():
    H, W = map(int, input().split())
    maze = [[0]*(W+2)]
    visited = [[0]*(W+2)]
    for _ in range(H):
        S = input()
        S = [0 if s == "." else 1 for s in S]
        V = [0 if s == 0 else -1 for s in S]
        S.insert(0, 0)
        V.insert(0, 0)
        S.append(0)
        V.append(0)
        maze.append(S)
        visited.append(V)
    maze.append([0]*(W+2))
    visited.append([0]*(W+2))
    if DFS(visited, maze, H, W, [1, 1]) == 1:
        print("Possible")
    else:
        print("Impossible")



if __name__ == "__main__":
    main()
