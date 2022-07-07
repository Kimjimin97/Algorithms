"""
N*M인 게이판 위에서 진행
칠해진 공이 하나씩 있다. 
같은 색으로 이루어진 사이클 찾기
사이클이 존재하는 경우에 "yes" 없는 경우 "No" 출력

- 아이디어
모든 점에 대해서 사이클이 존재하는지 확인
자기 자신으로 돌아올 수 있는가 없는가 확인

2 ≤ N, M ≤ 50

dfs
N*N*O(V+E) = 4*50*50*O(50*50 + 4*50*50) = 6250000


- 로직
모든 점에 대해서 dfs 시작하기
만약 인접 노드에 자기 자신이 있으면  answer 값 증가하기
아니면 탐색하기

사이클의 조건
첫 이동 이후 노드에서 인접노드에 자기 자신이 있으면 사이클이 발생
"""

from ast import Continue


N,M = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(str, input())))

visited = [[False]*M for _ in range(N)]

dxy = [[1,0],[-1,0],[0,1],[0,-1]]

def dfs(sx,sy,x,y,n):

    if n > 1: 
        for kk in range(4):
            cx, cy = x+dxy[kk][0], y+dxy[kk][1]
            if cx <0 or cy <0 or cx >=N or cy >= M:
                continue 
            if cx == sx and cy== sy:
                print("Yes")
                exit(0)


    for k in range(4):
        nx, ny = x+dxy[k][0], y+dxy[k][1]
        if nx <0 or ny <0 or nx >=N or ny >= M:
            continue 

        if visited[nx][ny]:
            continue 

        if graph[sx][sy] != graph[nx][ny]:
            continue
        visited[nx][ny] = True
        dfs(sx,sy, nx,ny, n+1)
        visited[nx][ny] = False

for i in range(N):
    for j in range(M):
        visited = [[False]*M for _ in range(N)]
        visited[i][j] = True
        dfs(i,j,i,j,0)

print("No")