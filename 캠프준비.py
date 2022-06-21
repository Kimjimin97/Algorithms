N, L, R, X = map(int, input().split())

problems = list(map(int, input().split()))

cnt = 0

def dfs(idx, pick):
    global cnt
    if idx == len(problems):
        if L <= sum(pick) <= R and max(pick) - min(pick) >= X and len(pick) >=2:
            cnt +=1
        return
    
    pick.append(problems[idx])
    dfs(idx+1,pick)
    pick.pop()
    dfs(idx+1, pick) 

dfs(0,[])
print(cnt)