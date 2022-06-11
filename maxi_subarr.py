T = int(input())

for _ in range(T):
    n = int(input())
    res = float("-Inf")
    lists =  list(map(int, input().split()))
    for i in range(n):
        answer = lists[i]
        res = max(res, answer)
        for j in range(i+1, n):
            answer += lists[j]
            res = max(res, answer)

    print(res)