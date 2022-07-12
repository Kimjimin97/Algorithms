"""
의사결정 : 물건으로 

로직

(물건, 무게)
- 무게에서 들어오는 물건을 뺀 것 무게 상태에서 가치 + 들어오는 물건의 가치
- 물건을 선택하지 않을 떼의 물건의 가치

"""

N,K = map(int, input().split())

graph = [[0,0]]
for _ in range(N):
    graph.append(list(map(int, input().split())))


memo = [[0]*(K+1) for _ in range(N+1)]
answer = float("-Inf")
for item in range(1, N+1):
    for w in range(K+1):
        weight, value = graph[item][0], graph[item][1]
        if w - weight >= 0:
            memo[item][w] = max(memo[item-1][w], memo[item-1][w-weight] + value)
        else:
            memo[item][w] = memo[item-1][w]
        if w == K:
            answer = max(answer, memo[item][w])
        
print(answer)
