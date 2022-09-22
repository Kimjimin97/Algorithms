import tempfile


N,M,x,y,K = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

command = list(map(int, input().split()))


dxy = {
    1: (0,1),
    2: (0,-1),
    3: (-1,0),
    4: (1,0)
}

box = [[0]*3 for _ in range(4)]

box_rotate = {
    1: [[1,0],[1,1],[1,2],[3,1],[1,0]],
    2: [[1,2],[1,1],[1,0],[3,1],[1,2]],
    3: [[3,1],[2,1],[1,1],[0,1],[3,1]],
    4: [[0,1],[1,1],[2,1],[3,1],[0,1]]
}

def change_box(k):
    global box
    before = box[box_rotate[k][0][0]][box_rotate[k][0][1]]
    for r in range(1,5):
        tmp = box[box_rotate[k][r][0]][box_rotate[k][r][1]]
        box[box_rotate[k][r][0]][box_rotate[k][r][1]] = before
        before = tmp 


    

for k in command:
    nx, ny = x+dxy[k][0], y+dxy[k][1]
    if nx < 0 or ny < 0 or nx >= N or ny >= M:
        continue
    x , y = nx, ny
    change_box(k)
    if graph[x][y] == 0:
        graph[x][y] = box[3][1]
    else:
        box[3][1] = graph[x][y]
        graph[x][y] = 0
    
    print(box[1][1])
    