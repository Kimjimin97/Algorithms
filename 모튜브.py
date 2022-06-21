import sys
input= sys.stdin.readline
limit_number = 15000
sys.setrecursionlimit(limit_number)


N ,Q = map(int, input().split())

link = [[] for _ in range(N+1)]
graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    link[a].append(b)
    link[b].append(a)
    graph[a][b] = c
    graph[b][a] = c


def dfs(now,cost,k):
    global cnt
    for next in link[now]:
        if visited[next]:
            continue

        costs = cost
        if cost > graph[now][next]:
            costs = graph[now][next]

        if k <= costs:
            cnt += 1
        
        visited[next] = True
        dfs(next, costs, k) 
        

for _ in range(Q):
    k, V = map(int, input().split())
    visited = [False]*(N+1)
    cnt = 0
    visited[V] = True
    dfs(V,float("Inf"),k)
    print(cnt)
