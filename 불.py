from collections import deque
T = int(input())
dxy = [[0,1],[1,0],[-1,0],[0,-1]]
answer = []
for _ in range(T):
    w, h = map(int, input().split())
    graph = []
    start_x = -1
    start_y = -1
    queue = deque()
    for hhh in range(h):
        ww = list(map(str, input()))
        graph.append(list(ww))
        for www in range(len(ww)):
            if ww[www] == "*":
                queue.append([hhh,www,0])
                graph[hhh][www] = 0 # 방문처리
                
            elif ww[www] == "@":
                start_x = hhh
                start_y = www

    
    while queue:
        top = queue.popleft()
        
        for k in range(4):
            nx, ny = top[0] +dxy[k][0], top[1]+dxy[k][1]
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == ".":
                    graph[nx][ny] = top[2]+1
                    queue.append([nx,ny,top[2]+1])

    
    queue = deque()
    queue.append([start_x,start_y,0])
    flag = False
    while queue:
        top = queue.popleft()
        graph[start_x][start_y] = "#" # 방문처리


        if top[0] == 0  or top[0] == h-1 or top[1] == 0 or top[1] == w-1:
            print(top[2]+1)
            flag = True
    

        for k in range(4):
            nx, ny = top[0] +dxy[k][0], top[1]+dxy[k][1]
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == "#":
                    continue

                if graph[nx][ny] == ".":
                    graph[nx][ny] = "#"
                    queue.append([nx,ny,top[2]+1])
                    continue

                if graph[nx][ny] > top[2]:
                    graph[nx][ny] = "#"
                    queue.append([nx,ny,top[2]+1])
    
    if not flag:
        print("IMPOSSIBLE")


    



    # while queue:
