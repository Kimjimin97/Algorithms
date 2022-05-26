import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

distance = list(map(int, input().split()))
costs = list(map(int, input().split()))

d = sum(distance)


queue = deque()
answer = float("Inf")
# 노드 번호, 가격, 남은 기름, 남은 거리
# 다음 노드까지 갈 수 있는 기름 ~ 전체까지 갈 수 있는 기름양

dd = 0
sum_dis = []
for i in range(len(distance)):
    dd += distance[i]
    sum_dis.append(d-dd)



for i in range(distance[0],d+1):

    queue.append((0, i*costs[0], i-distance[0]))

# print(sum_dis)
while queue:
    # print(queue)
    top = queue.popleft()
    
    node, cost, res_oil= top[0] + 1, top[1], top[2]

    if node == N-1:
        answer = min(answer, cost)
        continue

    for k in range(distance[node]-res_oil, sum_dis[top[0]]+1):
        queue.append((node, cost+k*costs[node], res_oil+k-distance[node]))


print(answer)