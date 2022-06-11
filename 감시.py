N, M = map(int, input().split())

graph = []
cctv = []

for i in range(N):
    lists = list(map(int, input().split()))
    graph.append(lists)
    for j in range(len(lists)):
        if graph[i][j] != 0 and graph[i][j] !=6 :
            cctv.append((i,j))



move = dict()
move[1] = [(0),(1),(2),(3)]
move[2] = 