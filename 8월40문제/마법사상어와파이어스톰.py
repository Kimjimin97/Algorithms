N ,Q= map(int, input().split())

N = 2**N

dxy = [[0,1],[1,0],[0,-1],[-1,0]]

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


command = []
for _ in range(Q):
    command.append(int(input()))

def rotate(i,j,k,L,before):
    global graph
    for _ in range(L):
        i , j = i +dxy[k][0], j + dxy[k][1]
        tmp = graph[i][j]
        graph[i][j] = before
        before= tmp
    return [i,j,before]


for c in command:
    L = 2**c
    for i in range(0,N,L):
        for j in range(0,N,L):
            ## 회전
            before = graph[i][j]
            x,y,before = map(int,rotate(i,j,0,L-1,before))
            x,y,before = map(int,rotate(x,y,1,L-1,before))
            x,y,before = map(int,rotate(x,y,2,L-1,before))
            x,y,before = map(int,rotate(x,y,3,L-1,before))
    
    # for g in graph:
    #     print(g)
    # print()
       

## 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다.
    for a in range(N):
        for b in range(N):
            ice = 0
            for k in range(4):
                nx, ny = a +dxy[k][0], b +dxy[k][1]
                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue
                if graph[nx][ny] > 0:
                    ice += 1
            if ice < 3:
                if graph[a][b] - 1 >= 0:
                    graph[a][b] -= 1
    
for g in graph:
    print(g)
print()
 


sums = 0
max_num = -1
def dfs(i,j,d):
    global visited
    global max_num
    max_num = max(max_num, d)
    for k in range(4):
        nx,ny = i+dxy[k][0], j + dxy[k][1]
        if nx <0 or ny < 0 or nx >= N or ny >=N:
            continue
        if visited[nx][ny] or graph[nx][ny] == 0:
            continue
        visited[nx][ny] = True
        dfs(nx,ny,d + 1)
        visited[nx][ny] = False



for i in range(N):
    for j in range(N):
        visited = [[False]*N for _ in range(N)]
        visited[i][j] = True
        dfs(i,j,0)
        sums += graph[i][j]
  

print(sums)
print(max_num)