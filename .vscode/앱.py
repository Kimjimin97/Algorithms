N , M = map(int, input().split())

memory = [0] + list(map(int, input().split()))
costs = [0]+list(map(int, input().split()))

dp = [[0]*(sum(costs)+1) for _ in range(len(memory)+1)]
result = sum(costs)

for i in range(len(memory)): ## 들어오는 메모리 
    for j in range(len(dp[0])):  ## j 는 비용
        if j < costs[i]: ## 구매하지 못할 때
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-costs[i]]+memory[i], dp[i-1][j])
        
        if dp[i][j] >= M:
            result = min(result, j) ## 메모리가 충족 되었다면, 더 적은 비용 갱신

print(result)