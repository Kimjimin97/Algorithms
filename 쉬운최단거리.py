from collections import deque
n, m = map(int, input().split())

graph = []

for i in range(n):
    lists = list(map(int, input().split()))
    graph.append(lists)
    for j in range(m):
        if graph[i][j] == 2:
            endx = i
            endy = j
    

answer = [[-1]*m for _ in range(n)]

dxy = [[1,0],[-1,0],[0,1],[0,-1]]

visited = [[False]*m for _ in range(n)]

queue = deque()
queue.append((endx,endy,0))
visited[endx][endy] = True


while queue:
    top = queue.popleft()
    
    for k in range(4):
        nx, ny = top[0] +dxy[k][0], top[1]+dxy[k][1]
        if 0 <= nx < n and 0 <= ny < m :
            if not visited[nx][ny]:
                if graph[nx][ny]!=0:
                    answer[nx][ny] = top[2] +1
                    visited[nx][ny] = True
                    queue.append([nx,ny,top[2]+1])
                    
                elif graph[nx][ny] == 0:
                    answer[nx][ny] = 0
                    visited[nx][ny] = True
                
                # elif graph[nx][ny] == 2:
                #     answer[nx][ny] = 0

answer[endx][endy] = 0

for k in range(len(answer)):
    print(*answer[k])