from collections import deque


N = int(input())


wolf_graph = [0,0]
graph = [[],[]]
in_cnt = [0]*(N+1)

for _ in range(N-1):
    a,b,c = map(str, input().split())
    graph.append([a,int(b),int(c)])
    in_cnt[int(c)] += 1
    if a == "W":
        wolf_graph.append(int(b))
    else:
        wolf_graph.append(0)

queue = deque()

for i in range(2,len(in_cnt)):
    if in_cnt[i] == 0:
        if graph[i][0] == "S":
            queue.append([graph[i][1],i])
        else:
            queue.append([0,i])


answer =0

## 방문처리

while queue:
    in_sheep, node = queue.popleft()
    now_node = graph[node][2]

    if now_node == 1:
        answer += in_sheep
        continue

    if graph[now_node][0] == "S":
        in_sheep += graph[now_node][1]
        graph[now_node][1] = 0

    else:
        now_wolf = wolf_graph[now_node]
        cnt = now_wolf - in_sheep

        if cnt >= 0 : ## 늑대 수가 많을 때-> 양의 수는 줄고/ 늑대수 또한 준다.
            in_sheep = 0
            wolf_graph[now_node] = cnt 
        else:
            in_sheep = cnt*(-1)
            wolf_graph[now_node] = 0
    queue.append([in_sheep, now_node])
print(answer)