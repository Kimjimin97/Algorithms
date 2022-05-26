from collections import deque
N = int(input())

people = []
sum_people = 0
for _ in range(N):
    people_li =list(map(int, input().split()))
    people.append(people_li)
    sum_people += sum(people_li)


dxy = [[1,0],[0,1],[-1,0],[0,-1]]


def bfs(x,y,n):
    # 0 이면 인원수를 더 준다
    # n 이면 인덱스에 더해준다
    # n 이 아니면 return
    queue = deque()
    queue.append([x,y])
    while queue:
        top = queue.popleft()
        for k in range(4):
            nx, ny = top[0]+dxy[k][0], top[1]+dxy[k][1]
            if 0 <= nx < N and 0 <= ny< N:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = n
                    queue.append([nx,ny])


def divide(x,y,d1,d2):
    for i in range(d1+1):
        graph[x+i][y-i] = 5
        graph[x+d2+i][y+d2-i] = 5
    
    for j in range(d2+1):
        graph[x+j][y+j] = 5
        graph[x+d1+j][y-d1+j] = 5
    
    for a in range(y-d1):
        graph[x+d1][a] = 3
    
    for b in range(x):
        graph[b][y] = 1
    
    for c in range(y+d2+1, N): 
        graph[x+d2][c] = 2
    
    for d in range(x+d1+d2+1,N):
        graph[d][y+d2-d1] = 4
    
    graph[0][0] = 1
    graph[0][N-1] = 2
    graph[N-1][0] = 3
    graph[N-1][N-1] = 4

    bfs(0,0,1)
    bfs(0,N-1,2)
    bfs(N-1,0,3)
    bfs(N-1,N-1,4)   

    for i in range(N):
        for j in range(N):
            v = graph[i][j]
            res[v-1] += people[i][j]

    

answer = float("Inf")
for x in range(N):
    for y in range(N):
        for d1 in range(1,N):
            for d2 in range(1,N):
                if x+d1+d2 <= N-1 and y+d2 <=N-1 and 0<= y-d1 and y+d2 <= N-2:
                    graph = [[0]*(N) for _ in range(N)]
                    res = [0]*5
                    divide(x,y,d1,d2)
                    answer = min(answer, max(res) - min(res))
    


print(answer)
