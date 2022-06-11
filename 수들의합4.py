N, K = map(int, input().split())

lists = list(map(int, input().split()))

sums_list = dict()

sums = 0
answer = 0
for i in range(len(lists)):
    sums += lists[i]

    # 해당 누적합이 K와 같은 경우는 두가지  경우도 만족해야한다.
    #  때문에 if else문이 아닌 두개의 if문으로 작성해야한다.
    if sums - K in sums_list:
        answer += sums_list[sums-K]
    if sums == K:
        answer += 1

    if sums in sums_list.keys():
        sums_list[sums] += 1
    else:
        sums_list[sums] = 1

print(answer)