

from ast import Continue


N, M = map(int, input().split())

graph = []
cctv = []
wall = 0

for i in range(N):
    lists = list(map(int, input().split()))
    graph.append(lists)
    for j in range(len(lists)):
        if graph[i][j] != 0 and graph[i][j] !=6 :
            cctv.append((i,j))
        if graph[i][j] == 6:
            wall += 1


dxy = [[0,1],[-1,0],[0,-1],[1,0]]

move = dict()
move[1] = [[0],[1],[2],[3]]
move[2] = [[0,2],[1,3]]
move[3] = [[0,1],[1,2],[2,3],[3,0]]
move[4] = [[0,1,2],[1,2,3],[2,3,0],[3,0,1]]
move[5] = [[0,1,2,3]]

res = float("-Inf")


def dfs(L, n):
    global res
    if L == len(cctv):
        res = max(res, n)
        return

    x, y = cctv[L][0], cctv[L][1]

    for dir in move[graph[x][y]]: # [(0,1,2),(1,2,3),(2,3,0),(3,0,1)]
        visited = []
        
        for dd in dir: # dd = (0,1,2)
            nx, ny = x, y
            while True:
                nx, ny = nx+dxy[dd][0], ny +dxy[dd][1]
                if  0 > nx or 0> ny or nx >= N or ny >=M:
                    break
                if graph[nx][ny] == 6:
                    break
                
                if graph[nx][ny] == "#" or graph[nx][ny] != 0:
                    continue

                visited.append([nx,ny])
                graph[nx][ny] = "#"
                

        dfs(L+1,n + len(visited)) 

        for a,b in visited:
            graph[a][b] = 0


dfs(0,0)
print(N*M - len(cctv)- res-wall)
