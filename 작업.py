
N = int(input())

out_graph = [[] for _ in range(N+1)]
in_cnt = [0]*(N+1)
time_graph = [0]*(N+1)

queue = []

for i in range(N):
    lists = list(map(int, input().split()))
    time_graph[i+1] = lists[0]  
    if lists[1] == 0:
        queue.append([i+1,lists[0]])
    for j in range(2, len(lists)):
        out_graph[lists[j]].append(i+1)
        in_cnt[i+1] += 1



while queue:
    queue.sort(key = lambda x: x[1],reverse=True)
    top = queue.pop()
    for a in out_graph[top[0]]:
        in_cnt[a] -= 1
        if in_cnt[a] == 0:
            queue.append([a, top[1]+time_graph[a]])


print(top[1])
