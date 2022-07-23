from collections import deque

N = int(input())

graph = [[] for _ in range(N+1)]
link_graph = [[] for _ in range(N+1)]

for k in range(N-1):
    animal, count, link = map(str, input().split())
    count, link = int(count), int(link)
    if animal == "S":
        graph[k+2] = [count,0]
    if animal == "W":
        graph[k+2] = [0, count]
    link_graph[link].append(k+2)



queue = deque()
answer = 0
## 첫번째 노드
for k in link_graph[1]:
    sheep, wolf = map(int, graph[k])
    answer += sheep
    queue.append([k,wolf])

while queue:
    node, total_wolf = queue.popleft()
    for k in link_graph[node]:
        sheep, wolf = map(int, graph[k])
        if sheep - total_wolf > 0:
            answer += (sheep - total_wolf)
        total_wolf += wolf
        queue.append([k,total_wolf])

print(answer)
