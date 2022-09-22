from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

graph  = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = [[False]*M for _ in range(N)]
dxy = [[0,1],[0,-1],[1,0],[-1,0]]

## bfs 방문처리 공부

def bfs(i,j):
    global visited
    global new_graph
    queue = deque()
    queue.append([i,j])
    visited[i][j] = True

    while queue:
        x,y = queue.popleft()
    
        now_data = graph[x][y]
        for k in range(4):
            nx, ny = x+dxy[k][0], y+ dxy[k][1]
            if 0 > nx or 0 > ny or N <= nx or M <= ny or visited[nx][ny]:
                continue
            if graph[nx][ny] == 0:
                now_data -= 1
            else: 
                queue.append([nx, ny])
                visited[nx][ny] = True
                
        
        if now_data < 0:
            new_graph[x][y] = 0
        else:
            new_graph[x][y] = now_data

    return
    

## 두가지 측정 기준이 필요하다 
## 년도 year
## 이어져 있는 갯수 cnt
year = 0
while True:
    ## 두 덩이 이상이 나올 때까지 while문 돈다
    ## 두 덩이가 이상 나온다는 판단 -> bfs가 2번 돈다.

    if year == 10000:
        print(0)
        break

    cnt = 0
    visited = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            ## bfs 탐색 시작
            ## 2개 이상 덩어리가 존재한다는 의미이다.
  

            if not visited[i][j] and graph[i][j] >= 1:
                ## 탐색 덩어리 확인
                cnt += 1
                if cnt == 2:
                    print(year)
                    sys.exit()
                    
                else:
                    new_graph = [[graph[i][j] for j in range(M)] for i in range(N)]
                    bfs(i,j)
                    graph = [[new_graph[i][j] for j in range(M)] for i in range(N)]
    year += 1

             