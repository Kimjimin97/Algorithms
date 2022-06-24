from ast import Continue


N, K =map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


now = dict()
dxy = [[],[0,1],[0,-1],[-1,0],[1,0]]
char_dir = [0]*(K)
rotate = {1:2, 2:1, 3:4, 4:3}



for i in range(K):
    a,b,d = map(int, input().split())
    now[i] = [a-1,b-1,1]
    char_dir[i] = d


cnt = 0
flag= False
while cnt <= 1000:
    cnt += 1
    for char in range(K):
        if now[char][2] != 1:
            continue 
        blue_flag = False
        print(now)
        x, y = now[char][0], now[char][1]
        nx, ny = x+dxy[char_dir[char]][0], y+dxy[char_dir[char]][1]
        print(char, char_dir)
        print(x,y,nx,ny)

        together = []
        move = []
        top = 0

        if nx < 0 or nx >= N or ny < 0 or ny >= N or graph[nx][ny] ==2:
            char_dir[char] = rotate[char_dir[char]]
            nx, ny = x+dxy[char_dir[char]][0], y+dxy[char_dir[char]][1]
            blue_flag=True
            if nx < 0 or nx >= N or ny < 0 or ny >= N  or graph[nx][ny] == 2:
                continue
            # else:
            #     now[char][0], now[char][1] = nx, ny
            #     continue
    
            


        for check in range(K):
            if check == char:
                continue 

            if now[check][0] == nx and now[check][1] == ny and check != char:
                top = max(now[check][2],top)
        
        for to in range(K):
            if now[to][0] == x and now[to][1] == y :
                together.append([now[to][2],to])
        
        together.sort()
        if graph[nx][ny] == 0:## 흰색
            for tt in together:
                top += 1
                t = tt[1]
                now[t][0], now[t][1], now[t][2] = nx, ny, top
            if top >= 4:
                flag = True
                break
            
        
        elif graph[nx][ny] == 1: ## 빨간색
            together = together[::-1]
            for tt in together:
                top += 1
                t = tt[1]
                now[t][0], now[t][1], now[t][2] = nx, ny, top
            if top >= 4:
                flag = True
                break
    if flag:
        break


if cnt >1000:
    print(-1)

else:
    print(cnt)
        



