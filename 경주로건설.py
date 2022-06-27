lis = [[[0,0,0,0],[0,0,0,0],[0,0,0,0]], [[0,0,0,0],[0,0,0,0],[0,0,0,0]], [[0,0,0,0],[0,0,0,0],[0,0,0,0]]]
lis[0][0][3] = 1
print(lis)
def solution(board):
    N = len(board)
    dp = [[[float("Inf")] * 4 for _ in range(N)] for _ in range(N)]
    visited =[ [False]*(N) for _ in range(N)]
    dxy = [[0,1],[0,-1],[1,0],[-1,0]]
    answer =0
    
    def dfs(x,y,d):
        nonlocal answer
        print()
        print(dp)

        exit(0)
        if x == N-1 and y == N-1:
            return
        
        for k in range(4):
            nx, ny = x+dxy[k][0], y+dxy[k][1]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] or board[nx][ny] == 1:
                continue
            
            if k != d:
                costs = dp[x][y][d] + 500
            else:
                costs = dp[x][y][d] + 100
                
            # print(x,y, nx,ny, costs)
        
            if dp[nx][ny] > costs:
                dp[nx][ny][k] = costs
                visited[nx][ny] = True
                dfs(nx,ny,k)
                visited[nx][ny] = False
    
    dp[0][0] = [0,0,0,0]
    visited[0][0] = True
    print(dp)
    print()
    for i in range(4):
        nx, ny = dxy[i][0], dxy[i][1]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        print(nx,ny,i, dp[nx][ny][i])
        dp[nx][ny][i] = 400
        visited[nx][ny] = True
        print(dp)
        dfs(nx, ny,i)
        visited[nx][ny] = False
    
    print(dp)
    
    return answer

solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])
