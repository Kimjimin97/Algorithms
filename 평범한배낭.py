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

print(memo[-1][-1])