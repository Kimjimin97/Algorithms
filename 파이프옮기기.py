import sys
input = sys.stdin.readline
N =int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

res = 0
visit = [[[False]*(N) for _ in range(N)] for _ in range(3)]



def dfs(x,y,d):
    global res
    if x == N-1 and y == N-1:
        res += 1
        return
    
    if d == 0:
        nx, ny = x, y+1
        if 0 <= nx < N and  0 <= ny < N:
            if graph[nx][ny] == 0 :
                dfs(nx,ny,0) 

        
        nx, ny = x+1, y+1
        nx1, ny1 = x, y+1
        nx2, ny2 = x+1, y
        if 0 <= nx < N and  0 <= ny < N:
            if graph[nx][ny] == 0 and graph[nx1][ny1] == 0 and graph[nx2][ny2] == 0 :

                    dfs(nx,ny,2) 

    
    elif d == 1:
        nx, ny = x+1, y
        if 0 <= nx < N and  0 <= ny < N:
            if graph[nx][ny] == 0 :

                dfs(nx,ny,1) 

        nx, ny = x+1, y+1
        nx1, ny1 = x, y+1
        nx2, ny2 = x+1, y
        if 0 <= nx < N and  0 <= ny < N:
            if graph[nx][ny] == 0 and graph[nx1][ny1] == 0 and graph[nx2][ny2] == 0 :

                dfs(nx,ny,2) 

    
    elif d == 2:
        nx, ny = x, y+1
        if 0 <= nx < N and  0 <= ny < N:
            if graph[nx][ny] == 0 :

                dfs(nx,ny,0) 

        nx, ny = x+1, y
        if 0 <= nx < N and  0 <= ny < N:
            if graph[nx][ny] == 0 :
                dfs(nx,ny,1) 

        nx, ny = x+1, y+1
        nx1, ny1 = x, y+1
        nx2, ny2 = x+1, y
        if 0 <= nx < N and  0 <= ny < N:
            if graph[nx][ny] == 0 and graph[nx1][ny1] == 0 and graph[nx2][ny2] == 0 :

                dfs(nx,ny,2) 


visit[0][0][0] = True
visit[1][0][0] = True
visit[2][0][0] = True

visit[0][1][0] = True
dfs(0,1,0)
print(res)