from collections import deque
import copy
R,C = map(int, input().split())

graph = []

person = deque()
rain = deque()

rain_graph = [[float("Inf")]*C for _ in range(R)]
rain_visited = [[False]*C for _ in range(R)]

for i in range(R):
    lists = list(input())
    graph.append(lists)
    for j in range(C):
        if lists[j] ==  "S":
            person.append([i,j,0])

        if lists[j] == "D":
            end_x = i
            end_y = j

        if lists[j] == "*":
            rain.append([i,j,0])
            rain_visited[i][j] = True

        
 

dxy = [[0,1],[1,0],[-1,0],[0,-1]]

def make_rain():
  
    while rain:
        x,y,t = rain.popleft()
        for k in range(4):
            nx, ny, nt  = x+dxy[k][0], y+dxy[k][1], t+1
            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue 
            if rain_visited[nx][ny]:
                continue

            if graph[nx][ny] == ".":
                rain_visited[nx][ny] =True
                rain_graph[nx][ny] = nt   
                rain.append([nx,ny,nt])        



def go():
    flag= False
    while person:
        x,y,t= person.popleft()
        for k in range(4):
            nx, ny, nt  = x+dxy[k][0], y+dxy[k][1], t+1
            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue 

            if nx==end_x and ny == end_y:
                flag =True
                print(nt)
                break

            if (graph[nx][ny] == ".") and (rain_graph[nx][ny] > nt):
                    graph[nx][ny] = nt   
                    person.append([nx,ny,nt]) 
        if flag:
            break 

    if not flag:
        print("KAKTUS")
            
            
if len(rain) != 0:
    make_rain()

go()
