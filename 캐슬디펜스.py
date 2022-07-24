from collections import deque


N,M,D = map(int, input().split())

graphs = []

for _ in range(N):
    graphs.append(list(map(int, input().split())))


dxy = [[0,-1],[0,1],[1,0],[-1,0]]
remove_list= []


def remove(queue,graph):
    visited = [[False]*M for _ in range(N)]
    while queue:
        x,y,n = queue.popleft()
        if n == D:
            continue

        for k in range(4):
            nx, ny = x+dxy[k][0], y+ dxy[k][1]
    
            if nx < 0 or ny < 0 or nx >= len(graph) or ny >= M:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == 1:
                return nx, ny

            visited[nx][ny] = True
            queue.append([nx,ny,n+1])

    return -1, -1


res = float("-Inf")
## 정해진 궁수 위치에서 완탐 시작하기
def start(position_loca):
    global res
    graph = [[graphs[i][j] for j in range(M)] for i in range(N)]
    cnt = 0
    answer = 0
    while cnt < N :
        remove_list =[]
        for q in position_loca:
            queue = deque()
            queue.append([len(graph), q,0])
            a,b = remove(queue,graph)
            if a == -1 and b== -1:
                continue

            if [a,b] not in remove_list:
                remove_list.append([a,b])
        
        for c,d in remove_list:
            graph[c][d] = 0
            answer += 1
        
        graph.pop(-1)
        cnt += 1

    res = max(res, answer)
        
        
        
    

position_loca = []
## 궁수 위치 조합 재귀
def position(n):
    global position_loca
    if n == M:
        if len(position_loca) == 3:
            # print(position_loca)
            start(position_loca)
        return

    position_loca.append(n)
    position(n+1)
    position_loca.pop()
    position(n+1)

position(0)
print(res)


