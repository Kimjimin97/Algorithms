
graph = []
loca = [[-1,-1] for _ in range(17)]

for i in range(4):
    lists = list(map(int, input().split()))
    lists1 = []
    for j in range(0,8,2):
        shark_num,shark_dir = lists[j], lists[j+1]
        loca[shark_num] = [i,j//2]
        lists1.append([shark_num,shark_dir-1])
    graph.append(lists1)



dxy = [[1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]

def move_fish(graph, location):
    
    for i in range(1,17):
        x,y = map(int, location[i])
        k = graph[x][y][1]

        if x == -1 and y == -1:
            continue

        for kk in range(8):

            nk = (k + kk) % 8
            nx, ny = x + dxy[nk][0], y + dxy[nk][1]

            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4 or graph[nx][ny] == [-1,-1]:
                continue


            ## 자리를 움직일 때는 상어가 있는지 체크하지 않는다.
            # if graph[nx][ny] == [0,0]:
            #     graph[nx][ny] = [i,k]
            #     location[i] = [nx,ny]
            #     break
            
            elif graph[nx][ny][0] >= 0:
                next, next_dir = map(int,graph[nx][ny])
                graph[nx][ny] = [i,k]
                graph[x][y] = [next, next_dir]
                location[next] = [x,y]
                location[i] = [nx,ny]
                break
        
        return graph, location


    

    
answer = float("-INF")
def dfs(graphs, loca, x, y, fish):
    global answer
    fish += graphs[x][y][0]
    answer = max(answer,fish)
    loca[graph[x][y][0]] = [-1,-1]
    k = graphs[x][y][1]
    graphs[x][y] = [-1,graphs[x][y][1]]
    

    new_graph = [[[graphs[i][j][0],graphs[i][j][1]] for j in range(4)] for i in range(4)]
    new_loca = [[loca[i][0], loca[i][1]] for i in range(17)]
    new_graph, new_loca = move_fish(new_graph, new_loca)

    print("물고기 이동")
    for gi in new_graph:
        print(gi)
    print()

    nx, ny = x, y 
    while True:
        nx, ny = nx + dxy[k][0], ny + dxy[k][1]
        if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
            return


        
        if new_graph[nx][ny][0] > 0:
            dfs(new_graph, new_loca, nx, ny, fish )



            
            

fish, dir = map(int, graph[0][0])
graph[0][0] = [-1,dir]
loca[fish] = [-1,-1]

print("g",graph)
print(dir)
dfs(graph, loca,0,0, fish)
print(answer)