# 진입갯수가 0인 노드 찾기
# 0인 노드를 pop해서 연결노드의 진입 갯수 줄이기
# 만약 진입 객수가 0 이면 queue에 넣는다.
'''
시간복잡도
O(V+E)
간선 들어가기 
간선 끊어내기
'''

from collections import deque
N, M = map(int, input().split())

out_graph = [[] for _ in range(N+1)]
in_cnt = [0]*(N+1)


for _ in range(M):
    a,b = map(int, input().split())
    out_graph[a].append(b)
    in_cnt[b] += 1

queue = deque()
answer = []

for i in range(1,N+1):
    if in_cnt[i] == 0:
        queue.append(i)
        answer.append(i)

while queue:
    top = queue.popleft()
    for k in out_graph[top]:
        in_cnt[k]-= 1
        if in_cnt[k] == 0:
            queue.append(k)
            answer.append(k)

print(*answer)



