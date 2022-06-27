from ast import Continue
from collections import deque
from operator import truediv
N, K, R = map(int, input().split())

graph = [[-1]*N for _ in range(N)]

road = dict()
for _ in range(R):
    a,b,c,d = map(int, input().split())
    a-=1
    b-=1
    c-=1
    d-=1

    if (a,b) in road.keys():
        road[(a,b)].append([c,d])
    else:
        road[(a,b)] = [[c,d]]
    
    if (c,d) in road.keys():
        road[(c,d)].append([a,b])
    else:
        road[(c,d)] = [[a,b]]

cow_loca = [[] for _ in range(K)]

for k in range(K):
    x,y= map(int, input().split())
    graph[x-1][y-1] = k
    cow_loca[k].append([x-1,y-1])


dxy = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(x,y):
    queue =deque()
    visited[x][y] = True 
    queue.append([x,y])
    while queue:
        x, y = queue.popleft()
        if graph[x][y] != -1:
            cow_list[graph[x][y]] = True

        for k  in range(4):
            nx, ny = x+dxy[k][0], y +dxy[k][1]
            if nx < 0 or nx >=N or ny < 0 or ny>=N:
                continue 
            if visited[nx][ny]:
                continue

            if (x,y) in road.keys() and [nx,ny] in road[(x,y)]:
                continue 
            visited[nx][ny] = True
            queue.append([nx,ny])

answer = 0
for c in range(K):
    cow_list = [False] * K
    visited = [[False] *N for _ in range(N)]
    bfs(cow_loca[c][0][0],cow_loca[c][0][1])
    for j in range(c+1,K):
        if not cow_list[j]:
            answer += 1

print(answer)
    