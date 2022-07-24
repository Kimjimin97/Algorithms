from collections import deque

N = int(input())

graph = [[] for _ in range(N+1)]
link_graph = [[] for _ in range(N+1)]
wolf_graph = [0]*(N+1) ## 동적으로 변한다.
sheep_graph = [0]*(N+1) ## 양의 수 


in_cnt = [0]*(N+1)
for k in range(N-1):
    animal, count, link = map(str, input().split())
    count, link = int(count), int(link)
    if animal == "S":
        sheep_graph[k+2] = count
    if animal == "W":
        wolf_graph[k+2] = count
    link_graph[k+2].append(link)
    in_cnt[link] += 1


queue = deque()
answer = 0

# visited = [False] * (N+1)
## 리프노트 찾기
for k in range(2,len(in_cnt)):
    if in_cnt[k] == 0:
        queue.append([k,sheep_graph[k]])
print(queue)

"""
로직 다시 짜기
1. 노드 방문
2. 양이 있다면
   2.1 현재 노드이 wolf = 늑대수 - 양의수
   2.2 wolf가 양수이면 늑대 수 갱신
   2.3 wolf가 음수이면 절대값은 양의 수, 늑대수는 0

"""

while queue:
    print(wolf_graph)
    node, sheep = queue.popleft()
    if node ==1:
        answer += sheep
    for k in link_graph[node]: ## k 이동하려는 곳
        wolf = wolf_graph[k] - sheep 
        
        if wolf > 0:
            wolf_graph[k] = wolf
        else:
            wolf_graph[k] = 0
            queue.append([k,abs(wolf)])

            
print(answer)
