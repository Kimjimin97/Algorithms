from collections import deque
## even, ord
W,  H = map(int, input().split())

graph = [[0]*(W+2)]


for _ in range(H):
    graph.append([0]+list(map(int, input().split()))+[0])

graph.append([0]*(W+2))

## 짝수 행 탐색

even_dir = [[-1,-1],[0,-1],[1,-1],[1,0],[0,1],[-1,0]]
ord_dir = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[0,-1]]

## 홀수 행 탐색
answer = 0

## 0과 1이 인접하면
def bfs():
    global answer
    while queue:
        x,y = queue.popleft()
        if x%2 == 0: ## 짝수 행일 때
            for k in range(6):
                nx, ny = x +even_dir[k][0] , y+even_dir[k][1]

                if nx < 0 or ny < 0 or nx >= H+2 or ny >= W+2:
                    continue

                ## 1이면 count를 증가 시켜준다.
                if graph[nx][ny] == 1:
                    answer += 1

                ## 방문하지 않았고 0 일때는 탐색을 이어나가기 위해서 queue에 추가
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append([nx,ny])
                    continue
        else:
            for k in range(6):
                nx, ny = x +ord_dir[k][0] , y+ord_dir[k][1]

                if nx < 0 or ny < 0 or nx >= H+2 or ny >= W+2:
                    continue

                ## 1이면 count를 증가 시켜준다.
                if graph[nx][ny] == 1:
                    answer += 1

                ## 방문하지 않았고 0 일때는 탐색을 이어나가기 위해서 queue에 추가
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append([nx,ny])
                    continue

## 0인 그래프 찾기
visited = [[False]*(W+2) for _ in range(H+2)]
queue = deque()
queue.append([0,0])
visited[0][0] = True
bfs()
print(answer)
        