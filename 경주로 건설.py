def solution(board):
    N = len(board)
    dp = [[[0,0,0,0]]*N for _ in range(N)]

    visited =[ [[False]*4]*(N) for _ in range(N)]
    dxy = [[0,1],[0,-1],[1,0],[-1,0]]
    answer =0
    
    def dfs(x,y,d):
        nonlocal answer
        # print(x,y)
        if x == N-1 and y == N-1:
            return
        for k in range(4):
            nx, ny = x+dxy[k][0], y+dxy[k][1]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny][k] or board[nx][ny] == 1:
                continue
            
            if k != d:
                costs = dp[x][y][d] + 500
            else:
                costs = dp[x][y][d] + 100
            # print(costs)
            if dp[nx][ny][k] > costs:
                dp[nx][ny][k] = costs
                visited[nx][ny] = True
                dp[nx][ny] = min(dp[nx][ny], d)
                visited[nx][ny] = False
    
    for i in range(4):
        nx, ny = dxy[i][0], dxy[i][1]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        dp[nx][ny][i] = 0
        visited[nx][ny][i] = True
        dfs(nx, ny,i)
        visited[nx][ny][i] = False
    
    print(dp)
    # answer = max(board[nx][ny])
            
        
    return answer

solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])