


from pickle import FALSE


N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

cost = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append(b)
    cost[a][b] = c

def dfs(v, time):
    memo[v] = min(memo[v], time)

    for k in graph[v]:
        if visited[k]:
            continue 
        visited[k] = True 
        dfs(k,time+cost[v][k])
        visited[k] = False


memo = [float("Inf")]*(N+1)
visited = [False]*(N+1)
visited[1] = True
dfs(1,0)

flag = True
for i in range(2,N+1):
    if memo[i] <= 0:
        flag= False
        print(-1)
        break

if flag:
    for i in range(2, N+1):
        if memo[i] != float("Inf"):
            print(memo[i])
        else:
            print(-1)