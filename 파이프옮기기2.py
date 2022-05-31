N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))



memo = [[[0]*N for _ in range(N) ] for  _ in range(3)]



## 가로 방향 먼저 설정
memo[0][0][1] = 1

for i in range(N):
    for j in range(1,N):

        if graph[i][j] == 1:
            continue

        if i == 0:
            if j == 1:
                memo[0][i][j] = 1
                continue
             ## 왼쪽에서 들어오는 경로 ( 가로 방향이 됌)
            else:
                memo[0][i][j] = (memo[0][i][j-1] + memo[2][i][j-1])
                continue
    
        ## 위에서 들어오는 경로 (세로 방향이 됌)
        memo[1][i][j] = (memo[1][i-1][j] + memo[2][i-1][j])


        ## 왼쪽에서 들어오는 경로 ( 가로 방향이 됌)
        memo[0][i][j] = (memo[0][i][j-1] + memo[2][i][j-1])

        ## 대각선에서 들어오는 경로 (대각선 방향이 됌)
        if graph[i-1][j] == 1 or graph[i][j-1] == 1:
            continue
        else:
            memo[2][i][j] = (memo[0][i-1][j-1] + memo[1][i-1][j-1]+memo[2][i-1][j-1])



answer = 0
for a in range(3):
    answer += memo[a][N-1][N-1]

print(answer)
