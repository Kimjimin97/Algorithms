N, K = map(int, input().split())

lists = list(map(int,input().split()))


cnt = 0

for i in range(N):
    sum = lists[i]
    if sum == K:
        cnt += 1
    for j in range(i+1,N):
        sum += lists[j]
        if sum == K:
            cnt += 1

print(cnt)