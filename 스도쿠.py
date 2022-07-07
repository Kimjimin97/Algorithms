import sys


import sys
input = sys.stdin.readline

graph = []
zero = []

for i in range(9):
    lists = list(map(int, input().split()))
    graph.append(lists)
    for j in range(9):
        if graph[i][j] == 0:
            zero.append([i,j])


def ga(x,y,k):
    flag = True
    for j in range(9):
        if graph[x][j] == k:
            flag= False
            return False
    if flag:
        return True

def se(x,y,k):
    flag = True
    for i in range(9):
        if graph[i][y] == k:
            flag= False
            return False
    if flag:
        return True

def nemo(x,y,k):
    start_x = (x//3)*3
    start_y = (y//3)*3
    flag= True
    for i in range(start_x, start_x+3):
        for j in range(start_y, start_y+3):
            if graph[i][j] == k:
                flag = False 
                return False
    if flag:
        return True


def dfs(L):
    # print(graph)
    if L == len(zero):
        for g in graph:
            print(*g)
        exit(0)
        return

    x,y = zero[L][0], zero[L][1]

    for k in range(1,10):
        if not ga(x,y,k):
            continue

        if not se(x,y,k):
            continue

        if not nemo(x,y,k):
            continue 

        graph[x][y] = k
        dfs(L+1)
        graph[x][y] = 0

dfs(0)