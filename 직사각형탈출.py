"""
시간 복잡도
O(V+E) =??
"""
import sys
from collections import deque
input= sys.stdin.readline
N,M = map(int, input().split())


graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

H, W, Sx,Sy,Fx,Fy = map(int, input().split())

dxy = [(1,0),(-1,0),(0,-1),(0,1)]


S = [[0]*M for _ in range(M)]


for i in range(N):
    for j in range(M):
        if j+1 < M:
            S[i][j+1] = graph[i][j+1] + S[i][j]
        
        if i+1 < N:
            S[i+1][j] = graph[i+1][j] + S[i][j]


print(S)

answer = float("Inf")
queue = deque()
visited = [[False]*M for _ in range(N)]

visited[Sx-1][Sy-1] = True
queue.append([Sx-1,Sy-1,0])

while queue:
    top = queue.popleft()

    if top[0] == Fx-1 and top[1] ==Fy-1 :
        answer = top[2]
        break

    for k in range(4):
        nx, ny = top[0] + dxy[k][0], top[1] + dxy[k][1]
    
        #범위
        if nx < 0 or ny < 0 or nx > N-H or ny > M-W:
            continue

        # 방문 여부
        if visited[nx][ny]:
            continue

        flag = True
        for i in range(H):
            for j in range(W):
                if graph[nx+i][ny+j] != 0:
                    flag = False
                    break
            if not flag:
                break

        if flag:
            visited[nx][ny] = True
            queue.append((nx,ny,top[2]+1))

if answer == float("Inf"):
    print(-1)
else:
    print(answer)

        
                    
    

