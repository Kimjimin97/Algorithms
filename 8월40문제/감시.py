import sys
input = sys.stdin.readline
N, M = map(int, input().split())


cctv = []
graph =[]
for i in range(N):
    lists = list(map(int, input().split()))
    graph.append(lists)
    for j in range(M):
        if graph[i][j] != 0 and graph[i][j] !=6:
            cctv.append([graph[i][j],i,j])


dxy = [[-1,0],[0,1],[1,0],[0,-1]]

cctv_rotate = [[],
[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
[[1,0,1,0],[0,1,0,1]],
[[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]],
[[1,1,1,0],[0,1,1,1],[1,0,1,1],[1,1,0,1]],
[[1,1,1,1]]
]


def calculate(graph):
    nanswer = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                nanswer += 1
    return nanswer


answer = calculate(graph)

def dfs(L):
    global graph
    global answer
    
    
    if L == len(cctv):
        answer = min(answer, calculate(graph))

        return
    
    now_cctv = cctv[L][0]
    
    for move_dir_ind in range(len(cctv_rotate[now_cctv])): ## 방향의 가짓수 [[1,1,1,0],[0,1,1,1],[1,0,1,1]],
        visited = []
        for k in range(4): ## 한 경우의 수 중 한 방향 감시
            if cctv_rotate[now_cctv][move_dir_ind][k] == 0:
                continue
            nx, ny = cctv[L][1],cctv[L][2] ## 시작 장소 찾기
            while True:
                nx += dxy[k][0]
                ny += dxy[k][1]

                if 0 > nx or 0 > ny or N <= nx or M <= ny:
                    break

                elif graph[nx][ny] ==6:
                    break

                elif graph[nx][ny] == 0:
                    graph[nx][ny] = "#"
                    visited.append([nx,ny])

                
        

        dfs(L+1)
        for dx,dy in visited:
            graph[dx][dy] = 0

dfs(0)
print(answer)