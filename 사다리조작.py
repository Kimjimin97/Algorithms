from ast import Return
from genericpath import exists
from operator import truediv
from pickle import FALSE


N,M,H = map(int, input().split())


exist = [[False]*(N+1) for _ in range(H+1)]

for _ in range(M):
    a,b = map(int, input().split())
    exist[b-1][a-1] = True 

res = float("Inf")

def dfs(goal,x,y,n):
    global res
    print(goal,x,y,n)
    if n > 3:
        return
    
    if goal == N-1 and x == H and y == goal:
        res = min(res, n)
        return
    

    if x == H :
        if y == goal:
            # print(goal,x,y,n)
            dfs(goal+1, 0, goal+1,n)
            return
        else:
            return    


 

    if exist[x][y]:
        dfs(goal, x+1,y+1,n)
    
    elif exist[x][y-1]:
        dfs(goal,x+1,y-1,n)

    else:
        if y+1 <= N-1 and x+1 <= H:
            dfs(goal, x+1, y, n)
            if not exist[x][y+1] :
                exist[x][y] = True
                dfs(goal,x+1, y+1, n+1)
                exist[x][y] = False 
        
        if not exist[x][y-1]:
            if y-1 >= 0 and x+1 <=H:
                exist[x][y-1] = True
                dfs(goal,x+1, y-1, n+1)
                exist[x][y-1] = False 
        
        

print()
dfs(0,0,0,0)
print(res)

    