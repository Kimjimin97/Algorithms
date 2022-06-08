N, K = map(int, input().split())

lists = list(map(int, input().split()))

sums_list = dict()

sums = 0
answer = 0
for i in range(len(lists)):
    sums += lists[i]

    if sums - K in sums_list:
        answer += sums_list[sums-K]
    if sums == K:
        answer += 1

    if sums in sums_list.keys():
        sums_list[sums] += 1
    else:
        sums_list[sums] = 1

print(answer)