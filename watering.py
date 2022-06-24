from pickle import FALSE
import sys
import heapq
input = sys.stdin.readline
N, C = map(int, input().split())


nodes = []
node = []
for _ in range(N):
    a,b = map(int, input().split())
    node.append([a,b])



for i in range(len(node)):
    a,b = node[i][0], node[i][1]
    for j in range(i+1,len(node)):
        x,y = node[j][0], node[j][1]
        dis = (a-x)**2 + (b-y)**2

        if dis >= C:
            heapq.heappush(nodes,[dis, i,j])


def find(kk):
    if parent[kk] != kk:
        parent[kk] = find(parent[kk])
    return parent[kk]

def union(aa,bb):
    root1 = find(aa)
    root2 = find(bb)
    if root1 == root2:
        return False
    else:
        parent[root2] = root1



parent = [i for i in range(N)]
edge = 0

cost = 0
while nodes:
    top = heapq.heappop(nodes)

    c,aa,bb = top[0], top[1], top[2]
    if union(aa,bb):
        cost += c
        edge+= 1
        if edge == N-1:
            break

if edge == N-1:
    print(cost)
else:
    print(-1)