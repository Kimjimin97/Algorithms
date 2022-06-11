

N = int(input())

lists = list(map(int, input().split()))


able_lists = []


move = [1,-1,0]

for i in range(N):
    able = []
    for j in range(3):
        able.append(lists[i]+move[j])
    able_lists.append(able)


res = float("Inf")

print(able_lists)
for i in range(len(able_lists[0])):
    for j in range(len(able_lists[1])):
        diff = able_lists[1][j] - able_lists[0][i]
        before = able_lists[1][j]
        answer = 0
        if i != 2:
            answer += 1
        if j != 2:
            answer += 1

        correct = diff+before
        flag1 = True
        for k in range(2,len(able_lists)):
            flag2 = False
            for w in range(3):
                if able_lists[k][w] == correct:
                    flag2 = True
                    before = correct
                    if w != 2:
                        answer += 1
            if not flag2:
                flag1 = False
                break
        
        if flag1:
            res = min(res, answer)

print(res)

