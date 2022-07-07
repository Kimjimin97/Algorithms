import sys
input= sys.stdin.readline
n,x,y = map(int, input().split())
answer = 0
visited = [False]*(n+1)
def dfs(L,lists):

    global answer
    if L == 2*n:
        if lists[x-1] == lists[y-1]:
            answer += 1
        return
    
    if L > max(x,y):
        if lists[x-1] != lists[y-1]:
            return

    if lists[L] != -1:
        dfs(L+1, lists)
        return 
    
    for k in range(1,n+1):
        if visited[k]:
            continue 
        if L+k+1 >= 2*n:
            continue
        if lists[L+k+1] != -1:
            continue 

        visited[k] = True 
        lists[L] = k 
        lists[L+k+1] = k
        dfs(L+1,lists)
        visited[k] = False 
        lists[L] = -1 
        lists[L+k+1] = -1


dfs(0,[-1]*2*n)
        
print(answer)
            
        