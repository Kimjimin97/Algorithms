from collections import deque

N,M,V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(len(graph)):
    graph[i].sort()


## 방문처리
visited = [False]*(N+1)
path = []

def dfs(v):
    global visited
    global path

    path.append(v)

    for g in graph[v]:
        if not visited[g]:
            visited[g] = True
            dfs(g)
    
    return

def bfs():
    queue = deque()
    queue.append(V)
    visited = [False]*(N+1)
    visited[V] = True
    while queue:
        v = queue.popleft()
        path.append(v)
        for g in graph[v]:
            if not visited[g]:
                visited[g] = True
                queue.append(g)

    return

visited[V] = True
dfs(V)
print(*path)
path =[]
bfs()
print(*path)