from collections import deque
N, M = map(int, input().split())

queue = deque()

graph =[[-1]*2 for _ in range(500001)]

# [시간][짝수(0) or 홀수(1) 시간]

# 어떤 시간 x 초에 어떤 위치에 도달했다면 2초 마다 x 위치에 도달할 수 있다. 최초로 도착할 수 있는 시간을 정해둔다.
# 짝수와 홀수 초마다 반복이 달라지기 때문에 따로 저장 해주어야 한다.

graph[N][0] = 0
queue.append([N,0])


while queue:
    now_loca, now_time = queue.popleft()

    for move_loca in [now_loca+1, now_loca-1, now_loca*2]:
        if 0<= move_loca <=500000 and 0 <= now_time+1 <= 500000:
            if graph[move_loca][(now_time+1)%2] == -1:
                graph[move_loca][(now_time+1)%2] = now_time+1
                queue.append((move_loca, now_time+1))



ans = -1
for i in range(500000):
    M += i
    if M > 500000:
        ans = -1
        break
    if graph[M][i%2] <= i: #짝수 초에 언니보다 나중에 도착했으면 i 초에 만날 수 있다.
        ans = i
        break

print(ans)
