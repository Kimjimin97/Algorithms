
while True:
    N,K = map(int, input().split())
    if N == 0 and K == 0:
        break
    parent = dict()
    graph = list(map(int, input().split()))

    if len(graph) <= 2:
        print(0)
        continue

    j = 0 
    before = graph[1]
    parent[graph[j]] = [before]
    parent_node = -1

    for i in range(2, N):
        if before + 1 == graph[i]:
            parent[graph[j]].append(graph[i])
            before = graph[i]
        else:
            j += 1
            parent[graph[j]] = [graph[i]]
            before = graph[i]
        
        if graph[i] == K:
            parent_node = graph[j]


    if parent_node == -1:
        print(0)
        continue

    answer = 0 
    for k in parent.keys():
        if parent_node in parent[k]:
            for kk in parent[k]:
                if parent_node != kk and kk in parent.keys():
                    answer += len(parent[kk])
            break

    print(answer)