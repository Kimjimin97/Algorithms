from bisect import bisect_left

N =  int(input())

lists = list(map(int, input().split()))
items = []
answer = 0

for k in lists:
    if not items:
        items.append(k)
        answer += 1
    else:
        ## 들어오는 수가 작으면
        if k <= items[-1]:
            in_ind = bisect_left(items,k)
            items[in_ind] = k
        else:
            items.append(k)
            answer += 1


