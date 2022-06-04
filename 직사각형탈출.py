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


S = [[0]*M for _ in range(N)]


for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            S[i][j] = S[i][j-1] + graph[i][j]
        
        elif j == 0:
            S[i][j] = S[i-1][j] + graph[i][j]
        
        else:
            S[i][j] = S[i-1][j] + S[i][j-1] + graph[i][j] - S[i-1][j-1]


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
        

        if nx == 0 and ny == 0:
            if S[nx+H-1][ny+W-1] == 0:
                visited[nx][ny] = True
                queue.append((nx,ny,top[2]+1))

        elif nx == 0:
            if S[nx+H-1][ny+W-1] -S[nx+H-1][ny-1] == 0:
                visited[nx][ny] = True
                queue.append((nx,ny,top[2]+1))
        
        elif ny == 0:
            if S[nx+H-1][ny+W-1]- S[nx-1][ny+W-1] == 0:
                visited[nx][ny] = True
                queue.append((nx,ny,top[2]+1))

        else:
          
            if S[nx+H-1][ny+W-1]-S[nx-1][ny+W-1] - S[nx+H-1][ny-1] +S[nx-1][ny-1]==0:
                visited[nx][ny] = True
                queue.append((nx,ny,top[2]+1))


if answer == float("Inf"):
    print(-1)
else:
    print(answer)

        
                    
    

