
import sys
import heapq
input= sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range((n+1))]
costs = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append(b)
    costs[a][b] = c
    

start, end = map(int, input().split())

answer = float("Inf")
visited = [False]*(n+1)
memo = [float("Inf")]*(n+1)


queue = []
heapq.heappush(queue, [0,start])
memo[start] =0

while queue:
    queue.sort()
    top = heapq.heappop(queue)
    
    if visited[top[1]]:
        continue

    for k in graph[top[1]]:
        memo[k] = min(memo[k],memo[top[1]]+costs[top[1]][k])
        heapq.heappush(queue,[memo[k],k])
        visited[top[1]] = True

print(memo[end])