from itertools import product
n,m = map(int, input().split())

if m != 0:
    must_have = list(map(int, input().split()))

answer = 0

items = [i for i in range(0,10)]



list_item = list(product(items, repeat = n))



for xx in list_item:
    cnt = 0
    for x in set(xx):
        if x in must_have:
            cnt+=1
    
    if cnt == m:
        print(xx)
        answer += 1

print(answer)