import sys
input = sys.stdin.readline


R,C,T = map(int, input().split())

graph = []
dxy = [[0,1],[1,0],[0,-1],[-1,0]]

def check_go(nx,ny):
    if nx < 0 or ny <0 or nx >=R or ny >=C:
        return False 
    return True

def check_air(nx,ny):
    if graph[nx][ny] == -1:
        return False
    return True


air = []
for i in range(R):
    graph.append(list(map(int, input().split())))
    for j in range(C):
        if graph[i][j] == -1:
            air.append([i,j])

def right(x,y,tmp):
    global graph
    for j in range(y+1,y+C):
        y= j
        prev_val = graph[x][y]
        graph[x][y] = tmp
        tmp = prev_val
    return x,y,tmp

def up(x,y,tmp,sx):
    for i in range(x-1,x-1-sx,-1):
        x = i 
        if graph[x][y] == -1:
            return x, y,tmp
        prev_val = graph[x][y]
        graph[x][y] = tmp
        tmp = prev_val
    return x,y,tmp

def left(x,y,tmp):
    for j in range(y-1,-1,-1):
        y = j 
        prev_val = graph[x][y]
        graph[x][y] = tmp
        tmp = prev_val
    return x,y,tmp

def down(x,y,tmp,n):
    for i in range(x+1,x+1+n):
        x = i 
        if graph[x][y] == -1:
            return x, y,tmp
        prev_val = graph[x][y]
        graph[x][y] = tmp
        tmp = prev_val
    return x,y,tmp         


def air_clean(graph):

    sx,sy =air[0][0], air[0][1]
    tmp = 0
    ## 오른쪽 회전
    
    x,y,tmp = right(sx,sy,tmp)

    ## 위쪽 회전
    x,y,tmp = up(x,y,tmp,sx)
    ## 왼쪽 회전
    x,y,tmp = left(x,y,tmp)
    ## 아래쪽 회전
    x,y,tmp = down(x,y,tmp,sx)

    
    ###########
    sx,sy =air[1][0], air[1][1]
    tmp = 0
    ## 오른쪽 회전
    x,y,tmp = right(sx,sy,tmp)
    ## 아래 회전
    x,y,tmp = down(x,y,tmp,R-sx-1) ## R-sx-1 7-3-1 =3
    ## 왼쪽 회전
    x,y,tmp = left(x,y,tmp)
    ## 위쪽 회전
    x,y,tmp = up(x,y,tmp,R-sx-1)

    return

def sum_graph (graph,new_graph):
    for i in range(R):
        for j in range(C):
            graph[i][j] += new_graph[i][j]
    return graph   

t = 0
while t <T:
    new_graph = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j] != 0 and graph[i][j] != -1:
                cnt = 0
                for k in range(4):
                    nx, ny = i+dxy[k][0], j+dxy[k][1]
                    if check_go(nx,ny) and check_air(nx,ny):
                        cnt += 1
                        new_graph[nx][ny] += graph[i][j]//5
                graph[i][j] -= (graph[i][j]//5)*cnt 
        
    
    graph = sum_graph(graph, new_graph)
    air_clean(graph)
    t+=1    

answer = 0
for g in graph:
    answer += sum(g)
print(answer+2)



