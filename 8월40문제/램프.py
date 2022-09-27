
N,M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

k = int(input())
answer = 0

for i in range(N):
    n = graph[i].count(0)
    check_same = 0
    if n <= k and n % 2 == k % 2:
        for j in range(N):
            if graph[i] == graph[j]:
                print(i,j)
                check_same += 1
        answer = max(answer, check_same)

print(answer)