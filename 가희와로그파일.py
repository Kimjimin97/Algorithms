import bisect
N, Q = map(int, input().split())


write_log = [[] for _ in range(7)]


for _ in range(N):
    time1, type = map(str, input().split("#"))
    type = int(type)
    write_log[type].append(time1)
    

def lower_bound(start, k): ## 처음 k가 시작하는 위치
    l = 0
    r = len(write_log[k]) 
    while l<r: 
        mid = (l+r)//2
        if write_log[k][mid] < start: ## mid를 키워야 한다
            l = mid+1

        else:
            r = mid
    return r

def upper_bound(end,k):
    l = 0
    r = len(write_log[k]) 
    while l < r:
        mid = (l+r)//2
        if write_log[k][mid] <= end:
            l = mid+1

        else:
            r = mid
    return r

for _ in range(Q):
    start, end, Qtype =  map(str, input().split("#"))
    count = 0
    Qtype= int(Qtype)
    for k in range(Qtype,7):
        if (len(write_log[k]) <= 0) or (write_log[k][0] < start):
            continue
    
        lc = bisect.bisect_left(write_log[k],start)
        uc = bisect.bisect_right(write_log[k],end)
        count += (uc-lc)
    print(count)
