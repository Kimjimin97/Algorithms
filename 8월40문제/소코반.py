## 모든 박스를 목표점으로 이동시킨 경우에 게임은 끝난다. 게임이 끝난 후에 입력하는 키는 모두 무시된다.

print("Game", 3, ":", "incomplete")

dir_dict = {
    "U" : [-1,0],
    "L" : [0,-1],
    "R" : [0,1],
    "D" : [1,0]
}

def check(graph,goal):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == "B":
                cnt += 1
    

    if goal == cnt:
        return True
    return False 

def people_move(x,y):
    global graph
    if graph[x][y] == "W":
        graph[x][y] = "+"
    else:
        graph[x][y] = "."
    return

def box_move(nx,ny):
    global grpah
    if graph[nx][ny] == "B":
        graph[nx][ny] = "W"
    else:
        graph[nx][ny] = "w"
    return
  


def move(x,y,graph,command,goal):
    cnt = 0
    while cnt < len(command):
        dir = dir_dict[command[cnt]]
        nx, ny = x+ dir[0], y+dir[1]
        ## 벽인 경우
        if graph[nx][ny] == "#":
            cnt += 1 ########
            if check(graph,goal):
                return True
            continue
        ## 이동 좌표가 빈칸인 경우
        if graph[nx][ny] == ".":
            graph[nx][ny] = "w"
            people_move(x,y)
            x,y = nx, ny
        
        ## 이동 좌표가 목표지점인 경우
        elif graph[nx][ny] == "+":
            graph[nx][ny] = "W"
            people_move(x,y)
            x,y = nx, ny
        
        ## 이동 좌표가 박스인 경우
        else:
            bx, by = nx+dir[0], ny + dir[1]
            ## 만약 박스 이동 좌표가 벽이나 박스인 경우 이동 X
        
            if graph[bx][by] == ".":
                graph[bx][by] = "b"
                box_move(nx,ny)
                people_move(x,y)
                x,y = nx, ny

            elif graph[bx][by] == "+":  
                graph[bx][by] = "B"
                box_move(nx,ny)
                people_move(x,y)
                x,y = nx, ny

        if check(graph,goal):
            return True
        cnt+= 1

    return False
      
game = 0
while True:
    N,M = map(int, input().split())
    game += 1
    if N == 0 and M == 0:
        break
    graph = []
    goal  = 0
    for i in range(N):
        graph.append(list(map(str, input())))
        for j in range(M):
            if graph[i][j] ==  "w" or graph[i][j] == "W":
                x,y = i,j
            if graph[i][j] == "W" or graph[i][j]=='B'or graph[i][j] == "+":
                goal += 1



    command = list(map(str, input()))
 
    if move(x,y,graph,command,goal):
        print("Game %d: complete" %game)
        for g in graph:
            print("".join(g))
    else:
        print("Game %d: incomplete" %game)
        for g in graph:
            print("".join(g))

    
    
    