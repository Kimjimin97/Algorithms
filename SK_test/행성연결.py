import sys
input = sys.stdin.readline
N = int(input())
parent = [0] *(N+1)


for i in range(1, N+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        parent[b] = a 
    else:
        parent[a] = b

edges = []
total_cost = 0

graph =[]
for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(i,N):
        edges.append([graph[i][j],i+1,j+1])

edges.sort()

for i in range(len(edges)):
    cost, a,b = edges[i]
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        total_cost += cost

print(total_cost)