N, M = map(int, input().split())
lists = []

def dfs(L):
    global lists
    if L == M:
        print(*lists)
        return
    for i in range(1, N+1):
        lists.append(i)
        dfs(L+1)
        lists.pop()

dfs(0)