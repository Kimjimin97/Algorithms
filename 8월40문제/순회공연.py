import heapq
n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


graphs = sorted(graph, key=lambda x:x[1])


now = []

for g in graphs:
    heapq.heappush(now, g[0])
    if (len(now) > g[1]):
        heapq.heappop(now)

print(sum(now))



