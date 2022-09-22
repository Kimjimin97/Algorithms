import sys
from collections import deque

input =  sys.stdin.readline
N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(str, input())))

answer = 0

dxy = [[1,0],[-1,0],[0,1],[0,-1]]

visited =  [[False]*M for _ in range(N)]

def bfs(i,j):
    global visited 
    global answer 
    queue = deque()
    queue.append([i,j,0])
    visited[i][j] = True
    while queue:
        x,y,d = queue.popleft()
        answer = max(answer,d)
        for k in range(4):
            nx, ny = x+ dxy[k][0], y +dxy[k][1]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == "W":
                continue
            if visited[nx][ny]:
                continue

            visited[nx][ny] = True
            queue.append([nx,ny, d+1])



for i in range(N):
    for j in range(M):
        if graph[i][j] == "W":
            continue
        visited =  [[False]*M for _ in range(N)]
        bfs(i,j)


print(answer)

