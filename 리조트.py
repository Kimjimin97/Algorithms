from collections import deque
N,M = map(int, input().split())

queue = deque()

impossible = list(map(int, input().split()))

# 날짜, 비용, 쿠폰
queue.append((1,0,0))

days = [1,3,5]
costs = [10000,25000,37000]

res = float("Inf")
# print(queue)

# memo = [[0,0]]*(N+2)
# for i in range(1,N+1):
#     Min_cost = min(Min_cost, memo[i][0])

#     if i in impossible:
#         memo[i+1][0] = Min_cost
        
#         continue

#     for j in range(3):
#         if memo[i+days[j]][0] >  memo[i][0]+costs[i]:
#             memo[i+days[j]][0] = memo[i][0]+costs[i]
#             memo[i+days[j]][1] = memo[i][1]+j
        


while queue:
    top = queue.popleft()
    if top[0] == N+1:
        print(top)
        res = min(res, top[1])
        continue


    if top[1]>res:
        continue


    # 못가는 날
    if top[0] in impossible:
        queue.append([top[0]+1,top[1],top[2]])
        continue

    #쿠폰 사용
    if top[2] >= 3:
        if top[0]+1 <= N+1:
            queue.append([top[0]+1,top[1],top[2]-3])
    else:
        for i in range(3):
            if top[0]+days[i] <= N+1:
                queue.append([top[0]+days[i],top[1]+costs[i],top[2]+i])

print(res)