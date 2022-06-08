'''
시간복잡도 (4*4*3*4)
'''

k = int(input())
a,b = map(int, input().split())
N = 2**k
graph = [[0]*(2**k) for _ in range(2**k)]

num = 1

graph[N-b][a-1] = -1

print(graph)

check_list = [[0,0],[0,2],[2,0],[2,2],[1,1]]
dxy = [[0,1],[0,-1],[1,0],[-1,0]]


check = [False]*5


item = [[[num,num],[num,0]], [[num,num],[0, num]], [[num,0],[num,num]],[[0,num],[num,num]]]

for c in range(5):
    x,y = check_list[c][0], check_list[c][1]
    for k in range(4):
        nx, ny = x+dxy[k][0], y+dxy[k][1]
        if graph[nx][ny] == -1:
            check[c] = True
            

    