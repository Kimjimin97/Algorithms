import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)
input = sys.stdin.readline
N,M = map(int, input().split())

visit = [False] * (N+1)
graph = [[] for _ in range(N+1)]

for i in range(M):
    a,b= map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)



dis = [float("Inf")]*(N+1)


res = float("-Inf")
def dfs(v,d):
    global res

    res = max(res, d)
    for n in graph[v]:
        dfs(n, d+1)



dfs(1, 0)
print(d)