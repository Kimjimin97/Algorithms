N, M = map(int, input().split())

graph = []

cctv = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(M):
        ## cctv인 경우
        if graph[i][j] != 0 and graph[i][j] !=6:
            cctv.append([graph[i][j],i,j])

## cctv 방향 설정
cctv_rotate = {
    1 : [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
    2: [[1,0,1,0], [0,1,0,1]],
    3: [[1,1,0,0], [0,1,1,0],[0,0,1,1],[1,0,0,1]],
    4: [[1,1,1,0], [0,1,1,1],[1,0,1,1],[1,1,0,1]], ## 4번 방향 설정이 헷갈린다.
    5: [[1,1,1,1]],
}


## 사각지대 구하기
def cal(graph):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    return cnt 


answer = cal(graph)

dxy = [[-1,0],[0,1],[1,0],[0,-1]]

## 경우의 수 탐지
def dfs(L):
    global answer
    global graph

    if L == len(cctv):

        answer = min(answer, cal(graph))
        return
    
    now_dir = cctv[L][0] ## 현재 방향 
    ## 현재 방향에 대한 탐색을 위한 for 문
    x,y = cctv[L][1], cctv[L][2]
    for d in cctv_rotate[now_dir]:
        visited = []
        for k in range(4):
            if d[k] == 1 :
                ## 한 방향으로 이동이 가능한 경우
                nx, ny = x, y
                while True:
                    nx, ny = nx+dxy[k][0], ny+ dxy[k][1]
                    ## 범위를 넘어가거나 벽인 경우는 더 이상 진행하면 안된다
                    if 0 > nx or 0 > ny or N <= nx or M <= ny or graph[nx][ny] == 6:
                        break
                    
                    ## 감시 되는 위치
                    if graph[nx][ny] == 0:
                        visited.append([nx,ny])
                        graph[nx][ny] = "#"
        
        dfs(L+1)

        for mx, my in visited:
            graph[mx][my] = 0

dfs(0)
print(answer)

                    
            
        
    
    
    
    
