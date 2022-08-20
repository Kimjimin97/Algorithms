

N, M, H = map(int, input().split())

graph = [[0]*N for _ in range(H)]
visited = [[False]*N for _ in range(H)] 

for _ in range(M):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1



## 문제에서 헷갈리는 것 행은 H 열은 N

dxy = [[1,0],[-1,0],[0,1],[0,-1]]
answer = float("INF")

## 사다리는 경로 문제가 아니다.
## 어떻게 푸는 것이 가장 효율적인가
## 2중 for문을 도는 것이 효율적인가.?
## 방문처리가 필요없을까?
## 무엇이 필요없을지 고민해보아야 한다.

def one_check(k):
    x,y = 0,k
    while True:
        if x == H-1:
            if y ==k:
                return True
            else:
                return False 
        
        if graph[x][y] == 1:
            x,y = x+1, y+1
        elif graph[x][y-1] == 1:
            x,y = x+1, y -1
        else:
            x,y = x+1, y

    return False

def check():
    for k in range(N):
        if not one_check(k):
            return False
    return True


def bridge(x,y,cnt):
    global graph 
    global visited
    global answer
    ## 다리를 놓는 것은 마지막행에서도 실행된다.
    ## 사다리 놓는 시점에 대해서 잘 알아야 한다. 
    if x == H-1: 
        if check():
            if answer > cnt:
                print(cnt)
                print(graph)
            answer = min(answer, cnt)
        return

    for k in range(4):
        ## 이동 좌표
        nx, ny = x+dxy[k][0], y+dxy[k][1]
        
        ## 범위가 넘어가면 움직이지 못한다.
        if 0 > nx or 0 > ny or H <= nx or  N-1 <= ny:
            continue
        ## 방문한 적이 있으면 이동하지 않는다
        if visited[nx][ny] == True:
            continue

        visited[nx][ny] = True
        ## 만약에 왼쪽에 사다리가 있으면
        if graph[nx][ny-1] == 1 or graph[nx][ny] == 1:
            bridge(nx,ny,cnt)
            visited[nx][ny] = False

        ## 만약에 사다리가 없다면
        else:
            graph[nx][ny] = 1
            bridge(nx,ny,cnt +1)
            visited[nx][ny] = False
            graph[nx][ny] = 0

        

bridge(0,0,0)
print(answer)