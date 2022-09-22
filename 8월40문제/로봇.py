import sys
from collections import deque

input= sys.stdin.readline

N, M = map(int, input().split())


route = []
for _ in range(N):
    route.append(list(map(int, input().split())))

sx,sy,sd = map(int, input().split())
ex,ey,ed = map(int, input().split())


sx,sy,sd = sx -1 ,sy -1, sd -1
ex,ey,ed = ex-1 ,ey -1 ,ed -1


graph = [[[0]*4   for _ in range(M) ]for _ in range(N)]
visited = [[[False]*4   for _ in range(M) ]for _ in range(N)]

queue = deque()
dxy = [[0,1],[0,-1],[1,0],[-1,0]]

graph[sx][sy][sd] = 0
visited[sx][sy][sd] = True
queue.append([sx,sy,sd])

ro = [[2,3],[2,3],[0,1],[0,1]]

while queue:
    x,y,d = queue.popleft()
    if x == ex and y == ey and d == ed:
        print(graph[x][y][d])
        break
    
    for k in range(4):

        if not visited[x][y][k]:
            if k in ro[d]:
                graph[x][y][k] += graph[x][y][d] + 1
                visited[x][y][k] = True
                queue.append([x,y,k])
            # else:
            #     graph[x][y][k] += graph[x][y][d] + 2
            #     visited[x][y][k] = True
            #     queue.append([x,y,k])

    nx, ny = x, y
    for kk in range(3):
        nx, ny =  nx+dxy[d][0], ny+dxy[d][1]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if route[nx][ny] == 1:
            break
        if visited[nx][ny][d]:
            continue
        
  
        visited[nx][ny][d] = True
        graph[nx][ny][d] += (graph[x][y][d]+1)
        queue.append([nx,ny,d])




    # for g in graph:
    #     print(g)
    # print()

    # for g in visited:
    #     print(g)
    # print()