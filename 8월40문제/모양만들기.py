import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

## bfs로 1 모두 잇기 O(V^2) ~ 10^6
count_list = [0,0]
L = 2
visited = [[False]*M for _ in range(N)]
dxy = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(i,j,L):
    queue = deque()
    queue.append([i,j])
    visited[i][j] = True
    graph[i][j] = L
    # cnt = 1 
    cnt = 0
    while queue:
        x,y = queue.popleft()
        #####
        cnt += 1
        for k in range(4):
            nx, ny = x+dxy[k][0], y+dxy[k][1]
            if 0 > nx or 0 > ny or N <= nx or M <= ny:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == 1:
                #####
                visited[nx][ny] = True
                graph[nx][ny] = L
                queue.append([nx,ny])
    return cnt


for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            if not visited[i][j]:
                count_list.append(bfs(i,j,L))
                L+=1

### 주의
answer = float("-Inf")


for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            one_cnt = 1
            one_lists = set()
            for k in range(4):
                nx,ny = i+dxy[k][0], j+dxy[k][1]
                if 0 > nx or 0 > ny or N <= nx or M <= ny:
                    continue
                if graph[nx][ny] >= 1:
                    one_lists.add(graph[nx][ny])
                    #### 이어질 수 있다.
            
            one_lists = list(one_lists)
            for d in one_lists:
            #######
                one_cnt += count_list[d]
            answer = max(answer, one_cnt)
                    
print(answer)