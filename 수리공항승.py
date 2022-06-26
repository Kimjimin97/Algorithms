from ast import Pass


N, L = map(int, input().split())

fix = list(map(int, input().split()))

fix.sort()

now=0
cnt = 0
for i in range(N):
    # print(cnt, now)
    if now <= fix[i]-0.5:
        cnt += 1
        now = fix[i] - 0.5 + L
    
    if now < fix[i] + 0.5:
        cnt += 1
        now += L

print(cnt)