from collections import deque
N,M,K = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

sx,sy = map(int, input().split())
sx,sy = sx-1, sy-1

gstart = [[-1]*N for _ in range(N)]
gend = [[-1]*N for _ in range(N)]



for k in range(M):
    cx,cy,ex,ey = map(int, input().split())
    cx,cy,ex,ey = cx-1,cy-1,ex-1,ey-1
    gstart[cx][cy] = k 
    gend[ex][ey] = k

total_visited = [False]*(M)
dxy  = [[-1,0],[0,-1],[1,0],[0,1]]
candidate = []

def start(sx,sy):
    queue = deque()
    queue.append([sx,sy,0])
    visited = [[False]*N for _ in range(N)]
    visited[sx][sy] = True
    candidate = []
    while queue:
        x,y,d = queue.popleft()
        if gstart[x][y] >= 0 and not total_visited[gstart[x][y]]:
            candidate.append((x,y,d,gstart[x][y]))

        for k in range(4):
            nx, ny = x + dxy[k][0], y+dxy[k][1]

            if 0 > nx or 0 > ny or N <= nx or  N <= ny:
                continue
            if graph[nx][ny] == 1 or visited[nx][ny]:
                continue

            visited[nx][ny] = True
            queue.append([nx,ny,d+1])
    return candidate

def end(x,y,number):
    queue = deque()
    queue.append([x,y,0])
    visited = [[False]*N for _ in range(N)]
    visited[x][y] = True

    while queue:
        x,y,d = queue.popleft()
        if gend[x][y] == number: 
            return [x,y,d]

        for k in range(4):
            nx, ny = x + dxy[k][0], y+dxy[k][1]
            if 0 > nx or 0 > ny or N <= nx or  N <= ny:
                continue
            if graph[nx][ny] == 1 or visited[nx][ny] :
                continue

            visited[nx][ny] = True
            queue.append([nx,ny,d+1])
    return [-1,-1,-1]


fuel = K
flag = True
for _ in range(M):
  
    candidate = start(sx,sy)
    if not candidate:
        print(-1)
        flag= False
        break
    # print(candidate)
    candidate.sort(key = lambda x : (x[2],x[1],x[0]))
    x,y,d,number = candidate[0][0], candidate[0][1], candidate[0][2], candidate[0][3]

    total_visited[number] = True
    # print("numver",number)
    K -= d
    # print("r",x,y,d,K)
    if K <= 0  or  x+y+number+d < 0:
        # print("a")
        print(-1)
        flag = False
        break
    sx,sy,d = map(int, end(x,y,number))
    # print("s",sx,sy,d)
    K -= d
    if K < 0 or sx+sy+d < 0:
        print(-1)
        flag= False
        break
    K += 2*d

if flag:
    # print(flag)
    print(K)
