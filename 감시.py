N, M = map(int, input().split())

graph = []
cctv = []

for i in range(N):
    lists = list(map(int, input().split()))
    graph.append(lists)
    for j in range(len(lists)):
        if graph[i][j] != 0 and graph[i][j] !=6 :
            cctv.append((i,j))


dxy = [[0,1],[1,0],[0,-1],[-1,0]]

move = dict()
move[1] = [[0],[1],[2],[3]]
move[2] = [[0,2],[1,3]]
move[3] = [[0,1],[1,2],[2,3],[0,3]]
move[4] = [[0,1,2],[1,2,3],[2,3,0],[3,0,1]]
move[5] = [[0,1,2,3]]

print(cctv)
print(move)

print(move[1])
print(move[2])

for d in move[2]:
    for dd in d:
        print(dd)

# res = float("Inf")

# def dfs(L,x,y,n):
#     global res
#     if L == len(cctv):
#         res = min(res, n)
#         return
    
#     if n >= res:
#         return
    
#     print(move[graph[x][y]])
#     for dir in move[graph[x][y]]:
#         visited = []
#         mx, my = x, y
#         for dd in dir:

#             for d in range(len(dd)):
#                 while True:
#                     nx, ny = mx+dxy[dd[d]][0], my +dxy[dd[d]][0]
#                     if  0 > nx or 0> ny or nx >= N or ny >=M:
#                         break
#                     if graph[nx][ny] != 0:
#                         break

#                     n += 1
#                     graph[nx][ny] = "#"
#                     visited.append([nx,ny])
#         dfs(L+1,cctv[L+1][0], cctv[L+1][1],n)

#         for a,b in visited:
#             graph[a][b] = "0"


# dfs(0,cctv[0][0],cctv[0][1],0)
# print(res)
