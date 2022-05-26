import sys
limit_number = 1500
sys.setrecursionlimit(limit_number)

input = sys.stdin.readline
n,m = map(int, input().split())

if m != 0:
    must_have = list(map(int, input().split()))

answer = 0
visit = [0]*10
items = [str(i) for i in range(10)]


def dfs(L,s):
    global answer, visit
    if L == n:
        flag = True
        for i in must_have:
            if visit[i] == 0:
                flag = False
        if flag:
            answer += 1
        return
    
    for i in items:
        a = int(i)
        
        if a in must_have:
            visit[a] +=1
            dfs(L+1, s+i)
            visit[a] -=1
        else:
            dfs(L+1, s+i)

dfs(0,"")
print(answer)




# items = [i for i in range(0,10)]



# list_item = list(product(items, repeat = n))



# for xx in list_item:
#     cnt = 0
#     for x in set(xx):
#         if x in must_have:
#             cnt+=1
    
#     if cnt == m:
#         answer += 1

# print(answer)
        