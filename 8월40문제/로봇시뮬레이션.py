"""
L:  왼쪽 90
R: 오른쪽 90
F : 앞으로
"""

from urllib import robotparser


A,B = map(int, input().split())
N,M = map(int, input().split())

graph = [[-1]*A for _ in range(B)]

## 위, 오른쪽, 아래, 왼쪽
dxy =[[-1,0],[0,-1],[1,0],[0,1]]

command = []
location = dict()
for i in range(N):
    a,b,c = map(str, input().split())
    a = int(a)-1
    b = B- int(b)
    if c == "E":
        c = 1
    elif c == "N":
        c = 0
    elif c == "S":
        c = 2
    elif c == "W":
        c =3
    graph[b][a] = c
    location[i+1] = [b,a,c]



for _ in range(M):
    a,b,c = map(str, input().split())
    command.append([int(a),b,int(c)])



def command_func(robot, c):
    global location
    print(c)
    nx,ny,k = map(int, location[robot])
    if c == "F":

        for n in range(c):
            nx, ny = nx + dxy[k][0], ny + dxy[k][1]
        
            if 0 < nx or  0 < ny or nx >= N or ny >= N:
                print('Robot {} crashes into the wall'.format(graph[x][y]))
                return True
            if graph[nx][ny] != -1:
                print('Robot {} crashes into robot {}'.format(graph[x][y],graph[nx][ny]))
                return True
        
        graph[nx][ny] = robot
        location[robot] = [nx,ny]

        

    if c ==  "L":
        k = (k + (1*c))%4
        location[robot][1] = k

    if c ==  "R":
        k = (k+(3*c))%4
        location[robot][1] = k
    
    return False

flag = False

for c in command:
    if command_func(c[0],c[-1]):
        flag = True
        break

if not flag:
    print("OK")