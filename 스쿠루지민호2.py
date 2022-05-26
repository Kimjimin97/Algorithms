from collections import deque

N = int(input())

graph=[[] for _ in range(N+1)]

for i in range(N-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visit = [False]*(N+1)
police = [False]*(N+1)


def dfs(v,police):

    

    for n in graph[v]:
        if not visit[n]:
            visit[n] = True
            # police세워주기

            dfs(n,police)
            visit[n] = False