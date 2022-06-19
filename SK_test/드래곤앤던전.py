from itertools import combinations

item = ["a","b","c","d","e","f","g","h","i",
"j","k","l","m","n","o","p","q","r","s",
"t","u","v","w","x","y","z"]

N = int(input())

lists = list(map(str, input()))

items = list(combinations(item,N))


answer = float("-Inf")
for case in items:
    cnt = 0
    res = float("-Inf")
    for i in lists:
        if i in case:
            cnt += 1
        else:
            res = max(cnt, res)
            cnt = 0

    res = max(cnt, res)
    answer = max(answer, res)


print(answer)

