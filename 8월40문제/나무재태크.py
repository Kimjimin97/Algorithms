import sys
N,M,K = map(int, input().split())

input = sys.stdin.readline
food = []
for _ in range(N):
    food.append(list(map(int, input().split())))

A = [[5]*N for _ in range(N)]

graph = [[[] for _ in range(N)] for _ in range(N)]



##  1은 산 나무, 0은 죽은 나무
for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a-1][b-1].append([c]) 

while K > 0:
    for i in range(N):
        for j in range(N):
            for k in range(len(graph[i][j])):
                if A[i][j] >= graph[i][j][k]:
                    A[i][j] -= graph[i][j][k]
                    tree[i][j][k] += 1
                else:
                    for kk in range(k,len(graph[i][j])):
                        A[i][j] += graph[i][j].pop() //2
                    break
    
    for i in range(N):
        for j in range(N):
            for z in graph[i][j]:
                if z%5 == 0:
                    for l in range(8):
                        nx  = i +dxy[l]
                        ny = j +dxy[l]
                        if 0 <= nx <N and  0 <= ny <N:
                            graph[nx][ny].append(0)
            
            graph[i][j] += food[i][j]
    K-=1

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(graph[i][j])


print(graph)
