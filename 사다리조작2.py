

N,M,H = map(int, input().split())

exist = [[False]*(N+1) for _ in range(H+1)]

for _ in range(M):
    a,b = map(int, input().split())
    exist[b-1][a-1] = True 

res = float("Inf")

visited = [[False]*N for _ in range(H)]
dxy =[[0,1],[0,-1],[1,0],[-1,0]]

def check():
    for j in range(len(exist[0])):
        i = 0
        flag= False
        while True:
            if i == H:
                flag= True
                break
            if exist[i][j]:
                i += 1
                j += 1

            elif j > 0 and exist[i][j-1]:
                i += 1
                j -= 1
            else:
                i += 1
        
        if not flag:
            return False
    if flag:
        return True
    
res = float("Inf")
        


def dfs(x,y,n):
    global res
    print(x,y,n)
    if n > 3:
        return
    
    if check():
        res = min(res, n)
        return
    
    for i in range(x,H):
        


    for k in range(4):
        nx, ny = x +dxy[k][0], y+ dxy[k][1]
        if 0 < ny < N-2 and 0 < nx <= H-1:
            if not visited[nx][ny]:
                visited[nx][ny] = True 
                # dfs(nx,ny,n)
                if not exist[nx][ny-1] and not exist[nx][ny+1]:
                    exist[nx][ny] = True
                    dfs(nx,ny,n+1)
                    exist[nx][ny] = False
                visited[nx][ny] = False

dfs(0,0,0)
print(res)