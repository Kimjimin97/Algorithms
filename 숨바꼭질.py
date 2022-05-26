from collections import deque
N,M = map(int, input().split())

visit = [False] * (N+1)
graph = [[] for _ in range(N+1)]

for i in range(M):
    a,b= map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

queue = deque()

dis = [float("Inf")]*(N+1)
visit[1] = True
queue.append((1,0))

res = float("-Inf")
answer = [0]*3

while queue:
    top = queue.popleft()
    if res < top[1]:
        res = top[1]
        answer[0] = top[0]
        answer[1] = top[1]
        answer[2] = 1
    elif res ==top[1]:
        answer[0] = min(answer[0], top[0])
        answer[2] += 1 
    
        
    
    

    for v in graph[top[0]]:
        if not visit[v]:
            visit[v] = True
            queue.append((v,top[1]+1))

print(*answer)
    

# def dfs(v,d):

#     for n in graph[v]:
#         if not visit[n]:
#             visit[n] = True
#             dfs(n, d+1)
#             visit[n] = False

#     dis[v] = min(d, dis[v])

# visit[1] = True
# dfs(1, 0)
# # print(dis)

# cnt = 0
# res = float("-Inf")
# first = -1
# for i in range(1,len(dis)):
#     if res < dis[i]:
#         res = dis[i]
#         cnt = 1
#         first = i
#     elif res == dis[i]:
#         cnt += 1
# print(first, res, cnt)
        
