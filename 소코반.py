from ast import Continue
import copy

dxy = dict()
dxy["U"] = [-1,0]
dxy["D"] = [1,0]
dxy["L"] = [0,-1]
dxy["R"] = [0,1]

def is_complete(a):
    goal = 0
    box = 0
    for row in a:
        for ch in row:
            if ch == "+":
                goal+= 1
            if ch =="b":
                box += 1
    return goal == 0 and box == 0

def solution(R, C,round):
    graph = []
    goal = []
    box_cnt = 0
    flag = False
    for  i in range(R):
        lists = list(map(str, input()))
        graph.append(lists)
        for j in range(len(lists)):
            if graph[i][j] == "w" or graph[i][j] == "W":
                x = i
                y = j

            if graph[i][j] == "W" or graph[i][j] == "B" or graph[i][j] == "+":
                goal.append([i,j])

    
            if graph[i][j] == "b" or graph[i][j] == "B":
                box_cnt += 1
            
            
    move_lists = list(map(str, input()))



    for k in move_lists:
        # print(k,x,y)
        # for g in graph:
        #     print("".join(g))   
        # print()

        # goal_cnt = 0
        # for gx, gy in goal:
        #     if graph[gx][gy] == "B":
        #         goal_cnt += 1

        # if goal_cnt == box_cnt:
        #     flag= True
        #     print("Game %d: complete" %(round))
        #     for g in graph:
        #         print("".join(g))
        #     break

    
        nx, ny = x + dxy[k][0], y+dxy[k][1]
        bx, by = nx +dxy[k][0], ny+dxy[k][1]

        if graph[nx][ny] == "#":
            continue
        elif graph[nx][ny] in "bB":
            if graph[bx][by] in "bB#":
                continue
       
        if graph[x][y] == "W":
            graph[x][y] = "+"
        
        elif graph[x][y] =="w":
            graph[x][y] = "."

        if graph[nx][ny] == ".": # 빈공간이면 이동
            graph[nx][ny] = "w"
            x,y = nx, ny
        
        elif graph[nx][ny] == "+":
            graph[nx][ny] = "W"
            x,y = nx, ny
        
        
        elif graph[nx][ny] == "B":
            graph[nx][ny] = "W" # 원래 자리 바꿔주기
            if graph[bx][by] == ".":
                graph[bx][by] = "b"
            elif graph[bx][by] == "+":
                graph[bx][by] = "B"
            x,y = nx, ny
        
        elif graph[nx][ny] == "b":
            graph[nx][ny] = "w" # 원래 자리 바꿔주기
            if graph[bx][by] == ".":
                graph[bx][by] = "b"
            elif graph[bx][by] == "+":
                graph[bx][by] = "B"
            x,y = nx, ny
        
        if is_complete(graph):
            break
    
    print('Game %d: %s' % (round, 'complete' if is_complete(graph) else 'incomplete'))
    for row in graph:
        print(''.join(row))

        



round = 0
while True:
    a,b  = map(int, input().split())
    round += 1
    if a == 0 and b == 0:
        break
    else:
        solution(a,b, round)
    

