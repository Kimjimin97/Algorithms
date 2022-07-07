from sys import stdin
from collections import deque



N,M,K = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

dp = [[[-1]*(K+1)for _ in range(M) ] for _ in range(N)]


queue = deque()
queue.append((0,0,0))
dp[0][0][0] = 0
dxy = [[0,1],[1,0],[-1,0],[0,-1]]
flag= True
while queue:
    x,y,z = queue.popleft()
    if x== N-1 and y== M-1:
        flag= False
        print(dp[x][y][z]+1)
        break

    for k in range(4):
        nx, ny, nz = x+dxy[k][0], y+dxy[k][1] , z+1
        if 0 > nx or 0> ny or N <= nx or M <= ny:
            continue 
        if graph[nx][ny] == 1:
            if nz <= K and dp[nx][ny][nz] == -1:
                dp[nx][ny][nz] = dp[x][y][z] + 1 
                queue.append((nx,ny,nz))

        else:
            if dp[nx][ny][z] == -1:
                dp[nx][ny][z] = dp[x][y][z] + 1
                queue.append((nx,ny,z))

if flag:
    print(-1)