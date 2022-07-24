import sys
input= sys.stdin.readline
N, M = map(int, input().split())

graph = []


for _ in range(N):
    graph.append(list(map(int, input().split())))


dxy = [[1,0],[-1,0],[0,1],[0,-1]]

answer = float("-Inf")
visited = [[False] * M for _ in range(N)]

def dfs(x,y,n,sums):
    global answer
    global visited

    if n == 3:
        answer = max(answer, sums)
        return
    
    
    for k in range(4):
        nx, ny = x +dxy[k][0], y+dxy[k][1]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if visited[nx][ny]:
            continue
        if n == 1:
            visited[nx][ny] = True
            dfs(x,y,n+1, sums + graph[nx][ny])
            visited[nx][ny] = False 

        visited[nx][ny] = True
        dfs(nx,ny,n+1, sums + graph[nx][ny])
        visited[nx][ny] = False
    


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i,j,0,graph[i][j])
        visited[i][j] = False

print(answer)