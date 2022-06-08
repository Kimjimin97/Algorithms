import sys
import heapq
input = sys.stdin.readline
N, M = map(int, input().split())
A,B,k,g = map(int, input().split())

go_go = list(map(int, input().split()))

graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

limit_time = [[0]*(N+1) for _ in range(N+1)]

go = go_go[0]
take_time = 0
for i in range(1, len(go_go)):
    froms = go_go[i]
    
    limit_time[froms][go] = (take_time,take_time + graph[go][froms])
    limit_time[go][froms]  = (take_time,take_time + graph[go][froms])
    take_time += graph[go][froms]
    go = froms

heap = []

heapq.heappush(heap,(k,A))
visited = [False]*(N+1)
memo = [float("Inf")]*(N+1)
memo[A] = 0
visited[A] = True
while heap:
    top = heapq.heappop(heap)
    visited[top[1]] = True
    for link in range(1,N+1):
        if graph[top[1]][link] != 0:
            if not visited[link]:
                if limit_time[top[1]][link] == 0:
                    finish_time =  top[0]+graph[top[1]][link]
                    
                else:
                    a,b = limit_time[top[1]][link]
                    if a <= top[0]< b:
                        finish_time = b+graph[top[1]][link]
    
                    else:
                        finish_time =  top[0]+graph[top[1]][link]
                    
            if memo[link] > finish_time:
                memo[link] = finish_time
                heapq.heappush(heap, (memo[link], link))
                    

print(memo[B]-k)
