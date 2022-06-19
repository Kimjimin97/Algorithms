N = int(input())

lists = list(map(int, input().split()))

diff_lists = [[lists[0],lists[0]+1, lists[0]-1],[lists[1],lists[1]+1,lists[1]-1]]

dxy = [0,1,-1]

    
res = float("Inf")
if len(lists) <=2:
    print(0)
else:
    for i in range(3):
        for j in range(3):
            diff = diff_lists[1][i] - diff_lists[0][j]
            before = diff_lists[1][i]
            cnt = 0
            if i >=1:
                cnt += 1
            if j >= 1:
                cnt += 1
            for k in range(2, len(lists)):
                flag = False
                for th in range(3):
                    if before+diff == lists[k]+dxy[th]:
                        flag = True
                        before = lists[k]+dxy[th]
                        if th >=1 :
                            cnt += 1
                if not flag:
                    break
            
            if flag and k ==  len(lists)-1:
                res = min(res, cnt)

    if res == float("Inf"):
        print(-1)
    else:
        print(res)