

import sys
sys.setrecursionlimit(10**9)


N = int(input())
nums = list(map(int, input().split()))

res = float("Inf")

def dfs(L,s, num):
    global res
    if len(s) <= 1:
        res = min(res, num)
        return
    
    if num >= res:
        return


    if s[0] == s[-1]:
        ns = s[1:-1]
        dfs(L+1, ns, num)
    
    else:
        # 앞에 문자열 맞추기
        ns = s[1:]
        dfs(L+1,ns,num+1)

        # 뒤에 문자열 맞추기
        ns = s[:-1]
        dfs(L+1,ns,num+1)


dfs(0,nums, 0)
print(res)