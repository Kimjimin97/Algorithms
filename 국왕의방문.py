import heapq

N,M = map(int, input().split())
A, B, K, G = map(int, input().split())

went_go = list(map(int, input().split()))

graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b,c =map(int, input.split())
    graph[a][b] = c
    graph[b][a] = c

went_go_graph = [[0]*(N+1) for _ in range(N+1)]
