
from collections import deque
N, M = map(int, input().split())



def make_bin(a):
    tens = str(bin(a))
    tens = tens[2:]

    if len(tens) < 4:
        tens = "0"*(4-len(tens)) + tens
    return tens

graph = []
bin_graph = []

for i in range(M):
    lists =list(map(int, input().split()))
    bin_lists =[]
    graph.append(lists)
    for j in range(N):
        bin_lists.append(make_bin(graph[i][j]))
    bin_graph.append(bin_lists)


dxy = [[1,0],[0,1],[-1,0],[0,-1]]
room = [[-1]*(N) for _ in range(M)]
sizes = []

def bfs(i,j,n):
    global room
    queue = deque()
    queue.append([i,j])
    room[i][j] = n
    size = 1
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx,ny = x+dxy[k][0], y+dxy[k][1]
            if nx <0 or ny <0 or nx >=M or ny >= N:
                continue

            if bin_graph[x][y][k] == "1":
                continue 
            
            if room[nx][ny] == -1:
                room[nx][ny] = n
                size += 1
                queue.append([nx,ny])
    sizes.append(size)


def make_room():
    n=0
    for i in range(M):
        for j in range(N):
            if room[i][j] == -1:
                bfs(i,j,n)
                n+=1


make_room()

max_size = sizes[0]
room_visited =[[False]*N for _ in range(M)]

def link_room():
    global max_size
    n=0
    for i in range(M):
        for j in range(N):
            for k in range(4):
                nx,ny = i+dxy[k][0], j+dxy[k][1]
                if nx <0 or ny <0 or nx >=M or ny >= N:
                    continue
                if room[i][j] != room[nx][ny]:
                    max_size = max(max_size, sizes[room[i][j]]+sizes[room[nx][ny]])
link_room()
print(len(sizes))
print(max(sizes))
print(max_size)
