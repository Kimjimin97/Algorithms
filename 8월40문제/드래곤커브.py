

N = int(input())
n = 100
graph = [[False]*101 for _ in range(101)]


dxy = [(0,1),(-1,0),(0,-1),(1,0)]

rotate = {
    ## 오른쪽
    (0,1) : (-1,0),
    ## 위쪽 
    (-1,0): (0,-1),
    ## 왼쪽
    (0,-1): (1,0),
    ## 아래쪽
    (1,0) : (0,1)
}

check_rec = [[0,0],[0,1],[1,0],[1,1]]

def cal():
    answer = 0
    for i in range(n):
        for j in range(n):
            flag= True
            for k in range(4):
                nx, ny = i + check_rec[k][0], j +check_rec[k][1]
                if graph[nx][ny] == False:
                    flag = False
                    break
            if flag:
                answer += 1
    return answer


def go(r,c,dir_list,g):
    global graph
    ## 한 세대 이동
    for _ in range(g):
        new_rotate = []
        for reverse in dir_list[::-1]:
            new_rotate.append(rotate[reverse])
            r, c = r + rotate[reverse][0], c+ rotate[reverse][1]
            graph[r][c] = True
        dir_list.extend(new_rotate)
    


for _ in range(N):
    x,y,d,g = map(int, input().split())
    r = y
    c = x
    graph[r][c] = True
    r,c = r+dxy[d][0], c+dxy[d][1]
    graph[r][c] = True
    dir_list = [dxy[d]]
    go(r,c,dir_list,g)

print( cal())


